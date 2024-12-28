from FileUpload.forms import FileForm
from .models import Order

class OrderForm(FileForm):

    def save(self):
        Order.objects.create()