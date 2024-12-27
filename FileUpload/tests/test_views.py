from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from FileUpload.forms import FileForm
from Orders.models import Order

class TestFileUpload(TestCase):

    def setUp(self):
        self.url = "/files/add/"
        self.good_file = SimpleUploadedFile("FileUpload/tests/invoice.pdf", b'Simple content', content_type='application/pdf')
        self.bad_file = SimpleUploadedFile("FileUpload/tests/invoice.txt", b'Simple content', content_type='text/plain')

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
        self.assertIsInstance(get.context['form'], FileForm)
        self.assertIsInstance(post.context['form'], FileForm)

    def test_form_submission_makes_new_order(self):
        old_count = Order.objects.count()
        self.client.post(self.url, {"new_file": self.good_file})
        new_count = Order.objects.count()
        self.assertGreater(new_count, old_count)
        

