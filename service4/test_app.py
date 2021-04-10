from flask_testing import TestCase
from flask import url_for
from app import app
from mock import patch

#pytest --cov=app --cov-report=term-missing
#pytest --cov . --cov-report html

class TestBase(TestCase):
    def create_app(self):
        return app

# class TestPrizeCreation(TestBase):
#     def test_prize_creation(self):
#         # write test for combining service 2 & 3 together to create result
#         with patch('requests.get') as g:

#             response = self.client.get(url_for("test_prize_creation"))
#             g.return_value.text = "abbcde"

#             self.assertIn(b'6', response.data)

class TestPrizeCreator(TestBase):
    def test_prize_creator(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)