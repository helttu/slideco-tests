# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Track_orders(CommonUtils):
    # Pagemodel timestamp: 20160201110849
    # Pagemodel url: http://finndeco.codemen.fi/manage/#/dash/retailers/5/orders
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
    # Links found: 1
    # Page model constants:
    EMBER1029_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember1029>.glyphicon-user') # x: 1164 y: 19 width: 12 height: 12
    EMBER1037_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember1037>.glyphicon-briefcase') # x: 1261 y: 19 width: 12 height: 12
    CLASS_GLYPHICON_QUESTION_SIGN = (By.CLASS_NAME, u'glyphicon-question-sign') # x: 1444 y: 19 width: 12 height: 12
    EMBER768_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember768>.glyphicon-log-out') # x: 1477 y: 19 width: 12 height: 12
    CLASS_NOTIFICATION = (By.CLASS_NAME, u'notification') # x: 180 y: 30 width: 4 height: 4
    GLYPHICON_SHOPPING_CART = (By.CSS_SELECTOR, u'h1>.glyphicon-shopping-cart') # x: 308 y: 104 width: 36 height: 36
    ORDERS = (By.LINK_TEXT, u'Orders') # x: 308 y: 156 width: 76 height: 42
    CLASS_GLYPHICON_PLUS = (By.CLASS_NAME, u'glyphicon-plus') # x: 1415 y: 164 width: 12 height: 12
    CLASS_GLYPHICON_DASHBOARD = (By.CLASS_NAME, u'glyphicon-dashboard') # x: 32 y: 166 width: 14 height: 14
    EMBER1069_GLYPHICON_SHOPPING_CART = (By.CSS_SELECTOR, u'#ember1069>.glyphicon-shopping-cart') # x: 32 y: 202 width: 14 height: 14
    CLASS_GLYPHICON_TH = (By.CLASS_NAME, u'glyphicon-th') # x: 32 y: 238 width: 14 height: 14
    EMBER1094_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember1094>.glyphicon-certificate') # x: 32 y: 274 width: 14 height: 14
    EMBER1105_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember1105>.glyphicon-briefcase') # x: 32 y: 310 width: 14 height: 14
    CLASS_GLYPHICON_GBP = (By.CLASS_NAME, u'glyphicon-gbp') # x: 32 y: 346 width: 14 height: 14
    BTN_SM_DEFAULT_ACTIVE_ASCENDING = (By.CSS_SELECTOR, u'button.btn.btn-sm.btn-default.active') # x: 1251 y: 352 width: 80 height: 30
    EMBER1129_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember1129>.glyphicon-user') # x: 32 y: 382 width: 14 height: 14
    ID_ORDERS_LIST_CREATED = (By.XPATH, u'id(\'table-orders-list\')/THEAD[1]/TR[1]/TH[2]') # x: 423 y: 397 width: 80 height: 51
    CONTAINS_TEXT_TOTAL = (By.XPATH, u'//th[contains(text(),"Total")]') # x: 680 y: 397 width: 88 height: 51
    ID_ORDERS_LIST = (By.XPATH, u'id(\'table-orders-list\')/THEAD[1]/TR[1]/TH[5]') # x: 768 y: 397 width: 18 height: 51
    CONTAINS_TEXT_CREATED_BY = (By.XPATH, u'//th[contains(text(),"Created by")]') # x: 1141 y: 397 width: 80 height: 51
    CONTAINS_TEXT_CURRENT_RETAILER = (By.XPATH, u'//th[contains(text(),"Current Retailer")]') # x: 1221 y: 397 width: 80 height: 51
    CLASS_GLYPHICON_COG = (By.CLASS_NAME, u'glyphicon-cog') # x: 32 y: 418 width: 14 height: 14
    EMBER6947_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember6947>.glyphicon-briefcase') # x: 1223 y: 453 width: 14 height: 14
    EMBER6997_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember6997>.glyphicon-certificate') # x: 1157 y: 463 width: 14 height: 14
    RETAILER_SIDEBAR = (By.CSS_SELECTOR, u'#retailer-sidebar>hr') # x: 0 y: 464 width: 260 height: 2
    ID_EMBER6950 = (By.ID, u'ember6950') # x: 1303 y: 466 width: 71 height: 30
    GDL_ORDER_962_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_962>td>.btn-group>.btn-danger') # x: 1406 y: 466 width: 58 height: 30
    GDL_ORDER_962_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_962>td.text-center>.unread') # x: 971 y: 473 width: 5 height: 16
    EMBER6952_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember6952>.glyphicon-pencil') # x: 1384 y: 475 width: 12 height: 12
    EMBER781_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember781>.glyphicon-user') # x: 32 y: 496 width: 14 height: 14
    EMBER6985_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember6985>.glyphicon-briefcase') # x: 1223 y: 518 width: 14 height: 14
    EMBER6999_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember6999>.glyphicon-certificate') # x: 1157 y: 528 width: 14 height: 14
    ID_EMBER6988 = (By.ID, u'ember6988') # x: 1303 y: 531 width: 71 height: 30
    GDL_ORDER_968_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_968>td>.btn-group>.btn-danger') # x: 1406 y: 531 width: 58 height: 30
    EMBER803_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember803>.glyphicon-log-out') # x: 32 y: 532 width: 14 height: 14
    GDL_ORDER_968_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_968>td.text-center>.unread') # x: 971 y: 538 width: 5 height: 16
    EMBER6990_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember6990>.glyphicon-pencil') # x: 1384 y: 540 width: 12 height: 12
    ID_RETAILER_CONTENT_FLOATED_0 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[5]/DIV[1]/DIV[1]/BUTTON[1]') # x: 308 y: 630 width: 34 height: 34
    CONTAINS_TEXT_1 = (By.XPATH, u'//button[contains(text(),"1")]') # x: 342 y: 630 width: 34 height: 34
    ID_RETAILER_CONTENT_FLOATED = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[5]/DIV[1]/DIV[1]/BUTTON[3]') # x: 376 y: 630 width: 34 height: 34
    CONTAINS_TEXT = (By.XPATH, u'//span[contains(text(),"«")]') # x: 321 y: 639 width: 8 height: 16

    # Dynamic objects:
    BODY = (By.XPATH, u'//BODY/DIV[1]/DIV[3]/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[4]/TABLE[1]/TBODY[1]/TR[1]/TD[10]/DIV[1]/A[1]')     # x: 1303 y: 129 width: 71 height: 30 # Dynamic object
    total_549_e = (By.XPATH, u'//span[contains(text(),"€549.00")]')     # x: 697 y: 472 width: 56 height: 18 # Dynamic object
    reg_kodin_terra_jkl = (By.XPATH, u'//td[9]/a')     # x: 1223 y: 453 width: 73 height: 56 # Dynamic object
    ref_cust_name = (By.XPATH, u'//div[3]/div/input')     # x: 413 y: 287 width: 180 height: 34 # Dynamic object
    descending = (By.XPATH, u'//button[2]')     # x: 1329 y: 352 width: 89 height: 30 # Dynamic object
    ascending = (By.XPATH, u'//span/button')     # x: 1251 y: 352 width: 80 height: 30 # Dynamic object
    creator_list = (By.XPATH, u'//div[4]/select')     # x: 1042 y: 352 width: 180 height: 34 # Dynamic object


    def wait_for_visible_reg_kodin_terra_jkl_linkki(self):
        self.wait_for_visible(self.reg_kodin_terra_jkl)

    def type_ref_cust_name(self, parameters=None):
        self.type(self.ref_cust_name, parameters)

    def click_descending(self):
        self.click(self.descending)

    def click_ascending(self):
        self.click(self.ascending)

    def wait_for_visible_ascending(self):
        self.wait_for_visible(self.ascending)

    def select_text_from_dropdown_list_creator_list(self, parameters=None):
        self.select_text_from_dropdown_list(self.creator_list, parameters)

    def select_value_from_dropdown_list_creator_list(self, parameters=None):
        self.select_value_from_dropdown_list(self.creator_list, parameters)

    def click_creator_list(self):
        self.click(self.creator_list)
