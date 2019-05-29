import json
import subprocess
import requests

from TVD_Distributed.config import SERVER_IP


def request_to_server():
    URL = "http://maps.googleapis.com/maps/api/geocode/json"

    data = json.dumps({'type': 'request_file'})

    r = requests.post(url=URL, data=data)

    print(r)


def dependency_request():

    url = SERVER_IP + 'requirements/'


if __name__ == '__main__':
    pass
