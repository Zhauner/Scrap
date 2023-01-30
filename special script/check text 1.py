import os

scraping_files = os.listdir('C:\\Users\\Stas\\Desktop\\hl7conv\\chekc url')

for file in scraping_files:

    datas = open(f'C:\\Users\\Stas\\Desktop\\hl7conv\\chekc url\\{file}', 'r',encoding='utf-8')
    text = datas.readlines()

    if 'no suggested values' not in text and 'No suggested values defined' not in text and 'No suggested values' not in text and 'No suggested values defined.' not in text and 'No suggested value defined' not in text and 'No suggested values.' not in text:

        print(f'{file}  {text}')