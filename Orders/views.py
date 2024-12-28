from django.shortcuts import render
from .forms import OrderForm
from .models import Order

def all_orders_page(request):
    context = {}
    context['orders'] = Order.objects.all()
    return render(request, 'Orders/all.html', context)

def add_order_page(request):
    form = OrderForm()
    context = {}
    context['form'] = form
    context['recent'] = []
    if request.method == "POST":
        filled_upload = OrderForm(request.POST, request.FILES)
        context['form'] = filled_upload
        if filled_upload.is_valid():
            filled_upload.save()
            context['recent'].append(request.FILES['new_file'].name)
    return render(request, "Orders/add.html", context)