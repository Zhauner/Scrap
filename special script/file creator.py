import requests
from bs4 import BeautifulSoup

headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,\
    application/signed-exchange;v=b3;q=0.9",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",

}

url = 'http://www.hl7.eu/HL7v2x/v28/'
filename_len = open('../data/filenames.txt', 'r').readlines()
all_urls = open('../data/hrefs.txt', 'r').readlines()
filename_len_without_n = [x.replace('\n', '').replace("'", ' ').replace('/', '-').replace(',', ' ').replace('\t', '') for x in filename_len]
filename_for_class = [x.replace('\n', '').replace("'", ' ').replace('/', '-').replace(',', ' ')\
                          .replace('\t', '').replace(' ', '').replace('-', '_') for x in filename_len]


count = 1

for all in range(len(filename_len)):

    responce = requests.get(url + all_urls[all], headers=headers)

    soup = BeautifulSoup(responce.text, 'lxml')

    tables = soup.find_all('td', class_='table')


    if tables != []:
        if tables[0].text != '...':
            with open(f'C:\\Users\\Stas\\Desktop\\hl7conv\\scraping datas\\{all_urls[all].split(".")[0][10:]} {filename_len_without_n[all]}.txt', 'a', encoding='utf-8') as scrap:
                scrap.write('\n\n' + f'class {filename_for_class[all]}(str, Enum):' + '\n')
                scrap.write('     ' + '"""' + '\n')
                scrap.write('     ' + f'{all_urls[all].split(".")[0][10:]} - {filename_len_without_n[all]}' + '\n\n')
                for x in range(0, len(tables), 5):
                    if tables[x].text != "...":
                        scrap.write('     ' + f'{tables[x].text}  {tables[1:][x].text}' + '\n')
                    else:
                        scrap.write('1312' + '\n')
                scrap.write('     ' + '"""' + '\n')
                scrap.write('\n\n')
                scrap.close()

            with open(f'C:\\Users\\Stas\\Desktop\\hl7conv\\scraping datas\\{all_urls[all].split(".")[0][10:]} {filename_len_without_n[all]}.txt', 'a', encoding='utf-8') as scrap_two:
                for x in range(0, len(tables), 5):

                    if tables[x].text != "...":
                        if tables[x].text[0] in '0123456789':

                            scrap_two.write('     ' + '_' + tables[x].text.replace('/', '_').replace(' ', '_').\
                            replace('.', '_').replace('<', '_').replace('>', '_').replace('&', '_').\
                            replace('', 'NEL').replace('-', '_').replace('or', '_').replace('+', '_').replace('??', 'QQ').\
                            replace('*', 'star').replace('#', 'hashtag').replace('%', 'percent').\
                            replace('(code=MVX)', '').replace(',', '_') + ' = ' + f'"{tables[x].text}"' + '\n')

                        else:

                            scrap_two.write('     ' + tables[x].text.replace('/', '_').replace(' ', '_').\
                            replace('.', '_').replace('<', '_').replace('>', '_').replace('&', '_').\
                            replace('', 'NEL').replace('-', '_').replace('or', '_').replace('+', '_').replace('??', 'QQ').\
                            replace('*', 'star').replace('#', 'hashtag').replace('%', 'percent').\
                            replace('(code=MVX)', '').replace(',', '_') + ' = ' + f'"{tables[x].text}"' + '\n')

                scrap_two.close()

        else:

            with open(f'C:\\Users\\Stas\\Desktop\\hl7conv\\chekc url\\{all_urls[all].split(".")[0][10:]} {filename_len_without_n[all]}.txt','a', encoding='utf-8') as empty_file_with_dots:
                empty_file_with_dots.write(tables[1].text)
            empty_file_with_dots.close()

    else:
        with open(f'C:\\Users\\Stas\\Desktop\\hl7conv\\chekc url\\{all_urls[all].split(".")[0][10:]} {filename_len_without_n[all]}.txt','a', encoding='utf-8') as empty_file:
            empty_file.write('check url')
        empty_file.close()

    print(f'[*]File: {count}')
    count += 1
