import os

scraping_files = os.listdir('C:\\Users\\Stas\\Desktop\\hl7conv\\scraping datas')

for files in scraping_files:

    datas = open(f'C:\\Users\\Stas\\Desktop\\hl7conv\\scraping datas\\{files}', 'r',encoding='utf-8')
    text = datas.readlines()

    with open('C:\\Users\\Stas\\Desktop\\hl7conv\\hl7conv\\schemas\\versions\\v2_8\\enums.py', 'a', encoding='utf-8') as f:
        for x in text:
            f.write(x)
        f.close()
