# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Oven_mitat_alert(CommonUtils):
    # Pagemodel timestamp: 20160215133906
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
    BODY_OVEN_MITAT = (By.XPATH, u'//BODY/SECTION[4]/DIV[7]/DIV[2]/H2[1]') # x: 735 y: 254 width: 450 height: 45
    CLASS_CONFIRM = (By.CLASS_NAME, u'confirm') # x: 798 y: 489 width: 160 height: 48
    CLASS_CANCEL = (By.CLASS_NAME, u'cancel') # x: 962 y: 489 width: 160 height: 48

    def click_ok(self, parameters=None):
        self.click_element(self.CLASS_CONFIRM)
