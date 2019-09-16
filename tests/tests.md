# tests

to run tests, install `python-requests` and run:

```
pytest test_put.py -v
```

-- to check put requests (updating bears) or

```
pytest test_post.py -v
```

-- to check post requests (creating bears)

To run the tests, docker instance should be running at `172.17.0.1` address.
