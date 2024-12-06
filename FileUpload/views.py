from django.shortcuts import render

def AddFileView(request):
    return render(request, "file_upload.html")