from django.shortcuts import render
from .forms import FileForm
from django.http.response import HttpResponseBadRequest

def AddFileView(request):
    form = FileForm()
    context = {}
    context['form'] = form
    context['recent'] = []
    if request.method == "POST":
        filled_upload = FileForm(request.POST, request.FILES)
        context['form'] = filled_upload
        if filled_upload.is_valid():
            context['recent'].append(request.FILES['new_file'].name)
    return render(request, "file_upload.html", context)