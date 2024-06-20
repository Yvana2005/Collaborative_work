from django.shortcuts import render
from .models import File
from uuid import uuid4

def file(request):
    if request.method == 'POST':
        userfile = request.POST.get('userfile')
        if userfile:
            id = uuid.uuid4()
            file = File(id=id, file=userfile )
            file.save()
            link = "http://127.0.0.1:8000/"+str(id)+"/"
            print(link)
            return render(request, 'fileshare/file.html', {"link":link})
    return render(request, 'fileshare/file.html')

def downloadFile(request, id):
    print(id)
    get_file = File.objects.get(id=id)
    return render(request, 'fileshare/downloadfile.html', {"get_file":get_file})

# Create your views here.
