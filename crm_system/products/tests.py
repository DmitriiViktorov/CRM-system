from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='<PASSWORD>')
        self.group = Group.objects.create(name='Marketologists')
        self.user.groups.add(self.group)

        self.product = Product.objects.create(
            name='Test product',
            description='This is a test product',
            cost=100.00
        )

        self.client = Client()


class ProductListViewTest(ProductTestCase):
    def test_list_view(self):
        self.client.login(username='testuser', password='<PASSWORD>')
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)