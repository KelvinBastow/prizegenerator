from flask_testing import TestCase
from flask import Flask, url_for
from flask import Response, request
from os import getenv
import random
from app import app

#pytest --cov=app --cov-report=term-missing
#pytest --cov . --cov-report html

class TestBase(TestCase):
    def create_app(self):
        return app
        # Pass in testing configurations for the app.

class TestHome(TestBase):
    def test_home(self):
        #write test for combining service2 & 3 together to create result
        response = self.client.get(url_for("test_home"))