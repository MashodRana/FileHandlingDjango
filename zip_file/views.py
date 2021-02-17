import os
import zipfile
import filetype

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseServerError


# Create your views here.

def upload_zip(request):

    if request.method=='POST':
        try:
            # FILES dict not contain 'zip_file' key
            if not request.FILES['zip_file']:
                return render(request, 'upload_zip.html', context={'msg':'Cant not process this request'})
            
            # Check the file format
            if not filetype.guess(request.FILES['zip_file']).mime=='application/zip':
                return render(request, 'upload_zip.html', context={"msg":'bad file format'})
            
            file = zipfile.ZipFile(request.FILES['zip_file'])
            file.extractall(settings.MEDIA_ROOT)

            return render(request, 'upload_zip.html', context={"done":True, "msg": "File uploading has successfully done."} )
        except  Exception as e:
            return HttpResponseServerError("Unkown file type")
    else:
        return render(request, 'upload_zip.html')
    
        

    