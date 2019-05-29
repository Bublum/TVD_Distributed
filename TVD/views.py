import os

from django.http import HttpResponse

# Create your views here.
from TVD_Distributed.settings import MEDIA_ROOT


def requirements(request):
    return None


def get_files(request):
    if request.method == 'GET':
        files_to_send_dir = os.listdir(MEDIA_ROOT + '/to_send/')

        print(files_to_send_dir)
    return HttpResponse(files_to_send_dir)
