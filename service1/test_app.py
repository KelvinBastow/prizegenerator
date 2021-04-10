from prizegenerator.service1.app import PrizeGenerator
from flask_testing import TestCase
from flask import url_for
from app import app ,db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        prizegenerator = PrizeGenerator(random_number = service_four_default_response['9'],random_letter = service_four_default_response['gfhfgt'])
        db.session.add(prizegenerator)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestPrizeGenerator(TestBase):
    def test_prize_generator(self):
        response = self.client.get(url_for('test_prize_generator'))
        self.assertEqual(response.status_code, 200)