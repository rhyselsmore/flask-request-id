# -*- coding: utf-8 -*-

"""Tests for flask-request-id."""

import flask
import flask_request_id
import unittest


REQUEST1 = "01234567-89ab-cdef-0123-456789abcdef"
REQUEST2 = "01234567-abcd-cdef-0123-456789abcdef"


class FlaskRequestIDTestCase(unittest.TestCase):

	def setUp(self):
		self.app = flask.Flask(__name__)

		@self.app.route('/')
		def index():
			return "Hello, World"

		self.request_id = flask_request_id.RequestID()
		self.request_id.init_app(self.app)

	def test_module_proxies(self):
		with self.app.test_client() as c:
			rv = c.get('/')
			assert flask_request_id.id is not None
			assert len(flask_request_id.ids) == 1

	def test_instance_proxies(self):
		with self.app.test_client() as c:
			rv = c.get('/')
			assert self.request_id.id is not None
			assert len(self.request_id.ids) == 1

	def test_with_passed_id(self):
		with self.app.test_client() as c:
			rv = c.get('/', headers={
				"Request-ID": REQUEST1
			})
			assert len(flask_request_id.ids) == 2

	def test_headers_set(self):
		with self.app.test_client() as c:
			rv = c.get('/', headers={
				"Request-ID": REQUEST1
			})
			self.assertIsNotNone(rv.headers.get('Request-ID'))
