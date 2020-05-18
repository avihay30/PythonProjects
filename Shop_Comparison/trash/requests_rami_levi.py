from time import sleep
from urllib.request import urlopen

import xlwt
from xlwt import Workbook

from Shop_helpers import getting_rami_levi_price
from constants import *
from url_parsing import rami_levi


def creating_xl(line):
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%H:%M")
    # while line_num:

    # line += 1
    for name, tag in RamiLeviItems.items():
        _spacer = 0
        _index = list(RamiLeviItems.keys()).index(name)
        if _index != 0:
            _spacer = 5 * _index

        page = urlopen(rami_levi(tag))
        price = getting_rami_levi_price(page)
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
    wb.save('Rami-Levi Prices Track' + RANDOM_NUMBER + '.xls')
    sleep(10)
    return creating_xl(line)





""" main for Rami-levi """

wb = Workbook()
style = xlwt.easyxf('font: bold 1')
# shufersal parameters
shufersal_sheet = wb.add_sheet('Rami-levi')

for index in range(len(list(RamiLeviItems.keys()))):
    spacer = 0
    if index != 0:
        spacer = 5 * index
    shufersal_sheet.write(0, SHUFERSAL_DATE_COLUMN + spacer, 'תאריך', style)
    shufersal_sheet.write(0, SHUFERSAL_TIME_COLUMN + spacer, 'שעה', style)
    shufersal_sheet.write(0, SHUFERSAL_PRICE_COLUMN + spacer, 'מחיר', style)
    shufersal_sheet.write(0, SHUFERSAL_PRODUCT_COLUMN + spacer, 'מוצר', style)

line_num = 1
creating_xl(line_num)

# print(getting_uuid_by_product_id("7290015834469"))
