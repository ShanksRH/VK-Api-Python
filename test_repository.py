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
        res = rep.getUserFriends(0, token)
        self.assertEqual(res, [2, 3, 14])
    
    def test_get_friends_2(self):
        rep = repository.UsersRepository(url)
        res = rep.getUserFriends(2, token)
        self.assertEqual(res, [10, 12, 13, 46])
    
    def test_get_friends_3(self):
        rep = repository.UsersRepository(url)
        res = rep.getUserFriends(1, token)
        self.assertEqual(res, None)
    
    def test_get_groups(self):
        rep = repository.UsersRepository(url)
        res = rep.getUserGroups(1, token)
        self.assertEqual(res, None)
    
    def test_get_groups_1(self):
        rep = repository.UsersRepository(url)
        res = rep.getUserGroups(0, token)
        self.assertEqual(res, [101, 102, 103])

if __name__ == "__main__":
    unittest.main()