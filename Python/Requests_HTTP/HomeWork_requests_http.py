# Задача №1
import requests

URL = 'https://akabab.github.io/superhero-api/api'

response = requests.get(f'{URL}/all.json')

my_heroes = ['Hulk', 'Captain America', 'Thanos']
most_clever_hero = {}

for hero in response.json():
    if hero['name'] in my_heroes:
        most_clever_hero[hero['name']] = hero['powerstats']['intelligence']

print(sorted(most_clever_hero)[-1])


# Задача №2
class YandexDisc:

    def __init__(self, token):
        self.token = token
        self.yandex_URL = 'https://cloud-api.yandex.net'

    # Функция формирует обязательные заголовки параметра headers
    # Данные заголовки обязательны для работы с запросами к REST API Яндекс диска.
    def get_headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
                }

    # Получить ссылку на загрузку файла на Яндекс диск:
    def get_upload_link(self, _download_path):

        _request_URL = f'{self.yandex_URL}/v1/disk/resources/upload'

        # 'overwrite': 'true' - параметр перезапишет файл если он уже есть на Яндекс диске.
        _params = {'path': _download_path, 'overwrite': 'true'}
        _headers = self.get_headers()

        _response = requests.get(_request_URL, headers=_headers, params=_params)

        return _response.json()['href']

    # Функция загрузки файла с диска компьютера на Яндекс Диск.
    def upload_file(self, _download_path, _file_path):

        # Формируем ссылку для загрузки файла:
        href = self.get_upload_link(_download_path)

        _response = requests.put(href, open(_file_path, 'rb'))

        if _response.status_code == 201:
            print('Файл успешно загружен на Яндекс диск.')


if __name__ == '__main__':
    Token = ''
    my_requests = YandexDisc(Token)

    download_path = '' # Путь загрузки и имя файла на Яндекс диске.
    file_path = r'' # Путь к файлу на компьютере, который будет загружен на Яндекс диск.

    my_requests.upload_file(download_path, file_path)
