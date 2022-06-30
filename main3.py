# Задача 1

import requests

def heroes_intelligence(url, heroes_list: list):
    response = requests.get(url).json()
    best_hero = ''
    best_brain = 0
    for name in heroes_list:
        for item in response:
            if name == item['name'] and best_brain < item['powerstats']['intelligence']:
                best_hero = item['name']
    return f'Самый умный среди героев - это {best_hero}'

if __name__ == '__main__':
    url = "https://akabab.github.io/superhero-api/api/all.json"
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    print(heroes_intelligence(url, heroes_list))

# Задача 2

import requests
import pathlib

class YaUploader:
    token = ''
    def __init__(self, file_path):
        self.file_path = file_path
    def upload(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': 'disk:/Загрузки/Netology/' + self.file_path.name,
                  'overwrite': 'true'}
        upload_link = requests.get(upload_url, headers=headers, params=params).json()['href']
        response = requests.put(upload_link, data=open(self.file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Файл успешно загружен на Яндекс.Диск'
        return 'Ошибка загрузки файла'

if __name__ == "__main__":
    uploader = YaUploader(pathlib.Path('C:\Howework 1', 'test.txt'))
    print(uploader.upload())