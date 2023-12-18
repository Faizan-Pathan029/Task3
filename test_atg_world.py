import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):

    def test_website_access(self):
        url = "https://atg.world/"

        try:
    
            response = requests.get(url)
            
         
            self.assertEqual(response.status_code, 200, "Failed to access {}. Status code: {}".format(url, response.status_code))

         

        except requests.RequestException as e:
            # If an exception occurs during the request (e.g., connection error), mark the test as failed
            self.fail("Failed to access {}. Exception: {}".format(url, e))

if __name__ == '__main__':
    unittest.main()
