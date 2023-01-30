import requests
from bs4 import BeautifulSoup

headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,\
    application/signed-exchange;v=b3;q=0.9",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

responce = requests.get('http://www.hl7.eu/HL7v2x/v28/hl7v28tab.htm', headers=headers)

soup = BeautifulSoup(responce.text, 'lxml')

table_values = soup.find('table', class_='info')

aa_href = table_values.find_all('td', class_='table')



filename = []
all_hrefs = []

for file in range(1, len(aa_href), 5):
    filename.append(aa_href[file].text)

for href in range(0, len(aa_href), 5):
    all_hrefs.append(aa_href[href].find('a').get('href'))

for z in all_hrefs:
    with open('C:\\Users\\Stas\\Desktop\\hl7conv\\data\\hrefs.txt', 'a', encoding='utf-8') as file:
        file.write(z + '\n')
    file.close()

for z in filename:
    with open('C:\\Users\\Stas\\Desktop\\hl7conv\\data\\filenames.txt', 'a', encoding='utf-8') as file:
        file.write(z + '\n')
    file.close()

