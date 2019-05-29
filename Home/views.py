import os
import zipfile

from django.http import HttpResponse

import json

from Home.models import Progress
from TVD_Distributed.settings import MEDIA_ROOT, MEDIA_URL


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def requirements(request):
    client_ip = get_client_ip(request)
    progress_obj = Progress.objects.get_or_create(ip=client_ip)
    progress_obj.status = 0
    progress_obj.save()

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
    response = {
        'url': MEDIA_URL + filename,
        'file': 'requirements.txt'
    }
    return HttpResponse(json.dumps(response))


def get_files(request):
    if request.method == 'GET':
        folder_path_to_send = MEDIA_ROOT + '/to_send/helmet/'
        filename = 'get_files.zip'
        zipf = zipfile.ZipFile(os.path.join(MEDIA_ROOT, filename), 'w', zipfile.ZIP_DEFLATED)
        files = os.listdir(folder_path_to_send)

        for file in files:
            zipf.write(os.path.join(folder_path_to_send, file), file)

        zipf.close()

        return HttpResponse(MEDIA_URL + filename)


def get_status(request):
    result = {}
    for each in Progress.objects.all():
        result['uid'] = each.ip
        result['status'] = 'done' if each.status_type == 2 else result[
            'status'] = 'processing' if each.status_type == 1 else result['status'] = 'No'
    return HttpResponse(json.dumps(result))
        # // var
    # result = "[{\"uid\": 1, \"status\": \"done\"},\
    #                    //             {\"uid\": 2, \"status\": \"done\"},\
    #                    //             {\"uid\": 4, \"status\": \"processing\"},\
    #                    //             {\"uid\": 5, \"status\": \"No\"},\n\
    #                    //             {\"uid\": 6, \"status\": \"done\"},\n                        \
    #                    //             {\"uid\": 7, \"status\": \"processing\"},\n\
    #                    //             {\"uid\": 8, \"status\": \"No\"},\n\
    #                    //             {\"uid\": 9, \"status\": \"done\"},\n \
    #                    //             {\"uid\": 10, \"status\": \"processing\"}]";

