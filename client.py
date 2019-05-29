import json
import subprocess
import requests

def request_to_server():
    URL = "http://maps.googleapis.com/maps/api/geocode/json"

    data = json.dumps({'type': 'request_file'})

    r = requests.post(url=URL, data=data)

    print(r)



if __name__ == '__main__':
    pass