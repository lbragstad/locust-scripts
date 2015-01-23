# Single Endpoint Authenticate and Validate

This locust swarm sends and authentication request, and if successful, proceeds
with sending several validate requests using the token from the authentication
call. Each request is sent to a single endpoint, or API node.

This test case is useful when testing the minimum time between replication
nodes behind the API node.

Load and run the locust swarm with the following:

```sh
$ python locustfile.py
```

By default, the locust user interface should be available on port 8089.
