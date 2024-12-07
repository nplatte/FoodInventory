from django.shortcuts import render
from .forms import FileForm

def AddFileView(request):
    file_upload_form = FileForm()
    if request.method == "POST":
        pass
    return render(request, "file_upload.html")