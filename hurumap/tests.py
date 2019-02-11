import requests

from django.test import TestCase


class MapitIntegration(TestCase):
    def test_get_kenya_country_geo(self):
        resp = requests.get('https://mapit.hurumap.org/areas/COUNTRY?generation=1&country=KE')

        self.assertEqual(resp.status_code, 200)
        # country should return only 1 item in nested dict
        response_data = resp.json().values()[0]
        self.assertEqual(response_data.get('name'), 'Kenya')
        self.assertEqual(response_data.get('type'), 'COUNTRY')

    def test_number_of_counties_in_kenya(self):
        resp = requests.get('https://mapit.hurumap.org/areas/COUNTY?generation=1&country=KE')
        self.assertEqual(resp.status_code, 200)
        response_data = resp.json()
        self.assertEqual(len(response_data), 47)






