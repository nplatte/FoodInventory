from django.test import TestCase

class TestFileUpload(TestCase):

    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_user_can_upload_pdf_file(self):
        pass

    def test_user_cannot_upload_non_pdf_file(self):
        pass