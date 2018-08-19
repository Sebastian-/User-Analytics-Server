import json
import unittest

from flask_testing import TestCase
from service.users_api import app


class TestUsersAPI(TestCase):

    def create_app(self):
        return app

    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_unique_users(self):
        """Ensure /unique-users response matches the brute forced value"""
        response = self.client.get('/unique-users')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('8550022', data['count'])



if __name__ == '__main__':
    unittest.main()
