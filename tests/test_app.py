import unittest
from server.app import app

class FlaskTestCase(unittest.TestCase):

    def test_status_count(self):
        tester = app.test_client(self)
        response = tester.get('/status_count?start=2023-01-01T00:00:00&end=2023-01-01T23:59:59')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)

if __name__ == '__main__':
    unittest.main()
