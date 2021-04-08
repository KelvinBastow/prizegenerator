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

class TestRandomLetterGenerator(TestBase):
    def test_random_letter_generator(self):
        response = self.client.get(url_for("random_letter_generator"))
        self.assertEqual(len(response.text), 6)