from flask_testing import TestCase
from flask import Flask, url_for
from flask import Response, request
from os import getenv
import random
from service2 import app

#pytest --cov=app --cov-report=term-missing
#pytest --cov . --cov-report html

class TestBase(TestCase):
    def create_app(self):
        # Pass in testing configurations for the app.

    def setUp(self):
        # Will be called before every test
        # Create table
        # Create test registree
        # Save users to database

    def tearDown(self):
        # Will be called after every test

class TestRandomNumberGenerator(TestBase):
    def test_random_number_generator(self):
        #write test for random number generation