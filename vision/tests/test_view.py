from rest_framework.test import APITestCase
from rest_framework import status


class ViewAPITest(APITestCase):

    def response(self, data):
        return self.client.post('/api/v1/vision/', data)

    def test_no_request_data(self):
        response = self.response({})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_good_request(self):
        data = {
            'image': 'https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/09/dog-landing-hero-lg.jpg?bust=1536935129&width=1080'
        }

        response = self.response(data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
