# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Set_prices(CommonUtils):
    # Pagemodel timestamp: 20160204165327
    # Pagemodel url: http://finndeco.codemen.fi/manage/#/dash/retailers/5/prices
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1600, 900)
    # Use project settings: True
    # Used filters: default
    # Depth of css path: 9
    # Minimize css selector: True
    # Use css pattern: False
    # Allow non unique css pattern: False
    # Pagemodel template: False
    # Use testability: False
    # Use contains text in xpath: True
    # Exclude dynamic table filter: True
    # Row count: 25
    # Element count: 140
    # Big element filter width: 55
    # Big element filter height: 40
    # Not filtered elements: button, strong, select
    # Canvas modeling: False
    # Pagemodel type: normal
    # Links found: 0
    # Page model constants:
    EMBER1029_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember1029>.glyphicon-user') # x: 1164 y: 19 width: 12 height: 12
    EMBER1037_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember1037>.glyphicon-briefcase') # x: 1261 y: 19 width: 12 height: 12
    CLASS_GLYPHICON_QUESTION_SIGN = (By.CLASS_NAME, u'glyphicon-question-sign') # x: 1444 y: 19 width: 12 height: 12
    EMBER768_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember768>.glyphicon-log-out') # x: 1477 y: 19 width: 12 height: 12
    CLASS_LOGO_MAIN = (By.CLASS_NAME, u'logo-main') # x: 80 y: 20 width: 100 height: 100
    CLASS_NOTIFICATION = (By.CLASS_NAME, u'notification') # x: 180 y: 30 width: 4 height: 4
    GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'h1>.glyphicon-briefcase') # x: 452 y: 106 width: 31 height: 31
    CLASS_GLYPHICON_DASHBOARD = (By.CLASS_NAME, u'glyphicon-dashboard') # x: 32 y: 166 width: 14 height: 14
    CLASS_GLYPHICON_SHOPPING_CART = (By.CLASS_NAME, u'glyphicon-shopping-cart') # x: 32 y: 202 width: 14 height: 14
    ID_EMBER4085 = (By.ID, u'ember4085') # x: 707 y: 229 width: 430 height: 34
    CLASS_GLYPHICON_TH = (By.CLASS_NAME, u'glyphicon-th') # x: 32 y: 238 width: 14 height: 14
    CLASS_GLYPHICON_CERTIFICATE = (By.CLASS_NAME, u'glyphicon-certificate') # x: 32 y: 274 width: 14 height: 14
    DELIVERY_PRICE = (By.CSS_SELECTOR, u'h3') # x: 707 y: 283 width: 430 height: 26
    EMBER1105_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember1105>.glyphicon-briefcase') # x: 32 y: 310 width: 14 height: 14
    ID_EMBER4086 = (By.ID, u'ember4086') # x: 707 y: 344 width: 430 height: 34
    CLASS_GLYPHICON_GBP = (By.CLASS_NAME, u'glyphicon-gbp') # x: 32 y: 346 width: 14 height: 14
    EMBER1129_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember1129>.glyphicon-user') # x: 32 y: 382 width: 14 height: 14
    CLASS_GLYPHICON_COG = (By.CLASS_NAME, u'glyphicon-cog') # x: 32 y: 418 width: 14 height: 14
    ID_EMBER4087 = (By.ID, u'ember4087') # x: 707 y: 460 width: 430 height: 34
    RETAILER_SIDEBAR = (By.CSS_SELECTOR, u'#retailer-sidebar>hr') # x: 0 y: 464 width: 260 height: 2
    EMBER781_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember781>.glyphicon-user') # x: 32 y: 496 width: 14 height: 14
    EMBER803_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember803>.glyphicon-log-out') # x: 32 y: 532 width: 14 height: 14
    ID_EMBER4088 = (By.ID, u'ember4088') # x: 707 y: 534 width: 430 height: 34
    ID_EMBER4089 = (By.ID, u'ember4089') # x: 707 y: 608 width: 430 height: 34
    ID_EMBER4090 = (By.ID, u'ember4090') # x: 707 y: 682 width: 430 height: 34
    ID_EMBER4091 = (By.ID, u'ember4091') # x: 707 y: 756 width: 430 height: 34

    # Dynamic objects:
    set_prices_link = (By.LINK_TEXT, u'Set prices')     # x: 0 y: 336 width: 260 height: 36 # Dynamic object
    VAT_MULTIPLIER_FIELD = (By.XPATH, u'//div[@id="retailer-content-floated"]/div/div/div/div[2]/div/div/input')     # x: 707 y: 229 width: 430 height: 34 # Dynamic object
    SET_PRICES_LINK = (By.LINK_TEXT, u'Set prices')     # x: 0 y: 336 width: 260 height: 36 # Dynamic object


    def click_set_prices_link(self):
        self.click(self.set_prices_link)

    def type_string_to_vat_multiplier_field(self, parameters=None):
        self.type(self.ID_EMBER4085, parameters)

    def type_string_to_vat_multiplier_field(self, parameters=None):
        self.type(self.VAT_MULTIPLIER_FIELD, parameters)

    def click_set_prices_link(self):
        self.click(self.SET_PRICES_LINK)

    def click_element_set_prices_link(self):
        self.click_element(self.SET_PRICES_LINK)

    def wait_until_element_is_visible_vat_multiplier_field(self):
        self.wait_until_element_is_visible(self.VAT_MULTIPLIER_FIELD)

    def input_text_vat_multiplier_field(self, parameters=None):
        self.input_text(self.VAT_MULTIPLIER_FIELD, parameters)
