# flask-request-id

Make Request IDs available to your app, and also send one back to the client.

![](https://travis-ci.org/rhyselsmore/flask-request-id.svg)

## Usage

So simple.

```python
from flask import Flask
from flask_request_id import RequestID

app = Flask(__name__)
request = RequestID(app)
```

You can then access the IDs in various ways.

### As part of the module

```python
>>> flask_request_id.ids
['abc123']
```

### As part of the extension instance

```python
>>> request.id
'abc123'
```

## Testing:

- use [tox](https://pypi.python.org/pypi/tox).

```bash
$ pip install tox
$ tox
```

- This takes care of py.test and all the other craziness.

## Contributing:

send me pull requests & doritos.
