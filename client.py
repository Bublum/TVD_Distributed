import json
import os
import subprocess
import requests
import urllib.request

URL = 'http://192.168.0.109:8000/get_files/'


from TVD_Distributed.config import SERVER_IP

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


def request_to_server():

    file_url = requests.get(url=URL)
    download_file(file_url.content.decode('utf-8'))

def execute_file(files):
    dir = ''
    for file in files:
        path = dir + '/' +  file
        code = subprocess.check_call(["python3", path + ' ' + data], stdout=subprocess.PIPE)

def send_file(files):
    for file in files:
        with open(file,'rb') as f:
            r = requests.post(URL, files={file: f})


def dependency_request():

    url = SERVER_IP + 'requirements/'

    r = requests.get(url=url)
    print(r.status_code)
    os.system('ls')


if __name__ == '__main__':
    # execute_file()
    # dependency_request()
    request_to_server()