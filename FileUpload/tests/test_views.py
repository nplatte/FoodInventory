from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from FileUpload.forms import FileForm

class TestFileUpload(TestCase):

    def setUp(self):
        self.url = "/files/add/"

    def tearDown(self):
        return super().tearDown()
    
    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_good_POST_returns_201(self):
        f = SimpleUploadedFile("FileUpload/tests/invoice.pdf", b'Simple content', content_type='application/pdf')
        response = self.client.post(self.url, {"new_file": f})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recent']), 1)
        self.assertIn('invoice.pdf', response.context["recent"])

    def test_bad_POST_returns_400(self):
        f = SimpleUploadedFile("FileUpload/tests/invoice.txt", b'Simple content', content_type='text/plain')
        response = self.client.post(self.url, {"new_file": f})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recent']), 0)

    def test_correct_form_used(self):
        get = self.client.get(self.url)
        f = SimpleUploadedFile("FileUpload/tests/invoice.pdf", b'Simple content', content_type='application/pdf')
        post = self.client.post(self.url, {"new_file": f})
        self.assertIsInstance(get.context['form'], FileForm)
        self.assertIsInstance(post.context['form'], FileForm)