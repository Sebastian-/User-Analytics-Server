import json
import unittest

from flask_testing import TestCase
from service.users_api import app


class TestUsersAPI(TestCase):

    def create_app(self):
        return app

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
