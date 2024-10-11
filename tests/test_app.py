import unittest
from app import app

class TestApp(unittest.TestCase):
    # Test the home route
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the E-commerce Store', response.data)

if __name__ == '__main__':
    unittest.main()
