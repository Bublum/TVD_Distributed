import json
import os
import subprocess
import requests

from TVD_Distributed.config import SERVER_IP, VIRTUAL_ENV


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    print(local_filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


def request_to_server():
    url = "http://maps.googleapis.com/maps/api/geocode/json"

    data = json.dumps({'type': 'request_file'})

    r = requests.post(url=url, data=data)

    print(r)


def create_virtual_env():
    # os.system('mkdir ' + VIRTUAL_ENV)
    os.system('cd')


def dependency_request():
    url = SERVER_IP + '/requirements/'

    r = requests.get(url=url)
    print(r.status_code)
    print(r.text)
    os.system('ls')
    c_url = SERVER_IP + r.text
    file_name = download_file(c_url)
    print(file_name)


if __name__ == '__main__':
    pass
    dependency_request()
