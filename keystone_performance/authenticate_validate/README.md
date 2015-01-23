# Authenticate and Validate

This locust swarm sends and authentication request, and if successful, proceeds
with sending several validate requests using the token from the authentication
call.

This test case is useful when testing the minimum time between replication
nodes behind the API node.

### Setup

Install locustio according to the [installation directions].

Load and run the locust swarm with the following:

```sh
$ locust -H http://<api_ip_address> -f single_endpoint.py
```

By default, the locust user interface should be available on port 8089. Through
locust you can define the number of users to simulate and the hatch rate of the
swarm.

[installation directions] http://docs.locust.io/en/latest/installation.html
