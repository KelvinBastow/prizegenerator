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

class TestRandomNumberGenerator(TestBase):
    def test_random_number_generator(self):
        response = self.client.get(url_for("random_number_generator"))
        self.assertEqual(len(response.data), 1)