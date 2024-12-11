from django.shortcuts import render

def all_orders_page(request):
    return render(request, 'Orders/all.html')