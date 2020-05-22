import csv
import json
import shutil
from time import sleep
from urllib.request import urlopen

from tqdm import tqdm

from Download_data import _delete_file
from constants import *
from data_from_json import Json

""" checking if network if alive """


def connect(host='http://google.com'):
    for _ in range(3):
        try:
            urlopen(host)
            return True
        except:
            print('No Internet!!\n trying again..')
            sleep(10)
    else:
        print('We tried 3 times --> there was not connection to the internet')
        return False


def importing_data_to_xl(path_of_src_xl_file, json_file_location, shop_name, path_of_output_xl_file):
    if not connect():
        exit()
    with open(path_of_src_xl_file, "r", encoding='utf-8') as source_file:
        source_sheet = csv.reader(source_file)
        for index, row in enumerate(source_sheet):
            with open(path_of_output_xl_file, "a", encoding='utf8', newline='') as output_file:
                writer = csv.writer(output_file)
                if index == 0:
                    with open(path_of_output_xl_file, "r", encoding='utf8', newline='') as check_output_file:
                        check_csv_dict = [row for row in csv.DictReader(check_output_file)]
                        if len(check_csv_dict) == 0:
                            # print("Excel file is empty creating new one now...")
                            writer.writerow(row)
                else:
                    tracking_num = row[COL_TRACKING_NUMBER]
                    tracking_num_by_competitors = row[COL_TRACKING_NUMBER_BY_COMPETITORS]
                    name = row[COL_PRODUCT_NAME]
                    tag = row[COL_PRODUCT_ID]
                    # name_by_website = row[COL_PRODUCT_NAME_FROM_WEBSITE]
                    # brand_name = row[COL_BRAND]

                    # date = datetime.datetime.now().strftime("%d/%m/%Y")

                    sale_price = row[COL_SALE_PRICE]
                    sale_price_per_unit = row[COL_SALE_PRICE_PER_UNIT]

                    with open(json_file_location) as json_file:
                        data = json.load(json_file)

                    # print(tag)
                    product_number = tag
                    product_data = Json(data, product_number)

                    name_by_website = product_data.get_name_of_product
                    brand_name = product_data.get_manufacturer_name
                    date = product_data.get_price_update_date
                    price = product_data.get_price
                    price_per_unit = product_data.get_item_price_per_unit
                    # sale_price = 0
                    # sale_price_per_unit = 0

                    writer.writerow(
                        [tracking_num, tracking_num_by_competitors, name, tag, name_by_website, brand_name, date, price,
                         price_per_unit, sale_price, sale_price_per_unit])

    _delete_file(json_file_location)
    shutil.copy2(path_of_output_xl_file, 'out-files\Backup\B_' + shop_name + '-' + DATE_STAMP + '.csv')
    return True


def get_progress_percent(src_xl, output_xl, hebrew_shop_name):
    # len_of_src_xl_file = sum(1 for row in src_xl)
    with open(output_xl, "r", encoding='utf-8') as f:
        first_output_reader = csv.reader(f, delimiter=",")
        first_output_row_count = len(list(first_output_reader))
    with open(src_xl, "r", encoding='utf-8') as v:
        src_reader = csv.reader(v, delimiter=",")
        src_row_count = len(list(src_reader)) - 1
    completion_percentage = 0
    pbar1 = tqdm(total=src_row_count, desc=" Downloading Prices To " + hebrew_shop_name, position=0)
    while True:
        sleep(1)
        with open(output_xl, "r", encoding='utf-8') as f:
            output_reader = csv.reader(f, delimiter=",")
            output_row_count = len(list(output_reader))
        if output_row_count <= first_output_row_count + src_row_count:
            # print("this is output row count " + str(output_row_count))
            # print("this is calc row count " + str(first_output_row_count + src_row_count))
            new_added_rows = output_row_count - first_output_row_count
            if new_added_rows != 0:
                completion_percentage = int(100 / (src_row_count / new_added_rows))
                pbar1.update(new_added_rows - pbar1.n)
        if completion_percentage == 100:
            print()
            exit()
