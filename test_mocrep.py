import unittest
import json
import mocrepository

url = 'http://magic.troll.me/'
token = 'abrakadabra'

class TestRepositories(unittest.TestCase):
    def test_users_repository(self):
        rep = mocrepository.MocUsersRepository(url)
        self.assertNotEqual(rep, None)
    
    def test_groups_repository(self):
        rep = mocrepository.MocGroupsRepository(url)
        self.assertNotEqual(rep, None)
    
    def test_get_friends(self):
        rep = mocrepository.MocUsersRepository(url)
        res = rep.getUserFriends(0, token)
        self.assertEqual(res, [2, 3, 10])
    
    def test_get_friends_1(self):
        rep = mocrepository.MocUsersRepository(url)
        res = rep.getUserFriends(1, token)
        self.assertEqual(res, None)
    
    def test_get_groups(self):
        rep = mocrepository.MocUsersRepository(url)
        res = rep.getUserGroups(1, token)
        self.assertEqual(res, None)
    
    def test_get_groups_1(self):
        rep = mocrepository.MocUsersRepository(url)
        res = rep.getUserGroups(0, token)
        self.assertEqual(res, [101, 102, 103])
    
    def test_get_group_info(self):
        rep = mocrepository.MocGroupsRepository(url)
        res = rep.getGroup(133, token)
        self.assertEqual(res, [{'id' : 133, 'name' : 'Best Group EVER'}])
    
    def test_get_group_info_none(self):
        rep = mocrepository.MocGroupsRepository(url)
        res = rep.getGroup(132, token)
        self.assertEqual(res, None)

if __name__ == "__main__":
    unittest.main()