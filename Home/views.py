import os
import zipfile

import io
from django.http import HttpResponse

from django.shortcuts import render

from TVD_Distributed.settings import MEDIA_ROOT, MEDIA_URL


def requirements(request):

    # zip_subdir = "/home/shibashis/Videos/something"
    # zip_filename = zip_subdir + ".zip"
    #
    # s = io.BytesIO()
    #
    # zf = zipfile.ZipFile(s, "w")
    #
    # for fpath in filenames:
    #     # Calculate path for file in zip
    #     fdir, fname = os.path.split(fpath)
    #     zip_path = os.path.join(zip_subdir, fname)
    #
    #     # Add file, at correct path
    #     print(fpath)
    #     zf.write(fpath, zip_path)
    #
    # # Must close zip for all contents to be written
    # zf.close()

    filename = 'requirements.zip'
    zipf = zipfile.ZipFile(os.path.join(MEDIA_ROOT, filename), 'w', zipfile.ZIP_DEFLATED)
    path = '/home/shibashis/DMW/'

    files = ["/home/shibashis/decryptor.py", "/home/shibashis/LED.html"]
    for file in files:
        fdir, fname = os.path.split(file)
        zipf.write(file, fname)
    zipf.close()

    return HttpResponse(MEDIA_URL + filename)

#
def zip(request):
    return HttpResponse(MEDIA_URL + 'requirements.zip')
