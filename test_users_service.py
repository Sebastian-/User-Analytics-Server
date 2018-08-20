import json
import unittest
from flask_testing import TestCase

from service import app


class TestUsersAPI(TestCase):
    """Unit tests for users api"""


    def create_app(self):
        return app


    def test_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


    # Tests for /unique-users =====================================================================
    """ Brute forced values

        Number of unique users is 8550022
        Users using OS 1: 1249619
        Users using OS 0 and 6: 1477249
        Users using device 3: 767244
        Users using device 0 and 5: 1285700
        Users using OS 1 and device 1: 6143198
    """
    def test_unique_users(self):
        """Ensure /unique-users response matches the brute forced value"""
        response = self.client.get('/unique-users')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(8550022, data['count'])


    def test_unique_users_single_os(self):
        """Ensure /unique-users?os=1 response matches the brute forced value"""
        response = self.client.get('/unique-users?os=1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1249619, data['count'])


    def test_unique_users_multiple_os(self):
        """Ensure /unique-users?os=0,6 response matches the brute forced value"""
        response = self.client.get('/unique-users?os=0,6')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1477249, data['count'])


    def test_unique_users_single_device(self):
        """Ensure /unique-users?device=3 response matches the brute forced value"""
        response = self.client.get('/unique-users?device=3')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(767244, data['count'])


    def test_unique_users_multiple_device(self):
        """Ensure /unique-users?device=0,5 response matches the brute forced value"""
        response = self.client.get('/unique-users?device=0,5')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1285700, data['count'])


    def test_unique_users_combined(self):
        """Ensure /unique-users?device=1&os=1 response matches the brute forced value"""
        response = self.client.get('/unique-users?device=1&os=1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(6143198, data['count'])


    # Tests for /loyal-users ======================================================================

    """ Brute forced values:

        Number of loyal users is 563740
        Loyal users using OS 1: 81413
        Loyal users using OS 0 and 6: 140467
        Loyal users using device 3: 79508
        Loyal users using device 0 and 5: 24561
        Loyal users using OS 1 and device 1: 414706
    """

    def test_loyal_users(self):
        """Ensure /loyal-users response matches the brute forced value"""
        response = self.client.get('/loyal-users')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(563740, data['count'])


    def test_loyal_users_single_os(self):
        """Ensure /loyal-users?os=1 response matches the brute forced value"""
        response = self.client.get('/loyal-users?os=1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(81413, data['count'])


    def test_loyal_users_multiple_os(self):
        """Ensure /loyal-users?os=0,6 response matches the brute forced value"""
        response = self.client.get('/loyal-users?os=0,6')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(140467, data['count'])


    def test_loyal_users_single_device(self):
        """Ensure /loyal-users?device=3 response matches the brute forced value"""
        response = self.client.get('/loyal-users?device=3')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(79508, data['count'])


    def test_loyal_users_multiple_device(self):
        """Ensure /loyal-users?device=0,5 response matches the brute forced value"""
        response = self.client.get('/loyal-users?device=0,5')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(24561, data['count'])


    def test_loyal_users_combined(self):
        """Ensure /loyal-users?device=1&os=1 response matches the brute forced value"""
        response = self.client.get('/loyal-users?device=1&os=1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(414706, data['count'])


if __name__ == '__main__':
    unittest.main()
