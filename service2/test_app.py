from app import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRandomNumberGenerator(TestBase):
    def test_random_number_generator(self):
        response = self.client.get(url_for('test_random_number_generator'))
        self.assertEqual(len(response.data), 1)

class TestRandomNumberGen(TestBase):
    def test_random_number_gen(self):
        response = self.client.get(url_for('test_random_number_gen'))
        self.assertEqual(response.status_code, 200)