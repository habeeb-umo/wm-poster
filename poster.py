import requests
import json
import os
from os import listdir
from os.path import isfile, join
from requests.auth import HTTPBasicAuth

url = os.environ['POST_URL']
json_path = '/app/json-dir/'
headers = {
    'Content-type': os.environ['CONTENT_TYPE_HEADER'],
    'Accept': os.environ['ACCEPT_HEADER'],
    'aw-tenant-code': os.environ['TENANT_CODE_HEADER']
}
auth_user = os.environ['AUTH_USER']
auth_pass = os.environ['AUTH_PASSWORD']

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

def post_request(filenames, group_ids):
    for i in range(len(filenames)):
        with open(json_path + filenames[i]) as f:
            file_data = json.load(f)
            for json_obj in file_data:
                url_with_id = url + '/' + group_ids[i]
                x = requests.post(url_with_id, data=json.dumps(json_obj), headers=headers, auth=HTTPBasicAuth(auth_user, auth_pass))

                if x.ok
                    print("POST complete with status code " + str(x.status_code) + " for object: " + json_obj.get("Name"))
                else:
                    print("POST failed with status code " + str(x.status_code) + " for object: " + json_obj.get("Name"))

if __name__ == "__main__":
    filenames = get_filenames()
    group_ids = get_ids(filenames)
    post_request(filenames, group_ids)