import unittest
from app.models import User


class UserModelTestUase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertTrue(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
