from flask_testing import TestCase
from flask import url_for
from app import app
import requests_mock

#pytest --cov=app --cov-report=term-missing
#pytest --cov . --cov-report html

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPrizeCreation(TestBase):
    def test_prize_creation(self):
        with requests_mock.mock() as m:
            m.get('http://service2:5001/randomnumberm', text = '2')
            m.get('http://service3:5002/randomletters', text = 'eerthf')
            response = self.client.get('http://service4:5003/prizecreator')
            self.assertIn(b'200', response.data)
            self.assertIn(b'20', response.data)

class TestPrizeCreator(TestBase):
    def test_prize_creator(self):
        response = self.client.get('http://service4:5003/prizecreator')
        self.assertEqual(response.status_code, 200)