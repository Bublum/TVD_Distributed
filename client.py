import json
import os
import subprocess
import requests

from TVD_Distributed.config import SERVER_IP, VIRTUAL_ENV_PATH, V_ENV, CREATE_VIRTUAL_ENV, DATA_PATH, DATA_CHUNK_SIZE


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    print(local_filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        file_path = os.path.join(DATA_PATH, local_filename)
        print(file_path)
        counter = 1
        with open(os.path.join(DATA_PATH, local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=DATA_CHUNK_SIZE):
                print(counter*81920/1024)
                counter+=1
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
    cd_command = 'cd ' + VIRTUAL_ENV_PATH + ';pwd;'
    create_command = 'virtualenv -p python3 {0};'.format(V_ENV)

    activate_command = 'source {0}/bin/activate;'.format(V_ENV)

    command = cd_command + create_command + activate_command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip().decode("utf-8")
    print(proc_stdout)


def dependency_request():
    url = SERVER_IP + '/requirements/'

    r = requests.get(url=url)
    print(r.status_code)
    response = json.loads(r.text)
    print(response)
    # os.system('ls')
    c_url = SERVER_IP + response['url']
    file_name = download_file(c_url)
    print('Done')


if __name__ == '__main__':

    if CREATE_VIRTUAL_ENV:
        create_virtual_env()

    dependency_request()
