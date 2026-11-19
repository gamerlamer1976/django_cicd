from rest_framework.test import APITestCase

from logistic.models import Product


class TestLogisticAPI(APITestCase):
    def test_products_list(self):
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        payload = {
            'title': 'Помидор',
            'description': 'Свежий томат',
        }
        response = self.client.post(
            '/api/v1/products/',
            data=payload,
            format='json',
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)

    def test_stocks_list(self):
        response = self.client.get('/api/v1/stocks/')
        self.assertEqual(response.status_code, 200)
