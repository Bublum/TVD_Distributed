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

    files = ["/home/shibashis/Downloads/tensorflow-1.13.1-cp35-cp35m-manylinux1_x86_64.whl",
             "/home/shibashis/Downloads/six-1.12.0-py2.py3-none-any.whl",
             "/home/shibashis/Downloads/numpy-1.16.4-cp35-cp35m-manylinux1_x86_64.whl",
             "/home/shibashis/Downloads/wheel-0.33.4-py2.py3-none-any.whl",
             "/home/shibashis/Downloads/setuptools-41.0.1-py2.py3-none-any.whl",
             "/home/shibashis/Downloads/mock-3.0.5-py2.py3-none-any.whl",
             "/home/shibashis/Downloads/Keras_Applications-1.0.7-py2.py3-none-any.whl",
             "/home/shibashis/Downloads/Keras_Preprocessing-1.0.9-py2.py3-none-any.whl",
             "/home/shibashis/VirtualEnv/TVD_Distributed/requirements.txt"]
    for file in files:
        fdir, fname = os.path.split(file)
        zipf.write(file, fname)
    zipf.close()

    return HttpResponse(MEDIA_URL + filename)


#
def zip(request):
    return HttpResponse(MEDIA_URL + 'requirements.zip')
