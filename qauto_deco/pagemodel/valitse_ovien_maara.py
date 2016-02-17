# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Valitse_ovien_maara(CommonUtils):
    # Pagemodel timestamp: 20160121131007
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
    CLASS_TAB_ENABLED_1 = (By.CLASS_NAME, u'tab-enabled-1') # x: 1232 y: 0 width: 368 height: 62
    CONTENT_DOOR_COUNT_STYLE_VALITSE_LIUKUOVIEN_R = (By.CSS_SELECTOR, u'.content-door-count>.style-header>h2') # x: 1240 y: 80 width: 352 height: 28
    UNKNOWN = (By.CSS_SELECTOR, u'br') # x: 1240 y: 134 width: 0 height: 20
    STYLE_DOORCOUNT_3_DOORICON = (By.CSS_SELECTOR, u'.style-doorcount-3>div.dooricon') # x: 1246 y: 180 width: 26 height: 62
    CLASS_BG = (By.CLASS_NAME, u'bg') # x: 1240 y: 256 width: 72 height: 74
    CLASS_ICON = (By.CLASS_NAME, u'icon') # x: 1240 y: 256 width: 72 height: 74
    STYLE_DOORCOUNT_2_DOORICON = (By.CSS_SELECTOR, u'.style-doorcount-2>div.dooricon') # x: 1246 y: 262 width: 26 height: 62
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22

    # Dynamic objects:
    CLASS_ICON = (By.CLASS_NAME, u'icon')     # x: 1240 y: 256 width: 72 height: 74 # Dynamic object
    CLASS_STYLE_DOORCOUNT_3 = (By.CLASS_NAME, u'style-doorcount-3')     # x: 1240 y: 174 width: 106 height: 74 # Dynamic object

    def valitse_ovien_maara(self, parameters=None):
        if parameters['ovien_maara'] == 2:
            self.click_element(self.CLASS_ICON)
        elif parameters['ovien_maara'] == 3:
            self.click_element(self.CLASS_STYLE_DOORCOUNT_3)
        else:
            self.click_element(self.CLASS_ICON)

    def click_seuraava_vaihe(self):
        self.click_element(self.ELEMENT_ENABLE_SEURAAVA_VAIHE)
