from django.test import TestCase

class TestFileUpload(TestCase):

    def setUp(self):
        self.url = "/file/add/"

    def tearDown(self):
        return super().tearDown()
    
    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_good_POST_returns_201(self):
        f = open("FileUpload/tests/invoice.pdf", "r")
        response = self.client.post(self.url, {"file": f})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.context), 1)
        self.assertIn(response.context["recent"], "invoice.pdf")

    def test_bad_POST_returns_401(self):
        f = open("FileUpload/tests/bad.txt", "r")
        response = self.client.post(self.url, {"file": f})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(len(response.context), 0)