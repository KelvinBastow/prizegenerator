from flask_testing import TestCase
from flask import Flask, url_for
from flask import Response
from os import getenv
import random
from app import app
import requests
#pytest --cov=app --cov-report=term-missing
#pytest --cov . --cov-report html

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRandomLetterGenerator(TestBase):
    def test_random_letter_generator(self):
        response = requests.get(url_for('test_random_letter_generator')).text
        response = str(response)
        self.assertEqual(len(response), 6)

class TestRandomLetterGen(TestBase):
    def test_random_letter_gen(self):
        response = self.client.get(url_for('test_random_letter_gen'))
        self.assertEqual(response.status_code, 200)