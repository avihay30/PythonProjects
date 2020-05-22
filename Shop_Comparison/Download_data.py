import collections
import glob
import gzip
import os
import pathlib
import shutil
import re

import xml2json
import xmltodict
import pprint
import json

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import datetime_for_ybitan, DATE_STAMP, RAMILEVI_DATA_BASE_URL, RAMILEVI_USERNAME, \
    SHUFERSAL_DATA_BASE_URL, VICTORY_DATA_BASE_URL
from data_from_json import Json


def _delete_file(file_location):
    os.remove(file_location)


def _xml_to_json(store_num):  # accessing one file at a time
    xml_file = ''.join(glob.glob("Download/xml/*.xml"))
    with open(xml_file, encoding='utf-8') as fd:
        data_dict = xmltodict.parse(fd.read())

    json_data = json.dumps(data_dict, ensure_ascii=False).encode("utf-8")
    json_file_location = f'Download/xml/{DATE_STAMP}store_number-{store_num}.json'
    with open(json_file_location, 'w') as json_file:
        json_file.write(json_data.decode())

    return json_file_location


def _gz_to_json(store_num):  # accessing one file at a time
    gz_file_location = ''.join(glob.glob("Download/*.gz"))
    xml_file_location = f'Download/xml/{DATE_STAMP}store_number-{store_num}.xml'
    with gzip.open(gz_file_location, 'rb') as gz_file_location:
        with open(xml_file_location, 'wb') as xml_file:
            shutil.copyfileobj(gz_file_location, xml_file)

    json_file_name = _xml_to_json(store_num)

    _delete_file(gz_file_location.filename)
    _delete_file(xml_file_location)

    return json_file_name


class StoreDataBase(object):
    def __init__(self, url, store_number):
        self.store_number = store_number
        self.url = url

    def _shufersal_downloader(self, driver):
        category_drawer = driver.find_element_by_id('ddlCategory')
        category_drawer.click()
        category_drawer_select = driver.find_element_by_xpath('//*[@id="ddlCategory"]/option[3]')
        category_drawer_select.click()
        store_drawer = driver.find_element_by_xpath('//*[@id="ddlStore"]').click()
        store_drawer_select = driver.find_element_by_xpath(f'//*[@id="ddlStore"]/option[{self.store_number + 1}]')
        store_drawer_select.click()
        sleep(5)
        download = driver.find_element_by_xpath('//*[@id="gridContainer"]/table/tbody/tr/td[1]/a')
        download.click()
        return

    def _ramilevi_downloader(self, driver):
        user_name = driver.find_element_by_id('username')
        user_name.send_keys(RAMILEVI_USERNAME)
        sign_in = driver.find_element_by_id('login-button')
        sign_in.click()
        sleep(1.5)
        file_name_tamplate = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/form/div[2]/table/tbody/tr[1]')
        file_name_tamplate = file_name_tamplate[0].text.split()[0]
        name_tamplate = re.split("(\d+)+[-.]", file_name_tamplate, 4)
        generated_number = name_tamplate[1]
        search_field = driver.find_element_by_xpath('//*[@id="fileList_filter"]/input')
        search_field.send_keys(f"PriceFull{generated_number}-{self.store_number}")
        sleep(1.5)
        download = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/table/tbody/tr/td[1]/a')
        download.click()
        return

    def _victory_downloader(self, driver):
        user_name = driver.find_element_by_id('username')
        user_name.send_keys(RAMILEVI_USERNAME)
        sign_in = driver.find_element_by_id('login-button')
        sign_in.click()
        return

    def download_prices(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        prefs = {"download.default_directory": f"{pathlib.Path().absolute()}\Download"}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
        driver.set_page_load_timeout(15)
        driver.get(self.url)

        if self.url == RAMILEVI_DATA_BASE_URL:
            self._ramilevi_downloader(driver)

        elif self.url == SHUFERSAL_DATA_BASE_URL:
            self._shufersal_downloader(driver)

        elif self.url == VICTORY_DATA_BASE_URL:
            self._victory_downloader(driver)

        # "is_downloaded?"
        while not glob.glob("Download/*.gz"):
            sleep(0.1)
        driver.close()

        json_file_location = _gz_to_json(self.store_number)

        return json_file_location
