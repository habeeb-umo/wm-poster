import requests
import json
import os
from os import listdir
from os.path import isfile, join

url = os.environ['POST_URL']
json_path = os.environ['JSON_FILEPATH']
headers = {
    'Content-type': os.environ['CONTENT_TYPE_HEADER'],
    'Accept': os.environ['ACCEPT_HEADER'],
    'aw-tenant-code': os.environ['TENANT_CODE_HEADER']
}

def get_filenames():
    filenames = [
        f for f in listdir(json_path) if isfile(join(json_path, f))
    ]
    return filenames

def get_ids(filenames):
    # Parse filenames to get Group IDs
    group_ids = []
    for f in filenames:
        split_filename = f.replace('.', '-').split('-')
        group_id = split_filename[len(split_filename)-2]
        group_ids.append(group_id)
    
    return group_ids

def post_request(filenames):
    for i in range(len(filenames)):
        with open(json_path + filenames[i]) as f:
            file_data = json.load(f)
            x = requests.post(url, data=json.dumps(file_data), headers=headers)
            print(x.status_code)

if __name__ == "__main__":
    filenames = get_filenames()
    group_ids = get_ids(filenames)
    post_request(filenames)