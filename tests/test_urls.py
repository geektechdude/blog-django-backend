from django.test import TestCase
from django.urls import reverse


class urlTest(TestCase):
    
    def setUp(self):
        pass

    def test_GraphQLURL(self):
        response = self.client.get('/graphql/')
        self.assertTrue(response.content, "Graph")