from django.urls import path
from .views import all_orders_page, add_order_page

urlpatterns = [
    path("all/", all_orders_page, name="view_orders"),
    path("add/", add_order_page, name="add_order")
]