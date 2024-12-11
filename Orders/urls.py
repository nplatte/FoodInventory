from django.urls import path
from .views import all_orders_page

urlpatterns = [
    path("all/", all_orders_page, name="view_orders")
]