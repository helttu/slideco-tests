# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Kauppias_login(CommonUtils):
    # Pagemodel timestamp: 20160128111051
    # Pagemodel url: http://finndeco.codemen.fi/manage/
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
    # Links found: 0
    # Page model constants:
    CLASS_LOGO_PRIMARY = (By.CLASS_NAME, u'logo-primary') # x: 736 y: 251 width: 128 height: 128
    CLASS_LOGO_SECONDARY = (By.CLASS_NAME, u'logo-secondary') # x: 736 y: 251 width: 128 height: 128
    CLASS_LOGO_EFFECT = (By.CLASS_NAME, u'logo-effect') # x: 736 y: 251 width: 128 height: 128
    ID_EMBER607 = (By.ID, u'ember607') # x: 702 y: 411 width: 196 height: 35
    CLASS_PHOTO = (By.CLASS_NAME, u'photo') # x: 864 y: 413 width: 32 height: 32
    ID_EMBER609 = (By.ID, u'ember609') # x: 702 y: 461 width: 196 height: 35
    CLASS_BTN_DEFAULT = (By.CLASS_NAME, u'btn-default') # x: 750 y: 529 width: 100 height: 34
    CLASS_GLYPHICON_LOG_IN = (By.CLASS_NAME, u'glyphicon-log-in') # x: 793 y: 538 width: 14 height: 14

    # Dynamic objects:
    username_field = (By.XPATH, u'//BODY/DIV[1]/DIV[1]/FORM[1]/DIV[1]/INPUT[1]')     # x: 702 y: 407 width: 196 height: 35 # Dynamic object
    password_field = (By.XPATH, u'//BODY/DIV[1]/DIV[1]/FORM[1]/DIV[2]/INPUT[1]')     # x: 702 y: 457 width: 196 height: 35 # Dynamic object
    login_button = (By.XPATH, u'//BODY/DIV[1]/DIV[1]/FORM[1]/BUTTON[1]')     # x: 750 y: 525 width: 100 height: 34 # Dynamic object

    def input_text_username_field(self, parameters=None):
        self.input_text(self.username_field, parameters)

    def input_text_password_field(self, parameters=None):
        self.input_text(self.password_field, parameters)

    def click_element_login_button(self):
        self.click_element(self.login_button)
        self.input_text(self.ID_EMBER609, parameters)
