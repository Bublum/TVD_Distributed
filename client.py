import json
import subprocess
import requests
import urllib.request

URL = 'http://192.168.0.109:8000/get_files/'


def request_to_server():
    # data = json.dumps({'type': 'free'})

    file_names = requests.get(url=URL)

    print(file_names.content.decode('utf-8'))
    # files = file_names['file_names']

    # urllib.request.urlretrieve(file_url, file_name)
    #
    # print(r)


if __name__ == '__main__':
    request_to_server()
