from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from Orders.forms import OrderForm
from Orders.models import Order

class TestFileUpload(TestCase):

    def setUp(self):
        self.good_file = SimpleUploadedFile("FileUpload/tests/invoice.pdf", b'Simple content', content_type='application/pdf')
        self.bad_file = SimpleUploadedFile("FileUpload/tests/invoice.txt", b'Simple content', content_type='text/plain')

    def _save_new_form(self, file):
        f = OrderForm(data={}, files={"new_file": file})
        self.assertTrue(f.is_valid())
        f.save()
        return f

    def test_form_attributes(self):
        f = self._save_new_form(self.good_file)
        self.assertIn('"pdf_upload"', f.as_p())

    def test_save_makes_new_order(self):
        old_count = Order.objects.count()
        self._save_new_form(self.good_file)
        new_count = Order.objects.count()
        self.assertLess(old_count, new_count)

    def test_save_pulls_order_data_from_pdf(self):
        self._save_new_form(self.good_file)
        order = Order.objects.all()[1]
        o_id = 592096481
        self.assertEqual(order.date_ordered, "11/24/2024")
        self.assertEqual(order.order_id, o_id)
    