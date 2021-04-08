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
        app
        # Pass in testing configurations for the app.

    # def setUp(self):
    #     # Will be called before every test
    #     # Create table
    #     # Create test registree
    #     # Save users to database

    # def tearDown(self):
    #     # Will be called after every test

class TestPrizeGenerator(TestBase):
    def test_prize_generator(self):
        response = self.client.get('http://35.242.157.198:5000')
        self.assertEqual(response.status_code, 200)