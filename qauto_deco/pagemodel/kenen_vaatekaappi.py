# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Kenen_vaatekaappi(CommonUtils):
    # Pagemodel timestamp: 20160209090547
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
    CONTAINS_TEXT_KYSYMYS_2 = (By.XPATH, u'//p[contains(text(),"Kysymys 2/2")]') # x: 96 y: 90 width: 1752 height: 20
    BODY_MIES = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]') # x: 96 y: 304 width: 438 height: 428
    BODY_NAINEN = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[2]/DIV[2]/DIV[2]') # x: 534 y: 304 width: 438 height: 428
    BODY_PARI = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[2]/DIV[2]/DIV[3]') # x: 972 y: 304 width: 438 height: 428
    BODY_PERHE = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[2]/DIV[2]/DIV[4]') # x: 1410 y: 304 width: 438 height: 428
    CLASS_DISABLE_ELEMENT = (By.CLASS_NAME, u'disable-element') # x: 0 y: 766 width: 192 height: 68

    # Dynamic objects:
    CLASS_ELEMENT_ENABLE = (By.CLASS_NAME, u'element-enable')     # x: 1632 y: 782 width: 288 height: 68 # Dynamic object

    def valitse_omistaja(self, parameters=None):
        if parameters['omistaja'] == "mies":
            self.click_element(self.BODY_MIES)
        elif parameters['omistaja'] == "nainen":
             self.click_element(self.BODY_NAINEN)
        elif parameters['omistaja'] == "pari":
             self.click_element(self.BODY_PARI)
        elif parameters['omistaja'] == "perhe":
             self.click_element(self.BODY_PERHE)
        else:
            self.click_element(self.BODY_MIES)

    def click_seuraava_vaihe(self, parameters=None):
        self.click_element(self.CLASS_ELEMENT_ENABLE)
