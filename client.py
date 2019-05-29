import json
import os
import subprocess
import requests
import zipfile

from config import SERVER_IP, VIRTUAL_ENV_PATH, V_ENV, CREATE_VIRTUAL_ENV, DATA_PATH, DATA_CHUNK_SIZE, REQUIREMENTS_PATH


def download_file(url, path):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    print(local_filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        file_path = os.path.join(DATA_PATH, path, local_filename)
        print(file_path)
        counter = 1
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=DATA_CHUNK_SIZE):
                print(counter * DATA_CHUNK_SIZE / 1024)
                counter += 1
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


def request_assets_for_processing():
    file_url = requests.get(url=SERVER_IP + '/get_files/')
    url = SERVER_IP + file_url.text
    print(url)
    downloaded_file = download_file(url)

    with zipfile.ZipFile(downloaded_file, 'r') as z:
        print(z.extractall(path=PROCESSING_DIR))


def execute_file():
    dir = PROCESSING_DIR
    files = os.listdir(dir)


def send_file(files):
    for file in files:
        with open(file, 'rb') as f:
            r = requests.post(URL, files={file: f})


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

    # r = requests.get(url=url)
    # print(r.status_code)
    # response = json.loads(r.text)
    # print(response)
    # # os.system('ls')
    # c_url = SERVER_IP + response['url']
    # downloaded_file = download_file(c_url, requirements_path)
    print('Done')
    # with zipfile.ZipFile(os.path.join(DATA_PATH, REQUIREMENTS_PATH,'requirements.zip'), 'r') as z:
    #     z.extractall(path=os.path.join(DATA_PATH, REQUIREMENTS_PATH))

    file_path = os.path.join(DATA_PATH, REQUIREMENTS_PATH, 'requirements.txt')
    f = open(file_path, 'r')
    command = 'cd {0}/{1}/bin/pip;pip3 --version;'.format(VIRTUAL_ENV_PATH, V_ENV)
    # for each in f:
    #     print(each[:-1])
    #     command += 'pip3 install {0};'.format(each[:-1])
    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
    proc_stdout = process.communicate()[0].strip().decode("utf-8")
    print(proc_stdout)

if __name__ == '__main__':
    # pass
    # dependency_request()

    if CREATE_VIRTUAL_ENV:
        create_virtual_env()

    dependency_request()
