from time import sleep
from urllib.request import urlopen

import xlwt
from xlwt import Workbook

from Shop_helpers import getting_shufersal_price
from constants import *
from url_parsing import shufersal


def creating_xl(line):
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%H:%M")
    # while line_num:

    # line += 1
    for name, tag in ShufersalItems.items():
        _spacer = 0
        _index = list(ShufersalItems.keys()).index(name)
        if _index != 0:
            _spacer = 5 * _index

        page = urlopen(shufersal(tag))
        price = getting_shufersal_price(page)
        print(name + ": " + price)

        shufersal_sheet.write(line, SHUFERSAL_PRICE_COLUMN + _spacer, price)
        shufersal_sheet.write(line, SHUFERSAL_PRODUCT_COLUMN + _spacer, name)
        shufersal_sheet.write(line, SHUFERSAL_TIME_COLUMN + _spacer, time)
        shufersal_sheet.write(line, SHUFERSAL_DATE_COLUMN + _spacer, date)
        # line += 1
        # if tag == ShufersalItems.values()[-1]:
        #     print(tag + "^^^^^^")
        #     print(ShufersalItems.values()[-1])
    line += 1
    wb.save('Prices Track' + RANDOM_NUMBER + '.xls')
    sleep(10)
    return creating_xl(line)


""" main for Shufersal """

wb = Workbook()
style = xlwt.easyxf('font: bold 1')
# shufersal parameters
shufersal_sheet = wb.add_sheet('Shufersal')

for index in range(len(list(ShufersalItems.keys()))):
    spacer = 0
    if index != 0:
        spacer = 5 * index
    shufersal_sheet.write(0, SHUFERSAL_DATE_COLUMN + spacer, 'תאריך', style)
    shufersal_sheet.write(0, SHUFERSAL_TIME_COLUMN + spacer, 'שעה', style)
    shufersal_sheet.write(0, SHUFERSAL_PRICE_COLUMN + spacer, 'מחיר', style)
    shufersal_sheet.write(0, SHUFERSAL_PRODUCT_COLUMN + spacer, 'מוצר', style)

line_num = 1
creating_xl(line_num)



""" nice to haves """
# print(list(ShufersalItems.keys()).index(index))




""" tries to seccess """
# article = ''
# # for i in content():
#     # article = i.text
#     # article = article + i.text
# print(article)
# print(content)

# print(soup.prettify())
# print(soup.find_all('span'))
# element = soup.find("div", class_="modal-dialog")
# print(element.append("data-gtm"))
# JsonData = json.loads(element.__getattribute__("data-gtm"))
#
# result = json.loads(data)


# r = requests.get(url=url).json()
# print(r)
# data = r.json()

# x = data['']
# y = data['']
#
# print('x:%s\ny:%s' %(x, y))
