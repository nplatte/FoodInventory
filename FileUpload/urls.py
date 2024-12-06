from django.urls import path
from .views import AddFileView

urlpatterns = [
    path("add/", AddFileView, name="add_file")
]