import requests
import json
token = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests(file_url, headers=headers, params=params).json()
        href = response.get('href', '')
        res = requests.put(href, data=open(file_path, 'r'))
        if res == 201:
          return 'OK'
        else:
          return f'Ошибка! Код ошибки: {res.status_code}'

if __name__ == '__main__':
    path_to_file = 'file.txt'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
