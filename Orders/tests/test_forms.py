from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from Orders.forms import OrderForm
from Orders.models import Order

class TestFileUpload(TestCase):

    def setUp(self):
        self.form = OrderForm
        self.good_file = SimpleUploadedFile("FileUpload/tests/invoice.pdf", b'Simple content', content_type='application/pdf')
        self.bad_file = SimpleUploadedFile("FileUpload/tests/invoice.txt", b'Simple content', content_type='text/plain')

    def test_form_attributes(self):
        f = self.form()
        self.assertIn('"pdf_upload"', f.as_p())

    def test_save_makes_new_order(self):
        old_count = Order.objects.count()
        f = self.form(data={}, files={"new_file": self.good_file})
        self.assertTrue(f.is_valid())
        f.save()
        new_count = Order.objects.count()
        self.assertLess(old_count, new_count)
    