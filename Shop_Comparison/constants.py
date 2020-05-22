import datetime
from random import randint

DATE_STAMP = datetime.datetime.now().strftime("%d_%m_%Y(%H-%M)")
datetime_for_ybitan = datetime.datetime.now().strftime("%Y%m%d")
# TIME_STAMP = datetime.datetime.now().strftime("%H:%M:%S")

""" xl Column num """
COL_TRACKING_NUMBER = 0
COL_TRACKING_NUMBER_BY_COMPETITORS = 1
COL_PRODUCT_NAME = 2
COL_PRODUCT_ID = 3
COL_PRODUCT_NAME_FROM_WEBSITE = 4
COL_BRAND = 5
COL_DATE_COLUMN = 6
COL_PRICE_COLUMN = 7
COL_PRICE_PER_UNIT = 8
COL_SALE_PRICE = 9
COL_SALE_PRICE_PER_UNIT = 10

# TIME_COLUMN = 1

RANDOM_NUMBER = str(randint(1, 99))

# if there is no product:
NO_PRODUCT_ERROR = 'מוצר לא נמצא! יש לבדוק באתר אם המוצר קיים'
NO_INTERNET_ERROR = 'לא היה אינטרנט בזמן הוצאת המוצר, אנא נסה שוב בחיבור יציב!'
NOT_AVAILABLE_PRODUCT = 'מוצר לא זמין באתר, כנראה נגמר המלאי'

PATH_OF_BACKUP_FILE = '\out-files\Backup\B_'

VICTORY_DATA_BASE_URL = 'http://matrixcatalog.co.il/NBCompetitionRegulations.aspx'
SHUFERSAL_DATA_BASE_URL = 'http://prices.shufersal.co.il/'
RAMILEVI_DATA_BASE_URL = 'https://url.retail.publishedprices.co.il/login'
RAMILEVI_USERNAME = 'RamiLevi'
YBITAN_DATA_BASE_URL = f'http://publishprice.ybitan.co.il/{datetime_for_ybitan}/'

VICTORY_STORE_NUM = 1
SHUFERSAL_STORE_NUM = 1
RAMILEVI_STORE_NUM = "001"
YBITAN_STORE_NUM = 1

EMPTY_ITEM_DATA = {'PriceUpdateDate': '', 'ItemCode': '', 'ItemType': '',
                                      'ItemName': 'מוצר לא נמצא', 'ManufacturerName': '',
                                      'ManufactureCountry': '', 'ManufacturerItemDescription': '',
                                      'UnitQty': '', 'Quantity': '', 'bIsWeighted': '',
                                      'UnitOfMeasure': '', 'QtyInPackage': '', 'ItemPrice': '',
                                      'UnitOfMeasurePrice': '', 'AllowDiscount': '', 'ItemStatus': ''}