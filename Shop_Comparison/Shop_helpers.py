import csv
import re
import shutil
from time import sleep
from urllib.error import URLError
from urllib.request import urlopen

from bs4 import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

from constants import *

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
        return False


""" extraction of the id of a product by it's name """


def getting_product_id_for_victory(product_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C:\Develpment\PycharmProjects\chromedriver.exe', chrome_options=chrome_options)
    driver.set_page_load_timeout(15)
    try:
        driver.get('https://www.victoryonline.co.il/מבצעים_מומלצים/מדף')
        search = driver.find_element_by_id('txtfind')
        search.click()
        search.send_keys(product_name)
        driver.find_element_by_class_name('MagnifyIcon').click()
        sleep(2)
        try:
            id = driver.find_element_by_css_selector("li.NgMspProductCell.MSM.Expanded")
            id = id.get_attribute('productid')
        except NoSuchElementException:
            id = ''
    except TimeoutException:
        print("Timeout!!!, retrying...\nPlease try to reconnect to the internet and run again.")
        sleep(5)
        driver.quit()
        id = '_'
    return id


# getting_product_id_for_victory('מגבונים לחים בבישום עדין טיטולים')

""" extraction of the uuid of a product by it's id->(מק"ט)  """


def getting_uuid_and_cat_by_product_id_for_rami_levi(id):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C:\Develpment\PycharmProjects\chromedriver.exe', chrome_options=chrome_options)
    driver.set_page_load_timeout(15)
    try:
        driver.get('https://www.rami-levy.co.il/')
        search = driver.find_element_by_id('strSearch')
        try:
            search.click()
        except ElementClickInterceptedException:
            driver.execute_script('arguments[0].click();', search)
        # sleep(2)
        search.send_keys(id)
        driver.find_element_by_class_name('search_but').click()
        """ getting the uuid """
        sleep(2)
        try:
            uuid = driver.find_element_by_css_selector("div.image_icons_zone")
            uuid = uuid.get_attribute('id')
            """ getting the cat-id """
            cat_id_holder = driver.find_element_by_xpath('//*[@id="tblSearchCategories"]/ul/li/a').get_attribute('href')
            cat_id = cat_id_holder.split('=')[3]
        except NoSuchElementException:
            cat_id = ''
            uuid = ''

    except TimeoutException:
        print("Timeout, retrying...\nPlease try to reconnect to the internet and run again.")
        driver.quit()
        cat_id = '_'
        uuid = '_'

    return cat_id, uuid


""" extraction of the price of a product by parsing the html """


def getting_victory_price(html_page):
    # html_page = urlopen('http://www.victoryonline.co.il/Ajax/FetchUserControl.aspx?UserControl=Popup_NgProductDetails&ProductID=3679')
    soup = BeautifulSoup(html_page, "html.parser")
    try:
        price_content = soup.find('span', {"class": "Offer"})
        price = price_content.text.strip()[1:]
    except AttributeError:
        price_content = soup.find('span', {"class": "Price"})
        price = price_content.text.strip()[1:]
    try:
        price_per_item_content = soup.find('span', {"class": "AfterOffer"})
        price_per_item = ''.join(re.findall(r"[-+]?\d*\.\d+|\d+", price_per_item_content.text.strip()))
    except AttributeError:
        try:
            price_per_item_content = soup.find('span', {"class": "BeforeOffer"})
            price_per_item = ''.join(re.findall(r"[-+]?\d*\.\d+|\d+", price_per_item_content.text.strip()))
        except AttributeError:
            price_per_item = '/'
            product_name = ''
            brand_name = ''
    """ checking if the value is below zero('אג) """
    if price_per_item != '/':
        list_price_per_item_content = list(price_per_item_content.text)
        reversed_list = list_price_per_item_content[::-1]
        for k, v in enumerate(list_price_per_item_content):
            if v == "א" and list_price_per_item_content[k + 1] == "ג":
                if reversed_list[-2] == '.':
                    price_per_item = '0.0' + str(''.join(price_per_item)).replace('.', '')
                elif reversed_list[-3] == '.':
                    price_per_item = '0.' + str(''.join(price_per_item)).replace('.', '')
                else:
                    price_per_item = '0.' + str(''.join(price_per_item))

        product_name_content = soup.find('span', {"class": "PrefixWrp"})
        product_name = product_name_content.text.strip()
        brand_name_content = soup.find('span', {"id": "Brand"})
        brand_name = brand_name_content.text.strip()
    return price, price_per_item, product_name, brand_name


# getting_victory_price("_")


def getting_rami_levi_price(html_page):
    # html_page = urlopen('https://www.rami-levy.co.il/default.asp?isjson=true&catid={7787895C-FF87-4283-A2E8-A9876CCD3E36}&details_type=1&itemid={BBB7501B-B656-45E4-A8DE-C1767AB1E253}')
    price = 0
    price_per_item = 0
    product_name = ""
    brand_name = ""
    soup = BeautifulSoup(html_page, "html.parser")

    price_content = soup.find('div', {"class": "product_attr"})
    extra_soup = BeautifulSoup(str(price_content), "html.parser").prettify()
    extra_soup = BeautifulSoup(extra_soup, 'html.parser')
    extra_soup = extra_soup.find({"div"})

    # generating a list of the HTML page
    man_content = str(extra_soup).split("\n")

    # list iteration
    for i in range(0, len(man_content)):
        man_value = man_content[i].strip()
        if man_value == "שם ספק:":
            brand_name = man_content[i + 3].strip()
        try:
            price_per_item_content = soup.find('div', {'class': 'prodNotes'})
            price_per_item = price_per_item_content.text.strip().replace('(', "").replace(')', "").strip()
        except AttributeError:
            if man_value == "מחיר ליחידת מידה:":
                price_per_item = man_content[i + 3].strip()
        if man_value == "שם פריט:":
            product_name = man_content[i + 3].strip()
        if man_value == "מחיר:":
            price = man_content[i + 3].strip()
        if man_value == "שם ספק/ יצרן:":
            brand_name = man_content[i + 3].strip()
        if man_value == "שם מותג:":
            brand_name = man_content[i + 3].strip()
            break
    # else:
    # print("\nthere was a problem with the extraction of the price!)
    if brand_name == '</div>' or brand_name == '<div>':
        brand_name = ''
    return price, price_per_item, product_name, brand_name


# getting_rami_levi_price('_')

def getting_shufersal_price(html_page):
    # html_page = urlopen('https://www.shufersal.co.il/online/he/p/P_63140/json?cartContext%5BopenFrom%5D=SEARCH&cartContext%5BrecommendationType%5D=PRODUCT')
    soup = BeautifulSoup(html_page, "html.parser")
    price_content = soup.find('div', {"itemprop": "price"})
    price = price_content.text.strip()[:-1]
    price_per_item_content = soup.find('div', {"class": "smallText"})
    price_per_item = price_per_item_content.text.strip()
    product_name_content = soup.find('h3', {"class": "title"})
    product_name = product_name_content.text.strip()
    try:
        brand_name_content = soup.find('div', {"class": "text tooltip-js"})
        """ AttributeError: 'NoneType' object has no attribute 'text'(shufelsal(https://www.shufersal.co.il/online/he/p/P_7296073345299/json?cartContext%5BopenFrom%5D=SEARCH&cartContext%5BrecommendationType%5D=PRODUCT) """
        brand_name = brand_name_content.text.strip()
    except AttributeError:
        brand_name_content = soup.find('div', {"itemprop": "description"})
        """ there is an option here to get a size of the products(units) """
        brand_name = brand_name_content.text.strip().split('\n')[-1].strip()
    except Exception:
        brand_name = ''
    return price, price_per_item, product_name, brand_name


# getting_shufersal_price("_")

def importing_data_to_xl(path_of_src_xl_file, ShopUrl, price_func, shop_name, path_of_output_xl_file):
    if not connect():
        print('We tried 3 times --> there was not connection to the internet')
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

                    date = datetime.datetime.now().strftime("%d/%m/%Y")
                    if shop_name == 'Victory':
                        html_page = ShopUrl(name)
                    else:
                        html_page = ShopUrl(tag)

                    if html_page == '':
                        price = ''
                        price_per_unit = ''
                        name_by_website = NO_PRODUCT_ERROR
                        brand_name = ''
                    elif html_page == '_':
                        price = ''
                        price_per_unit = ''
                        name_by_website = NO_INTERNET_ERROR
                        brand_name = ''
                    else:
                        try:
                            page = urlopen(html_page)
                        except URLError:
                            print("There was no internet while downloading the product... Please try again at stable connection!\n Link: " + html_page)
                            name_by_website = NO_INTERNET_ERROR
                            continue

                        price, price_per_unit, name_by_website, brand_name = price_func(page)

                    sale_price = row[COL_SALE_PRICE]
                    sale_price_per_unit = row[COL_SALE_PRICE_PER_UNIT]

                    # print(name_by_website + ": " + price + "\n")
                    # tqdm.write(name_by_website + ": " + price + "\n")
                    if price_per_unit == '/':
                        price = ''
                        price_per_unit = ''
                        name_by_website = NOT_AVAILABLE_PRODUCT
                        brand_name = ''

                    writer.writerow(
                        [tracking_num, tracking_num_by_competitors, name, tag, name_by_website, brand_name, date, price,
                         price_per_unit, sale_price, sale_price_per_unit])

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
        sleep(3)
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
