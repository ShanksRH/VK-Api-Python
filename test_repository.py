import unittest
import json
import repository

url = 'http://magic.troll.me/'
token = 'abrakadabra'

class TestRepositories(unittest.TestCase):
    def test_users_repository(self):
        rep = repository.UsersRepository(url)
        self.assertNotEqual(rep, None)

if __name__ == "__main__":
    unittest.main()