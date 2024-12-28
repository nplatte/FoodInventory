from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from Orders.models import Order
from Orders.forms import OrderForm
from django.urls import reverse

class TestFileUpload(TestCase):

    def setUp(self):
        self.url = reverse("add_order")
        self.good_file = SimpleUploadedFile("Orders/tests/invoice.pdf", b'Simple content', content_type='application/pdf')
        self.bad_file = SimpleUploadedFile("Orders/tests/invoice.txt", b'Simple content', content_type='text/plain')

    def tearDown(self):
        return super().tearDown()
    
    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_good_POST_returns_201(self):
        response = self.client.post(self.url, {"new_file": self.good_file})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recent']), 1)
        self.assertIn('invoice.pdf', response.context["recent"])

    def test_bad_POST_returns_400(self):
        response = self.client.post(self.url, {"new_file": self.bad_file})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recent']), 0)

    def test_correct_form_used(self):
        get = self.client.get(self.url)
        post = self.client.post(self.url, {"new_file": self.good_file})
        self.assertIsInstance(get.context['form'], OrderForm)
        self.assertIsInstance(post.context['form'], OrderForm)

    def test_form_submission_makes_new_order(self):
        old_count = Order.objects.count()
        self.client.post(self.url, {"new_file": self.good_file})
        new_count = Order.objects.count()
        self.assertGreater(new_count, old_count)

class TestViewAllOrders(TestCase):

    def setUp(self):
        url = reverse('view_orders')
        self.o = Order.objects.create()
        self.response = self.client.get(url)

    def tearDown(self):
        return super().tearDown()
    
    def test_GET_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_GET_sends_orders(self):
        self.assertIn(self.o, self.response.context['orders'])