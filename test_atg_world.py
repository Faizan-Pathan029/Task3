import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):

    def test_website_access(self):
        url = "https://atgsdgdasgsggsafa4w6634ld"

        try:
            # Attempt to connect to the website
            response = requests.get(url)
            
            # Check if the status code is 200 (OK)
            self.assertEqual(response.status_code, 200, "Failed to access {}. Status code: {}".format(url, response.status_code))

            # Additional checks can be added if necessary, such as checking for specific content on the page

        except requests.RequestException as e:
            # If an exception occurs during the request (e.g., connection error), mark the test as failed
            self.fail("Failed to access {}. Exception: {}".format(url, e))

if __name__ == '__main__':
    unittest.main()
