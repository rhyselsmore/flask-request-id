from werkzeug.local import LocalProxy
from flask import request
import wsgi_request_id


id = LocalProxy(lambda: request.environ.get('REQUEST_ID'))
ids = LocalProxy(lambda: request.environ.get('REQUEST_IDS'))


class RequestID(object):

	def __init__(self, app=None):
		if app:
			self.init_app(app)

	def init_app(self, app):
		app.wsgi_app = wsgi_request_id.init_app(app.wsgi_app)

	@property
	def id(self):
		return id

	@property
	def ids(self):
		return ids
