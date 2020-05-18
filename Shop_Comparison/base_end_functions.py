from Shop_helpers import importing_data_to_xl, getting_victory_price, getting_shufersal_price, getting_rami_levi_price
from url_parsing import rami_levi_url, shufersal_url, victory_url


def victory_main():
    """ main for Victory """
    # print("starting Victory: ... ")
    importing_data_to_xl(path_of_src_xl_file="source-files\Victory-src-csv.csv", ShopUrl=victory_url,
                         price_func=getting_victory_price, shop_name='Victory',
                         path_of_output_xl_file='out-files\Victory-out-csv.csv')

    # print("\nFinished Victory!!!!!!!!!")


def shufersal_main():
    """ main for Shufersal """
    # print("starting Shufersal: ... ")
    importing_data_to_xl(path_of_src_xl_file="source-files\shufersal-src-csv.csv", ShopUrl=shufersal_url,
                         price_func=getting_shufersal_price, shop_name='Shufersal',
                         path_of_output_xl_file='out-files\Sufersal-out-csv.csv')

    # print("\nFinished Shufersal!!!!!!!!!")


def rami_levi_main():
    """ main for Rami-levi """
    # print("starting RamiLevi: ...")
    importing_data_to_xl(path_of_src_xl_file="source-files\RamiLevi-src-csv.csv", ShopUrl=rami_levi_url,
                         price_func=getting_rami_levi_price, shop_name='RamiLevi',
                         path_of_output_xl_file='out-files\RamiLevi-out-csv.csv')

    # print("\nFinished Rami-levi!!!!!!!!!")
