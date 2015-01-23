# Single Endpoint Authenticate and Validate

This locust swarm sends and authentication request, and if successful, proceeds
with sending several validate requests using the token from the authentication
call. This test is designed to authenticate against one endpoint, and validate
the token recieved against another endpoint.

This test is useful when testing the replication time between API nodes and
their respective backends.

### Setup

Load and run the locust swarm with the following:

```sh
$ python locustfile.py
```

By default, the locust user interface should be available on port 8089. Through
locust you can define the number of users to simulate and the hatch rate of the
swarm.
