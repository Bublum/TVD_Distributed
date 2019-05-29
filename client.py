import json
import os
import re
import subprocess
import requests
import zipfile


from TVD_Distributed.config import SERVER_IP

PROCESSING_DIR = 'client_processing/'

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


def request_assets_for_processing():

    file_url = requests.get(url=SERVER_IP + '/get_files/')
    url = SERVER_IP +  file_url.text
    print(url)
    downloaded_file = download_file(url)

    with zipfile.ZipFile(downloaded_file, 'r') as z:
        print(z.extractall(path=PROCESSING_DIR))


def execute_file():
    dir = PROCESSING_DIR
    files = os.listdir(dir)



def send_file(files):
    for file in files:
        with open(file,'rb') as f:
            r = requests.post(URL, files={file: f})


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
    # pass
    # dependency_request()

    # execute_file()
    # dependency_request()
    request_assets_for_processing()
    execute_file()