from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

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
        response = self.client.post(self.url, {"file": f})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.context), 1)
        self.assertIn(response.context["recent"], "invoice.pdf")

    def test_bad_POST_returns_401(self):
        f = SimpleUploadedFile("FileUpload/tests/invoice.txt", b'Simple content', content_type='text/plain')
        response = self.client.post(self.url, {"file": f})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(len(response.context), 0)