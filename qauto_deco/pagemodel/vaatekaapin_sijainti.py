# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Vaatekaapin_sijainti(CommonUtils):
    # Pagemodel timestamp: 20160209083613
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

    # Dynamic objects:
    BODY_MAKUUHUONE = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]')     # x: 96 y: 320 width: 584 height: 428 # Dynamic object
    BODY_KODINHOITOHUONE = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[2]')     # x: 680 y: 320 width: 584 height: 428 # Dynamic object
    BODY_ETEINEN = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[3]')     # x: 1264 y: 320 width: 584 height: 428 # Dynamic object
    CLASS_ELEMENT_ENABLE = (By.CLASS_NAME, u'element-enable')     # x: 1632 y: 782 width: 288 height: 68 # Dynamic object
    CLASS_DISABLE_ELEMENT = (By.CLASS_NAME, u'disable-element')     # x: 0 y: 782 width: 192 height: 68 # Dynamic object
    CONTAINS_TEXT_KYSYMYS_1_2 = (By.XPATH, u'//p[contains(text(),"Kysymys 1/2")]')     # x: 96 y: 90 width: 1752 height: 20 # Dynamic object

    def valitse_sijainti(self, parameters=None):
        if parameters['huone'] == "makuuhuone":
            self.click_element(self.BODY_MAKUUHUONE)
        elif parameters['huone'] == "kodinhoitohuone":
             self.click_element(self.BODY_KODINHOITOHUONE)
        elif parameters['huone'] == "eteinen":
             self.click_element(self.BODY_ETEINEN)
        else:
            self.click_element(self.BODY_MAKUUHUONE)

    def click_seuraava_vaihe(self, parameters=None):
        self.click_element(self.CLASS_ELEMENT_ENABLE)
