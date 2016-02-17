# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Runkoosat(CommonUtils):
    # Pagemodel timestamp: 20160121144918
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
    CLASS_TAB_FRAME_SHAPE = (By.CLASS_NAME, u'tab-frame-shape') # x: 1232 y: 0 width: 368 height: 62
    CONTENT_SHAPE_STYLE_RUNKO_OSAT = (By.CSS_SELECTOR, u'.content-frame-shape>.style-header>h2') # x: 1240 y: 80 width: 352 height: 28
    OUTER_OPTIONS_CONTROL_CHECKBOX_CUSTOM = (By.CSS_SELECTOR, u'.outer-frame-options>div.control-checkbox>label>label.custom-checkbox') # x: 1246 y: 144 width: 20 height: 20
    CLOSED_ENDS_CONTROL_CHECKBOX_CUSTOM = (By.CSS_SELECTOR, u'.closed-ends>div.control-checkbox>label>label.custom-checkbox') # x: 1246 y: 500 width: 20 height: 20
    ID_SET_WARDROBE_DEPTH = (By.ID, u'set-wardrobe-depth') # x: 1240 y: 583 width: 352 height: 32
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22

    # Dynamic objects:
    KATTOLEVY = (By.XPATH, u'//BODY/SECTION[11]/DIV[2]/DIV[1]/DIV[2]/DIV[1]/DIV[1]/LABEL[1]/LABEL[1]')     # x: 1246 y: 144 width: 20 height: 20 # Dynamic object
    POHJALEVY = (By.XPATH, u'//BODY/SECTION[11]/DIV[2]/DIV[1]/DIV[2]/DIV[1]/DIV[2]/LABEL[1]/LABEL[1]')     # x: 1246 y: 181 width: 20 height: 20 # Dynamic object
    POHJALEVY_JA_SOKKELI = (By.XPATH, u'//BODY/SECTION[11]/DIV[2]/DIV[1]/DIV[2]/DIV[1]/DIV[3]/LABEL[1]/LABEL[1]')     # x: 1246 y: 217 width: 20 height: 20 # Dynamic object
    VAIN_PEITELEVYT = (By.XPATH, u'//BODY/SECTION[11]/DIV[2]/DIV[1]/DIV[2]/DIV[1]/DIV[4]/LABEL[1]/LABEL[1]')     # x: 1246 y: 254 width: 20 height: 20 # Dynamic object

    def valitse_runkoosat(self, parameters=None):
        if parameters['kattolevy'] == "true":
            self.click_element(self.KATTOLEVY)
        else:
            print ""

    def click_seuraava_vaihe(self, parameters=None):
        self.click_element(self.ELEMENT_ENABLE_SEURAAVA_VAIHE)
