import requests
import unittest

class TestPythonRepos(unittest.TestCase):
    def setUp(self):
        self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.headers = {'Accept': 'application/vnd.github.v3+json'}

    def test_api_call(self):
        r = requests.get(self.url, headers=self.headers)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()