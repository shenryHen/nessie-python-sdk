import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.client import Client

class TestAtmRequests(unittest.TestCase):
    
    def setUp(self):
        # implicitly get NESSIE_API_KEY from env
        self.client = Client()
        
    def test_get_atms(self):
        lat = 38.9283
        lng = -77.1753
        rad = 1
        
        observed_atms = self.client.atm.get_atms(lat,lng,rad)
        print(observed_atms)
        self.assertEqual(1,0)
        
        expected_firsttwo_atms = [
        {
          "_id": "56c66be5a73e492741506f4b",
          "name": "McLean 1",
          "geocode": {
            "lng": -77.17829449999999,
            "lat": 38.932887
          },
          "accessibility": 'true',
          "hours": [
            "24 hours a day, 7 days a week"
          ],
          "address": {
            "state": "VA",
            "zip": "22101",
            "city": "McLean",
            "street_name": "Chain Bridge Road",
            "street_number": "1439"
          },
          "language_list": [
            "English"
          ],
          "amount_left": 273775
        },
        {
          "_id": "56c66be5a73e492741506f4c",
          "name": "McLean 2",
          "geocode": {
            "lng": -77.17829449999999,
            "lat": 38.932887
          },
          "accessibility": 'false',
          "hours": [
            "24 hours a day, 7 days a week"
          ],
          "address": {
            "state": "VA",
            "zip": "22101",
            "city": "McLean",
            "street_name": "Chain Bridge Road",
            "street_number": "1439"
          },
          "language_list": [
            "Portuguese",
            "Korean",
            "Spanish",
            "Chinese",
            "French",
            "English"
          ],
          "amount_left": 444425
        }]