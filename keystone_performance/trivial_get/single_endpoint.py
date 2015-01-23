import locust


class Authenticate(locust.TaskSet):

    @locust.task
    def authenticate(self):
        # Set header information and path
        headers = {'content-type': 'application/json'}
        path = '/'

        # Since this is a python-request object handed to us on HttpLocust()
        # object initialization, we can pass extra stuff if necessary using
        # kwargs. Call to POST `/v3/auth/tokens` and capture the response
        # object.
        response = self.client.get(path, headers=headers)


class KeystoneUser(locust.HttpLocust):
    task_set = Authenticate
    min_wait=1000
    max_wait=1000
