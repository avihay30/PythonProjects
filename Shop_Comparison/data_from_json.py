class Json:

    def __init__(self, json_data, product_number):
        try:
            for item in json_data['root']['Items']['Item']:
                if product_number == item['ItemCode']:
                    self.item_data = item
                    break
        except KeyError:
            for item in json_data['Root']['Items']['Item']:
                if product_number == item['ItemCode']:
                    self.item_data = item
                    break
            else:
                self.item_data = {'PriceUpdateDate': '', 'ItemCode': '', 'ItemType': '',
                                  'ItemName': 'מוצר לא נמצא', 'ManufacturerName': '',
                                  'ManufactureCountry': '', 'ManufacturerItemDescription': '',
                                  'UnitQty': '', 'Quantity': '', 'bIsWeighted': '',
                                  'UnitOfMeasure': '', 'QtyInPackage': '', 'ItemPrice': '',
                                  'UnitOfMeasurePrice': '', 'AllowDiscount': '', 'ItemStatus': ''}

    @property
    def get_price(self):
        item_price = self.item_data['ItemPrice']
        return item_price

    @property
    def get_name_of_product(self):
        name_of_product = self.item_data['ItemName']
        return name_of_product

    @property
    def get_manufacturer_name(self):
        manufacturer_name = self.item_data['ManufacturerName']
        return manufacturer_name

    @property
    def get_size_type(self):
        size_type = self.item_data['UnitQty']
        return size_type

    @property
    def get_size(self):
        size = self.item_data['Quantity']
        return size

    @property
    def get_units_in_package(self):
        units_in_package = self.item_data['QtyInPackage']
        return units_in_package

    @property
    def get_unit_of_measure(self):
        unit_of_measure = self.item_data['UnitOfMeasure']
        return unit_of_measure

    @property
    def get_item_price_per_unit(self):
        item_price_per_unit = self.item_data['UnitOfMeasurePrice']
        return item_price_per_unit

    @property
    def get_price_update_date(self):
        price_update_date = self.item_data['PriceUpdateDate']
        return price_update_date

    @property
    def get_all_as_dict(self):
        return self.item_data
