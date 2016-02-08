# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Kauppias_account(CommonUtils):
    # Pagemodel timestamp: 20160128113704
    # Pagemodel url: http://finndeco.codemen.fi/manage/#/dash/managers/207
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
    EMBER857_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember857>.glyphicon-user') # x: 1162 y: 18 width: 12 height: 12
    EMBER942_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember942>.glyphicon-briefcase') # x: 1258 y: 18 width: 12 height: 12
    CLASS_GLYPHICON_QUESTION_SIGN = (By.CLASS_NAME, u'glyphicon-question-sign') # x: 1444 y: 18 width: 12 height: 12
    EMBER757_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember757>.glyphicon-log-out') # x: 1477 y: 18 width: 12 height: 12
    CLASS_LOGO_MAIN = (By.CLASS_NAME, u'logo-main') # x: 80 y: 20 width: 100 height: 100
    CLASS_NOTIFICATION = (By.CLASS_NAME, u'notification') # x: 180 y: 30 width: 4 height: 4
    GLYPHICON_USER = (By.CSS_SELECTOR, u'h1>.glyphicon-user') # x: 467 y: 104 width: 36 height: 36
    CONTACT_CARD = (By.LINK_TEXT, u'Contact Card') # x: 702 y: 155 width: 116 height: 42
    CLASS_GLYPHICON_DASHBOARD = (By.CLASS_NAME, u'glyphicon-dashboard') # x: 32 y: 166 width: 14 height: 14
    CLASS_GLYPHICON_PENCIL = (By.CLASS_NAME, u'glyphicon-pencil') # x: 836 y: 168 width: 14 height: 14
    CLASS_GLYPHICON_SHOPPING_CART = (By.CLASS_NAME, u'glyphicon-shopping-cart') # x: 32 y: 202 width: 14 height: 14
    CLASS_IMG_CIRCLE = (By.CLASS_NAME, u'img-circle') # x: 715 y: 225 width: 128 height: 128
    CLASS_GLYPHICON_TH = (By.CLASS_NAME, u'glyphicon-th') # x: 32 y: 238 width: 14 height: 14
    CLASS_GLYPHICON_PLANE = (By.CLASS_NAME, u'glyphicon-plane') # x: 987 y: 242 width: 24 height: 24
    CLASS_GLYPHICON_CERTIFICATE = (By.CLASS_NAME, u'glyphicon-certificate') # x: 32 y: 274 width: 14 height: 14
    CONTAINS_TEXT_UK_ENGLISH = (By.XPATH, u'//button[contains(text(),"UK English")]') # x: 893 y: 278 width: 124 height: 46
    CONTAINS_TEXT_SUOMI = (By.XPATH, u'//button[contains(text(),"Suomi")]') # x: 1020 y: 278 width: 85 height: 46
    EMBER1046_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember1046>.glyphicon-briefcase') # x: 32 y: 310 width: 14 height: 14
    CLASS_GLYPHICON_GBP = (By.CLASS_NAME, u'glyphicon-gbp') # x: 32 y: 346 width: 14 height: 14
    EMBER1070_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember1070>.glyphicon-user') # x: 32 y: 382 width: 14 height: 14
    GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'h2>.glyphicon-briefcase') # x: 707 y: 409 width: 30 height: 30
    CLASS_GLYPHICON_COG = (By.CLASS_NAME, u'glyphicon-cog') # x: 32 y: 418 width: 14 height: 14
    RETAILER_SIDEBAR = (By.CSS_SELECTOR, u'#retailer-sidebar>hr') # x: 0 y: 464 width: 260 height: 2
    ID_EMBER1099 = (By.ID, u'ember1099') # x: 716 y: 465 width: 76 height: 16
    EMBER770_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember770>.glyphicon-user') # x: 32 y: 496 width: 14 height: 14
    ID_EMBER1105 = (By.ID, u'ember1105') # x: 716 y: 507 width: 64 height: 16
    EMBER1224 = (By.CSS_SELECTOR, u'#ember1224>.img') # x: 829 y: 511 width: 16 height: 16
    EMBER1227 = (By.CSS_SELECTOR, u'#ember1227>.img') # x: 860 y: 511 width: 16 height: 16
    EMBER1230 = (By.CSS_SELECTOR, u'#ember1230>.img') # x: 891 y: 511 width: 16 height: 16
    EMBER1233 = (By.CSS_SELECTOR, u'#ember1233>.img') # x: 1002 y: 511 width: 16 height: 16
    EMBER1236 = (By.CSS_SELECTOR, u'#ember1236>.img') # x: 1033 y: 511 width: 16 height: 16
    EMBER1239 = (By.CSS_SELECTOR, u'#ember1239>.img') # x: 1064 y: 511 width: 16 height: 16
    EMBER772_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember772>.glyphicon-log-out') # x: 32 y: 532 width: 14 height: 14
    EMBER1242 = (By.CSS_SELECTOR, u'#ember1242>.img') # x: 829 y: 536 width: 16 height: 16
    EMBER1245 = (By.CSS_SELECTOR, u'#ember1245>.img') # x: 945 y: 536 width: 16 height: 16
    EMBER1248 = (By.CSS_SELECTOR, u'#ember1248>.img') # x: 1056 y: 536 width: 16 height: 16
    EMBER1251 = (By.CSS_SELECTOR, u'#ember1251>.img') # x: 1087 y: 536 width: 16 height: 16
    EMBER1254 = (By.CSS_SELECTOR, u'#ember1254>.img') # x: 829 y: 561 width: 16 height: 16
    EMBER1257 = (By.CSS_SELECTOR, u'#ember1257>.img') # x: 860 y: 561 width: 16 height: 16
    EMBER1260 = (By.CSS_SELECTOR, u'#ember1260>.img') # x: 891 y: 561 width: 16 height: 16
    EMBER1263 = (By.CSS_SELECTOR, u'#ember1263>.img') # x: 922 y: 561 width: 16 height: 16
    EMBER1266 = (By.CSS_SELECTOR, u'#ember1266>.img') # x: 829 y: 586 width: 16 height: 16
    EMBER1269 = (By.CSS_SELECTOR, u'#ember1269>.img') # x: 962 y: 586 width: 16 height: 16
    EMBER1272 = (By.CSS_SELECTOR, u'#ember1272>.img') # x: 829 y: 611 width: 16 height: 16
    EMBER1275 = (By.CSS_SELECTOR, u'#ember1275>.img') # x: 946 y: 611 width: 16 height: 16
    EMBER1278 = (By.CSS_SELECTOR, u'#ember1278>.img') # x: 829 y: 636 width: 16 height: 16
    EMBER1281 = (By.CSS_SELECTOR, u'#ember1281>.img') # x: 946 y: 636 width: 16 height: 16
    EMBER1284 = (By.CSS_SELECTOR, u'#ember1284>.img') # x: 829 y: 661 width: 16 height: 16
    EMBER1287 = (By.CSS_SELECTOR, u'#ember1287>.img') # x: 920 y: 661 width: 16 height: 16
    ID_EMBER1130 = (By.ID, u'ember1130') # x: 716 y: 699 width: 56 height: 16
    ID_EMBER1140 = (By.ID, u'ember1140') # x: 716 y: 789 width: 145 height: 34

    # Dynamic objects:
    TRACK_ORDERS = (By.LINK_TEXT, u'Track orders')     # x: 0 y: 192 width: 260 height: 36 # Dynamic object

    def klikkaa_track_orders(self):
        self.click_element(self.TRACK_ORDERS)
