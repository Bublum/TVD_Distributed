import os
import zipfile

import io
from django.http import HttpResponse

from django.shortcuts import render

from TVD_Distributed.settings import MEDIA_ROOT, MEDIA_URL


def requirements(request):

    filename = 'requirements.zip'
    zipf = zipfile.ZipFile(os.path.join(MEDIA_ROOT, filename), 'w', zipfile.ZIP_DEFLATED)
    path = '/home/shibashis/DMW/'

    files = ["/home/shibashis/decryptor.py", "/home/shibashis/LED.html"]
    for file in files:
        fdir, fname = os.path.split(file)
        zipf.write(file, fname)
    zipf.close()
    response = {
        'url' : (MEDIA_URL + filename),
        'file' : 'requirements.txt'
    }
    return HttpResponse(response)

#
def zip(request):
    return HttpResponse(MEDIA_URL + 'requirements.zip')
