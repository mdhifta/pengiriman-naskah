from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .class_forms import FileUplod

def index(request):
    form = FileUplod()
    # context = {}
    # if request.method == 'POST':
    #     uploaded_file = request.FILES['datafile']
    #     fs = FileSystemStorage()
    #     name = fs.save(uploaded_file.name,uploaded_file)
    #     context['url'] = fs.url(name)
    return render(request, 'index.html',{
        'form': form
    } )

def list_file(request):
    return render(request, 'admin_data.html')
