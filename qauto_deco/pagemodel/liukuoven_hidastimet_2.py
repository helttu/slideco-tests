# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Liukuoven_hidastimet_2(CommonUtils):
    # Pagemodel timestamp: 20160215113656
    # Pagemodel url: http://finndeco.codemen.fi/build/?api=K3JK2FCG
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1920, 1080)
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
    # Pagemodel type: dynamic
    # Links found: 0
    # Page model constants:
    CONTENT_PROFILE_EXTRAS_STYLE_LIUKUOVEN_HIDASTIMET = (By.CSS_SELECTOR, u'.content-profile-extras>.style-header>h2') # x: 1486 y: 95 width: 426 height: 28
    CONTENT_PROFILE_EXTRAS_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT = (By.CSS_SELECTOR, u'.content-profile-extras>.style-container-list>div.style.data-set-save-data-bint>.selection-checked>.icon') # x: 1488 y: 151 width: 426 height: 80
    BODY_VAKIO = (By.XPATH, u'//BODY/SECTION[10]/DIV[2]/DIV[3]/DIV[2]/DIV[2]') # x: 1486 y: 245 width: 430 height: 84
    CONTROL_CHECKBOX_LIUKUOVEN_HARJANAUHAT = (By.CSS_SELECTOR, u'.control-checkbox>label') # x: 1486 y: 721 width: 426 height: 37
    CLASS_CUSTOM_CHECKBOX = (By.CLASS_NAME, u'custom-checkbox') # x: 1492 y: 731 width: 20 height: 20
    CLASS_DISABLE_ELEMENT = (By.CLASS_NAME, u'disable-element') # x: 0 y: 766 width: 192 height: 68
    CLASS_ELEMENT_ENABLE = (By.CLASS_NAME, u'element-enable') # x: 1632 y: 766 width: 288 height: 68

    def click_seuraava_vaihe(self, parameters=None):
        self.click_element(self.CLASS_ELEMENT_ENABLE)

    def valitse_hidastimet(self, parameters=None):
        if parameters[u'hidastimet'] == u'ei_valintaa':
            self.click_element(self.CONTENT_PROFILE_EXTRAS_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT)
        elif parameters[u'hidastimet'] == u'vakio':
            self.click_element(self.BODY_VAKIO)
        else:
            self.click_element(self.CONTENT_PROFILE_EXTRAS_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT)
