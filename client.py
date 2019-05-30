import os
import shutil
import subprocess
import zipfile

import requests

from config import PROCESSING_PATH
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
    save_zip_to = os.path.join(PROCESSING_PATH, 'ZIP')
    downloaded_file = download_file(url, save_zip_to)

    with zipfile.ZipFile(os.path.join(DATA_PATH, save_zip_to, downloaded_file), 'r') as z:
        z.extractall(path=os.path.join(DATA_PATH, PROCESSING_PATH))


def execute_file():
    directory = os.path.join(DATA_PATH, PROCESSING_PATH) + '/'
    print(directory)
    code_files = []
    code_file = ''
    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, entry)):
            code_files.append(entry)
    if code_files:
        code_file = code_files[0]

    code_file_path = os.path.join(DATA_PATH, PROCESSING_PATH, code_file)
    if os.system('python3 ' + code_file_path) == 0:
        # send output.zip to server
        output_zip_path = os.path.join(DATA_PATH, PROCESSING_PATH, 'output', 'output.zip')
        with open(output_zip_path, 'r') as f:
            r = requests.post(SERVER_IP + '/from_client/', files={output_zip_path: f})

        # delete everything under client_processing and create required directories
        shutil.rmtree(os.path.join(DATA_PATH,PROCESSING_PATH))
        create_directories = os.path.join(DATA_PATH,PROCESSING_PATH,'ZIP')
        try:
            os.makedirs(create_directories)
        except OSError:
            print('Could not create path: ', create_directories)
        # request_assets_for_processing
        request_assets_for_processing()
    else:
        data = {'type' : 'error',
                'error_message' : 'Null'}
        response = requests.get(SERVER_IP + '/error/',params=data)
        print(response)
        print('Code has errors')


def send_file(files):
    for file in files:
        with open(file, 'rb') as f:
            r = requests.post(SERVER_IP + '/' + '', files={file: f})


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
    pip_command = '{0}/{1}/bin/pip install '.format(VIRTUAL_ENV_PATH, V_ENV)
    # command = '{0}/{1}/bin/pip install'.format(VIRTUAL_ENV_PATH, V_ENV)
    command = ''
    for each in f:
        print(each[:-1])
        command = pip_command + os.path.join(DATA_PATH, REQUIREMENTS_PATH, each[:-1])
        print(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        # for line in iter(process.stdout.readline, b''):  # replace '' with b'' for Python 3
        #     print(line.decode('utf-8'))
        #     if line.decode('utf-8').lower().__contains__('would'):
        #         print('contains')
        #         process.stdin.write(str.encode('y\n'))
        proc_stdout = process.communicate()[0].strip().decode("utf-8")
        print(proc_stdout)
    print(command)


if __name__ == '__main__':
    # pass
    # dependency_request()

    if CREATE_VIRTUAL_ENV:
        create_virtual_env()

    # dependency_request()

    request_assets_for_processing()
    # execute_file()
