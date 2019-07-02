from django.shortcuts import render, redirect
from shareimg.models import SharedImage
from django.core.files.uploadedfile import SimpleUploadedFile

def index(request):
    images = SharedImage.objects.all()
    return render(request, 'index.html', {'images':images})


def handle_upload(request):
    new_shareimg = SharedImage()
    new_shareimg.image = request.FILES['fileupload']
    new_shareimg.title = request.POST['title']
    new_shareimg.description = request.POST['description']
    new_shareimg.save()
    return redirect('main')
