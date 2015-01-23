from time import sleep

import locust
import json


class Authenticate(locust.TaskSet):

    @locust.task
    def authenticate(self):
        # Set header information and path
        headers = {'content-type': 'application/json'}
        path = '/v3/auth/tokens'
        # Build authentication request with an existing user. This will be
        # an unscoped token request.
        request = {
            'auth': {
                'identity': {
                    'methods': [
                        'password'
                    ],
                    'password': {
                        'user': {
                            'id': '9fff846eb28442418612b94fccda9264',
                            'password': 'sup3rs3cr3t'
                        }
                    }
                }
            }
        }

        # Since this is a python-request object handed to us on HttpLocust()
        # object initialization, we can pass extra stuff if necessary using
        # kwargs. Call to POST `/v3/auth/tokens` and capture the response
        # object.
        response = self.client.post(path, data=json.dumps(request),
                headers=headers)

        # If we know we can pull a token out of the `X-Subject-Token` header,
        # then proceed with the test plan and immediately attempt to validate
        # the token several times. Here we are trying to see if we can get 
        # Keystone to throw a 404.
        if response.status_code == 201:
            token = response.headers['X-Subject-Token']
            # TODO(lbragstad): Turn this test case into one that supports
            # generating an admin token with an admin user, instead of using
            # auth_token.
            admin_token = 'ADMIN'
            headers = {'X-Subject-Token': token,
                       'X-Auth-Token': admin_token}
            for i in range(5):
                response = self.client.get(path, headers=headers)


class KeystoneUser(locust.HttpLocust):
    task_set = Authenticate
    min_wait=1000
    max_wait=1000
