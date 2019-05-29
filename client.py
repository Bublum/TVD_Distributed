import json
import os
import subprocess
import requests

from TVD_Distributed.config import SERVER_IP

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


def request_to_server():
    url = "http://maps.googleapis.com/maps/api/geocode/json"

    data = json.dumps({'type': 'request_file'})

    r = requests.post(url=url, data=data)

    print(r)


def dependency_request():

    url = SERVER_IP + 'requirements/'

    r = requests.post(url=url)

    os.system('ls')


if __name__ == '__main__':
    pass
    dependency_request()