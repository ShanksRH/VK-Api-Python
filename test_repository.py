import unittest
import json
import repository

url = 'http://magic.troll.me/'
token = 'abrakadabra'

class TestRepositories(unittest.TestCase):
    def test_users_repository(self):
        rep = repository.UsersRepository(url)
        self.assertNotEqual(rep, None)
    
    def test_groups_repository(self):
        rep = repository.GroupsRepository(url)
        self.assertNotEqual(rep, None)
    
    def test_get_friends(self):
        rep = repository.UsersRepository(url)
        res = rep.getUserFriends(1, token)
        self.assertEqual(res, [1, 2, 3])
    
    def test_get_friends_2(self):
        rep = repository.UsersRepository(url)
        res = rep.getUserFriends(2, token)
        self.assertEqual(res, [10, 12, 33, 46])
    
    def test_get_friends_3(self):
        rep = repository.UsersRepository(url)
        res = rep.getUserFriends(3, token)
        self.assertEqual(res, None)

if __name__ == "__main__":
    unittest.main()