from Download_data import StoreDataBase
from Shop_helpers import importing_data_to_xl
from constants import VICTORY_DATA_BASE_URL, VICTORY_STORE_NUM, SHUFERSAL_DATA_BASE_URL, SHUFERSAL_STORE_NUM, \
    RAMILEVI_DATA_BASE_URL, RAMILEVI_STORE_NUM


# def victory_main():
#     """ main for Victory """
#     # print("starting Victory: ... ")
#     store_data = StoreDataBase(url=VICTORY_DATA_BASE_URL, store_number=VICTORY_STORE_NUM)
#     store_data.download_prices()
#     importing_data_to_xl(path_of_src_xl_file="source-files\Victory-src-csv.csv", ShopUrl=victory_url,
#                          price_func=getting_victory_price, shop_name='Victory',
#                          path_of_output_xl_file='out-files\Victory-out-csv.csv')

# print("\nFinished Victory!!!!!!!!!")
# if __name__ == '__main__':

def shufersal_main():
    """ main for Shufersal """
    # print("starting Shufersal: ... ")
    store_data = StoreDataBase(url=SHUFERSAL_DATA_BASE_URL, store_number=SHUFERSAL_STORE_NUM, store_name='Shufersal')
    json_file = store_data.download_prices()

    importing_data_to_xl(path_of_src_xl_file="source-files\shufersal-src-csv.csv", json_file_location=json_file, shop_name='Shufersal',
                         path_of_output_xl_file='out-files\Sufersal-out-csv.csv')

    # print("\nFinished Shufersal!!!!!!!!!")
# shufersal_main()


# if __name__ == '__main__':
def rami_levi_main():
    """ main for Rami-levi """
    # print("starting RamiLevi: ...")
    store_data = StoreDataBase(url=RAMILEVI_DATA_BASE_URL, store_number=RAMILEVI_STORE_NUM, store_name='RamiLevi')
    json_file = store_data.download_prices()

    importing_data_to_xl(path_of_src_xl_file="source-files\RamiLevi-src-csv.csv", json_file_location=json_file,
                         shop_name='RamiLevi',
                         path_of_output_xl_file='out-files\RamiLevi-out-csv.csv')

    # print("\nFinished Rami-levi!!!!!!!!!")

# rami_levi_main()
