# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Jakolistat(CommonUtils):
    # Pagemodel timestamp: 20160121151134
    # Pagemodel url: http://finndeco.codemen.fi/build/?api=K3JK2FCG
    # Pagemodel area: (0, 0, 1600, 690)
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
    CLASS_TAB_SEPARATORS_LAYOUT = (By.CLASS_NAME, u'tab-separators-layout') # x: 1232 y: 0 width: 184 height: 62
    CLASS_TAB_SEPARATORS_CUSTOM = (By.CLASS_NAME, u'tab-separators-custom') # x: 1416 y: 0 width: 184 height: 62
    CONTENT_SEPARATORS_CUSTOM_STYLE_LIS_POISTA_TAI_D_JAKOLISTOJA_MIELESI = (By.CSS_SELECTOR, u'.content-separators-custom>.style-header>h2') # x: 1240 y: 80 width: 352 height: 56
    CLASS_NUM = (By.CLASS_NAME, u'num') # x: 1246 y: 172 width: 90 height: 28
    CLASS_SIZE = (By.CLASS_NAME, u'size') # x: 1336 y: 172 width: 168 height: 28
    CLASS_ADD_SEPARATOR = (By.CLASS_NAME, u'add-separator') # x: 1240 y: 242 width: 335 height: 32
    CONTENT_SEPARATORS_CUSTOM_STYLE_CONTROL_CHECKBOX = (By.CSS_SELECTOR, u'.content-separators-custom>.style-footer>.control-checkbox>label>.custom-checkbox') # x: 1246 y: 589 width: 20 height: 20
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22

    def valitse_seuraava_vaihe(self, parameters=None):
        self.click(self.ELEMENT_ENABLE_SEURAAVA_VAIHE)
