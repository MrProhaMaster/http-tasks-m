import os
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_link(self, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": filename, "overwrite": "false"}
        link = requests.get(upload_url, headers=headers, params=params)
        return link.json()['href']

    def upload(self, file_path):
        for file in os.listdir(file_path):
            url = self._get_upload_link(file)
            response = requests.put(url, data=open(f'{file_path}/{file}', 'rb'))
        print('Done')

if __name__ == '__main__':
    path_to_file = 'file'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)