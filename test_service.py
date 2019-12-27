import unittest
import json
import service
import repository
import mocrepository

url = 'http://magic.troll.me/'
token = 'abrakadabra'

class TestService(unittest.TestCase):
    def test_find_group_mocrep(self):
        urep = mocrepository.MocUsersRepository(url)
        grep = mocrepository.MocGroupsRepository(url)
        self.assertNotEqual(urep, None)
        self.assertNotEqual(grep, None)
        svc = service.Service(urep, grep)
        res = svc.find_the_most_popular_friends_group(0, token)
        self.assertEqual(res, [{'id' : 133, 'name' : 'Best Group EVER'}])

if __name__ == "__main__":
    unittest.main()