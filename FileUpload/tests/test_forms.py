from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from FileUpload.forms import FileForm

class TestFileUpload(TestCase):

    def setUp(self):
        self.form = FileForm

    def tearDown(self):
        return super().tearDown()

    def test_form_accepts_pdf_files(self):
        test_file = SimpleUploadedFile("FileUpload/tests/invoice.pdf", b'Simple content', content_type='application/pdf')
        f = self.form(data={}, files={"new_file":test_file})
        self.assertTrue(f.is_valid())

    def test_form_denies_non_pdf_files(self):
        test_file = SimpleUploadedFile("FileUpload/tests/invoice.txt", b'Simple content', content_type='text/plain')
        f = self.form(data={}, files={"new_file":test_file})
        self.assertFalse(f.is_valid())