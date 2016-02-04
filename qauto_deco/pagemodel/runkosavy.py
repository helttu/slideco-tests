# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Runkosavy(CommonUtils):
    # Pagemodel timestamp: 20160201103506
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
    CONTENT_FURNITURE_COLOUR_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT = (By.CSS_SELECTOR, u'.content-furniture-colour>.style-container-list>div.style.data-set-save-data-bint>.selection-checked>.icon') # x: 1488 y: 151 width: 409 height: 80
    BODY_VALKEA_LINE = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[2]') # x: 1486 y: 245 width: 413 height: 84
    BODY_HARMAA = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[3]') # x: 1486 y: 342 width: 413 height: 84
    BODY_ANTRASIITTI = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[4]') # x: 1486 y: 438 width: 413 height: 84
    BODY_RUSKEA_LINE = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[5]') # x: 1486 y: 535 width: 413 height: 84
    BODY_TUMMA_PAHKINA = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[6]') # x: 1486 y: 631 width: 413 height: 84
    BODY_HKIN = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[7]') # x: 1486 y: 728 width: 413 height: 84
    CLASS_DISABLE_ELEMENT = (By.CLASS_NAME, u'disable-element') # x: 0 y: 766 width: 192 height: 68
    CLASS_ELEMENT_RESTART = (By.CLASS_NAME, u'element-restart') # x: 288 y: 766 width: 288 height: 68
    CLASS_ELEMENT_ENABLE = (By.CLASS_NAME, u'element-enable') # x: 1632 y: 766 width: 288 height: 68
    BODY_TAMMI = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[8]') # x: 1486 y: 824 width: 413 height: 84
    BODY_PY_KKI = (By.XPATH, u'//BODY/SECTION[14]/DIV[2]/DIV[2]/DIV[2]/DIV[9]') # x: 1486 y: 921 width: 413 height: 84

    def select_runkosavy(self, parameters=None):
        if parameters['runkosavy'] == 'valkea':
            self.click(self.CONTENT_FURNITURE_COLOUR_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT)
        elif parameters['runkosavy'] == 'valkealine':
            self.click(self.BODY_VALKEA_LINE)
        elif parameters['runkosavy'] == 'harmaa':
            self.click(self.BODY_HARMAA)
        elif parameters['runkosavy'] == 'antrasiitti':
            self.click(self.BODY_ANTRASIITTI)
        elif parameters['runkosavy'] == 'ruskealine':
            self.click(self.BODY_RUSKEA_LINE)
        elif parameters['runkosavy'] == 'tumma_pahkina':
            self.click(self.BODY_TUMMA_PAHKINA)
        elif parameters['runkosavy'] == 'pahkina':
            self.click(self.BODY_HKIN)
        elif parameters['runkosavy'] == 'tammi':
            self.click(self.BODY_TAMMI)
        elif parameters['runkosavy'] == 'pyokki':
            self.click(self.BODY_PY_KKI)
        else:
            self.click(self.CONTENT_FURNITURE_COLOUR_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT)

    def click_seuraava_vaihe(self, parameters=None):
        self.click(self.CLASS_ELEMENT_ENABLE)
