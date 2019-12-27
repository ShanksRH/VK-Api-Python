import unittest
import requests
import time
import json

url = 'http://magic.troll.me/'

class TestMocHandler(unittest.TestCase):
    def test_doget_check_ping(self):
        response = requests.get(url + 'ping')
        try:
            js = json.loads(response.text)
            self.assertEqual(js['ping'], 'ok')
        except:
            self.assertTrue(False)
    
    def test_doget_if_not_method(self):
        response = requests.get(url + 'mothod/get.friends?user_id=0&v=5.61')
        try:
            js = json.loads(response.text)
            self.assertEqual(js['error']['error_msg'], 'should use method')
        except:
            self.assertTrue(False)
    
    def test_doget_if_unknown_method(self):
        response = requests.get(url + 'method/get.friunds?user_id=0&v=5.61')
        try:
            js = json.loads(response.text)
            self.assertEqual(js['error']['error_msg'], 'unknown method')
        except:
            self.assertTrue(False)
    
    def test_doget_if_wrong_que_sign(self):
        response = requests.get(url + 'method/friends.get?ok?user_id=0&v=5.61')
        try:
            js = json.loads(response.text)
            self.assertEqual(js['error']['error_msg'], 'incorrect number of "?"')
        except:
            self.assertTrue(False)
    
    def test_doget_if_wrond_eq_sigh(self):
        response = requests.get(url + 'method/friends.get?user_id=0=1&v=5.61')
        try:
            js = json.loads(response.text)
            self.assertEqual(js['error']['error_msg'], 'incorrect number of "=" in user_id=0=1')
        except:
            self.assertTrue(False)
    
    def test_doget_if_no_token(self):
        response = requests.get(url + 'method/friends.get?user_id=0&v=5.61')
        try:
            js = json.loads(response.text)
            self.assertEqual(js['error']['error_msg'], 'invalid access token argument')
        except:
            self.assertTrue(False)

if __name__ == "__main__":
    
    unittest.main()
