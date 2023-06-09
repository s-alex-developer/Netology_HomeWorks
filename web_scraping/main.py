import bs4
import pandas
import requests
from tqdm import tqdm
from fake_headers import Headers

import json
from time import sleep
from pprint import pprint

headers = Headers(browser='firefox', os='win')
headers_data = headers.generate()

all_vacancy = []

for p in tqdm(range(9)):

    sleep(0.1)

    url = f'https://spb.hh.ru/search/vacancy?text=python+and+Django+and+Flask&salary=&area=2&area=1&no_magic=true&ored_clusters=true&items_on_page=20&excluded_text=&page={p}'

    response = requests.get(url, headers=headers_data)

    html_data = bs4.BeautifulSoup(response.text, 'lxml')

    for vacancy in html_data.findAll('div', class_="vacancy-serp-item-body__main-info"):

        vacancy_name = vacancy.find('a', class_="serp-item__title").text.strip()

        vacancy_href = vacancy.find('a').get('href')

        try:

            vacancy_offer = vacancy.find('span', class_="bloko-header-section-3").text.replace('\u202f', ' ')

        except AttributeError:

            vacancy_offer = 'Зарплата не указана.'

        vacancy_company = vacancy.find('a', class_="bloko-link bloko-link_kind-tertiary").text.replace('\xa0', ' ')

        vacancy_town = vacancy.findAll('div', class_="bloko-text")[-1].text.split(',')[0]

        all_vacancy.append([vacancy_name, vacancy_href, vacancy_offer, vacancy_company, vacancy_town])

all_vacancy.pop(68)
all_vacancy.pop(70)

header = ['position', 'reference', 'offer', 'company', 'town']

with open('vacancies.json', 'w') as file:
    json.dump(all_vacancy, file, ensure_ascii=False, indent=2)

df = pandas.DataFrame(all_vacancy, columns=header)
df.to_csv('vacancies.csv', sep=',', encoding='utf8')