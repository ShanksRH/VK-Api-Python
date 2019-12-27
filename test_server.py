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
        

if __name__ == "__main__":
    
    unittest.main()
