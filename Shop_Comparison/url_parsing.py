# from Shop_helpers import getting_uuid_and_cat_by_product_id_for_rami_levi, getting_product_id_for_victory, \
#     getting_product_id_for_my_supermarket
#
# """ Url Parsing of Shufersal """
#
#
# def shufersal_url(product_num):
#     product_number = product_num  # מק"ט
#     parsed_product_number = 'P_' + str(product_number)
#     const_url = "https://www.shufersal.co.il/online/he/p/" + parsed_product_number + "/json?cartContext%5BopenFrom%5D=SEARCH&cartContext%5BrecommendationType%5D=PRODUCT"
#     return const_url
#
#
# """ Url Parsing of Rami-levi """
#
#
# def rami_levi_url(product_num):
#     line_number = 0
#     try:
#         with open("source-files\Rami_levi_URLs.txt") as file:
#             all_lines = file.readlines()
#             for line in all_lines:
#                 line = line.rstrip()
#                 if str(product_num) in line:
#                     const_url = all_lines[line_number+1]
#                     # print(const_url)
#                     break
#                 else:
#                     line_number += 1
#             else:
#                 cat_id, uuid = getting_uuid_and_cat_by_product_id_for_rami_levi(product_num)
#                 if cat_id == '' and uuid == '':
#                     const_url = ''
#                 elif cat_id == '_' and uuid == '_':
#                     const_url = '_'
#                 else:
#                     const_url = "https://www.rami-levy.co.il/default.asp?isjson=true&catid=" + cat_id + "&details_type=1&itemid=" + uuid
#                     # print(const_url)
#                     with open("source-files\Rami_levi_URLs.txt", "a+") as file_writer:
#                         file_writer.write(str(product_num) + "\n" + const_url + "\n")
#                         # print("A new coded Rami-Levi URL has been added to your text file")
#     except IOError:
#         open("source-files\Rami_levi_URLs.txt", "a+")
#         print("The old Rami_levi_URLs.txt file has been deleted...\nA new URLs file as been created!")
#         return rami_levi_url(product_num)
#     print(const_url)
#     return const_url
#
#
# """ Url Parsing of Victory """
#
#
# def victory_url(name_of_product):
#     line_number = 0
#     try:
#         with open("source-files\Victory_URLs.txt", encoding='utf-8') as file:
#             all_lines = file.readlines()
#             for line in all_lines:
#                 line = line.rstrip()
#                 line = line
#                 if name_of_product in line:
#                     const_url = all_lines[line_number + 1]
#                     # print(const_url)
#                     break
#                 else:
#                     line_number += 1
#             else:
#                 id = getting_product_id_for_victory(name_of_product)
#                 if id == '':
#                     const_url = ''
#                 elif id == '_':
#                     const_url = '_'
#                 else:
#                     const_url = "http://www.victoryonline.co.il/Ajax/FetchUserControl.aspx?UserControl=Popup_NgProductDetails&ProductID=" + id
#                     # print(const_url)
#                     with open("source-files\Victory_URLs.txt", "a+", encoding='utf-8') as file_writer:
#                         file_writer.write(name_of_product + "\n" + const_url + "\n")
#                         # print("A new coded Victory URL has been added to your text file")
#     except IOError:
#         open("source-files\Victory_URLs.txt", "a+")
#         # print("The old Victory_URLs.txt file has been deleted...\nA new URLs file as been created!")
#         return victory_url(name_of_product)
#     return const_url
#
#
# def mysupermarket_url(product_num):
#     line_number = 0
#     try:
#         with open("source-files\My_Supermarket_URLs.txt") as file:
#             all_lines = file.readlines()
#             for line in all_lines:
#                 line = line.rstrip()
#                 if str(product_num) in line:
#                     const_url = all_lines[line_number+1]
#                     # print(const_url)
#                     break
#                 else:
#                     line_number += 1
#             else:
#                 cat_id, uuid = getting_product_id_for_my_supermarket(product_num)
#                 if cat_id == '' and uuid == '':
#                     const_url = ''
#                 elif cat_id == '_' and uuid == '_':
#                     const_url = '_'
#                 else:
#                     const_url = "https://www.mysupermarket.co.il/Ajax/FetchUserControl.aspx?UserControl=Popup_NgProductDetails&ProductID=" + cat_id
#                     # print(const_url)
#                     with open("source-files\My_Supermarket_URLs.txt", "a+") as file_writer:
#                         file_writer.write(str(product_num) + "\n" + const_url + "\n")
#                         print("A new coded My-Supermarket URL has been added to your text file")
#     except IOError:
#         open("source-files\My_Supermarket_URLs.txt", "a+")
#         print("The old My_Supermarket_URLs.txt file has been deleted...\nA new URLs file as been created!")
#         return rami_levi_url(product_num)
#     print(const_url)
#     return const_url
#
