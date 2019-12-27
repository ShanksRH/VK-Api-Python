import unittest
import mocserver

class TestMocServer(unittest.TestCase):
    def test_create_server(self):
        server = mocserver.MocServer()
        self.assertNotEqual(server, None)

if __name__ == "__main__":
    unittest.main()
