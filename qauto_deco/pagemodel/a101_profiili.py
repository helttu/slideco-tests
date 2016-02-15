# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class A101_profiili(CommonUtils):
    # Pagemodel timestamp: 20160121141809
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
    CLASS_TAB_PROFILE_GROUP = (By.CLASS_NAME, u'tab-profile-group') # x: 1232 y: 0 width: 184 height: 62
    CLASS_TAB_ENABLED_2 = (By.CLASS_NAME, u'tab-enabled-2') # x: 1416 y: 0 width: 184 height: 62
    CONTENT_PROFILE_OPTIONS_STYLE_VALITSE_MIELEISESI_PROFIILIS_VY = (By.CSS_SELECTOR, u'.content-profile-options>.style-header>h2') # x: 1240 y: 80 width: 352 height: 28
    ALT_PANELPROFILE_GLOSS_WHITE_A101 = (By.CSS_SELECTOR, u'img[alt="panelprofile_gloss_white_a101"]') # x: 1246 y: 136 width: 69 height: 69
    CONTENT_PROFILE_OPTIONS_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT = (By.CSS_SELECTOR, u'.content-profile-options>.style-container-list>div.style.data-set-save-data-bint>div.style-label') # x: 1322 y: 152 width: 272 height: 33
    ALT_PANELPROFILE_BRUSHED_SILVER_A101 = (By.CSS_SELECTOR, u'img[alt="panelprofile_brushed_silver_a101"]') # x: 1246 y: 233 width: 69 height: 69
    ALT_PANELPROFILE_ANODISED_SILVER_A101 = (By.CSS_SELECTOR, u'img[alt="panelprofile_anodised_silver_a101"]') # x: 1246 y: 329 width: 69 height: 69
    ALT_PANELPROFILE_ANODISED_OLIVE_A101 = (By.CSS_SELECTOR, u'img[alt="panelprofile_anodised_olive_a101"]') # x: 1246 y: 426 width: 69 height: 69
    ALT_PANELPROFILE_SATIN_BLACK_A101 = (By.CSS_SELECTOR, u'img[alt="panelprofile_satin_black_a101"]') # x: 1246 y: 522 width: 69 height: 69
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22

    def valitse_profiili_materiaali(self, parameters=None):
        if parameters[u'a101_materiaalit'] == u'valkea':
            self.click_element(self.ALT_PANELPROFILE_GLOSS_WHITE_A101)
        elif parameters[u'a101_materiaalit'] == u'harjattu_alumiini':
            self.click_element(self.ALT_PANELPROFILE_BRUSHED_SILVER_A101)
        elif parameters[u'a101_materiaalit'] == u'alumiini':
            self.click_element(self.ALT_PANELPROFILE_ANODISED_SILVER_A101)
        elif parameters[u'a101_materiaalit'] == u'shampanja':
            self.click_element(self.ALT_PANELPROFILE_ANODISED_OLIVE_A101)
        else:
            self.click_element(self.ALT_PANELPROFILE_GLOSS_WHITE_A101)
