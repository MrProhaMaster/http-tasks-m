import os
from yadisk import YaDisk as Y

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        files = []
        for file in  os.listdir(file_path):
            files.append(file)
        disk = Y(token=self.token)
        for i in files:
            disk.upload(file_path+'/'+i, i)
        print('Finished')
        
if __name__ == '__main__':
    path_to_file = 'file'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)