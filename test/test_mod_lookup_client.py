import unittest
from src.mod_lookup_client import ModLookupClient
import json


class TestModLookupClient(unittest.TestCase):

    def setUp(self):
        self.test_user = 'artosis'
        self.client = ModLookupClient()

    def test_can_get_user(self):
        response = json.loads(self.client.get_user(self.test_user))
        self.assertEqual(200, response['status'])

    def test_can_get_user_total(self):
        response = json.loads(self.client.get_user(self.test_user))
        self.assertEqual(200, response['status'])

    def test_can_get_top(self):
        response = json.loads(self.client.get_top())
        self.assertEqual(200, response['status'])

    def test_can_get_stats(self):
        response = json.loads(self.client.get_top())
        self.assertEqual(200, response['status'])


if __name__ == '__main__':
    unittest.main()
