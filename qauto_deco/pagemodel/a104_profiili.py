# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class A104_profiili(CommonUtils):
    # Pagemodel timestamp: 20160121142456
    # Pagemodel url: http://finndeco.codemen.fi/build/?api=K3JK2FCG
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
    CLASS_TAB_PROFILE_GROUP = (By.CLASS_NAME, u'tab-profile-group') # x: 1232 y: 0 width: 184 height: 62
    CLASS_TAB_ENABLED_2 = (By.CLASS_NAME, u'tab-enabled-2') # x: 1416 y: 0 width: 184 height: 62
    CONTENT_PROFILE_OPTIONS_STYLE_VALITSE_MIELEISESI_PROFIILIS_VY = (By.CSS_SELECTOR, u'.content-profile-options>.style-header>h2') # x: 1240 y: 80 width: 352 height: 28
    ALT_PANELPROFILE_GLOSS_WHITE_A104 = (By.CSS_SELECTOR, u'img[alt="panelprofile_gloss_white_a104"]') # x: 1246 y: 136 width: 69 height: 69
    CONTENT_PROFILE_OPTIONS_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT = (By.CSS_SELECTOR, u'.content-profile-options>.style-container-list>div.style.data-set-save-data-bint>div.style-label') # x: 1322 y: 152 width: 272 height: 33
    ALT_PANELPROFILE_ANODISED_SILVER_A104 = (By.CSS_SELECTOR, u'img[alt="panelprofile_anodised_silver_a104"]') # x: 1246 y: 233 width: 69 height: 69
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22
    MEASURE_TITLE_MITTAA_JA_RAKENNA = (By.CSS_SELECTOR, u'.section-measure>.section-title>span') # x: 0 y: 694 width: 533 height: 23
    DESIGN_TITLE_LIUKUOVIEN_SUUNNITTELU = (By.CSS_SELECTOR, u'.section-design>.section-title>span') # x: 533 y: 694 width: 533 height: 23
    SAVE_TITLE_TALLENNUS_JA_YHTEYDENOTTO = (By.CSS_SELECTOR, u'.section-save>.section-title>span') # x: 1067 y: 694 width: 533 height: 23
    CRUMB_1_ACTIVE = (By.CSS_SELECTOR, u'div.crumb.crumb-1.active') # x: 100 y: 754 width: 19 height: 19
    CRUMB_2_ACTIVE = (By.CSS_SELECTOR, u'div.crumb.crumb-2.active') # x: 180 y: 754 width: 19 height: 19
    CLASS_CURRENT = (By.CLASS_NAME, u'current') # x: 260 y: 754 width: 19 height: 19
    CLASS_CRUMB_4 = (By.CLASS_NAME, u'crumb-4') # x: 342 y: 757 width: 13 height: 13
    CLASS_CRUMB_5 = (By.CLASS_NAME, u'crumb-5') # x: 422 y: 757 width: 13 height: 13
    DESIGN_CRUMB_THREEWAY_1 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-1') # x: 636 y: 757 width: 13 height: 13
    DESIGN_CRUMB_THREEWAY_2 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-2') # x: 796 y: 757 width: 13 height: 13
    DESIGN_CRUMB_THREEWAY_3 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-3') # x: 956 y: 757 width: 13 height: 13
    SAVE_CRUMB_THREEWAY_1 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-1') # x: 1169 y: 757 width: 13 height: 13
    SAVE_CRUMB_THREEWAY_2 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-2') # x: 1329 y: 757 width: 13 height: 13
    SAVE_CRUMB_THREEWAY_3 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-3') # x: 1489 y: 757 width: 13 height: 13
    LINE_1_ACTIVE = (By.CSS_SELECTOR, u'div.line.line-1.active') # x: 107 y: 761 width: 80 height: 1
    LINE_2_ACTIVE = (By.CSS_SELECTOR, u'div.line.line-2.active') # x: 187 y: 761 width: 80 height: 1
    CLASS_LINE_3 = (By.CLASS_NAME, u'line-3') # x: 267 y: 761 width: 80 height: 1
    CLASS_LINE_4 = (By.CLASS_NAME, u'line-4') # x: 347 y: 761 width: 80 height: 1
    DESIGN_CRUMB_THREEWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.line-1') # x: 640 y: 761 width: 160 height: 1
    DESIGN_CRUMB_THREEWAY_LINE_2 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.line-2') # x: 800 y: 761 width: 160 height: 1
    SAVE_CRUMB_THREEWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.line-1') # x: 1173 y: 761 width: 160 height: 1
    SAVE_CRUMB_THREEWAY_LINE_2 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.line-2') # x: 1333 y: 761 width: 160 height: 1

    def valitse_profiili_materiaali(self, parameters=None):
        if parameters[u'a104_materiaalit'] == u'valkea':
            self.click_element(self.ALT_PANELPROFILE_GLOSS_WHITE_A104)
        elif parameters[u'a104_materiaalit'] == u'alumiini':
            self.click_element(self.ALT_PANELPROFILE_ANODISED_SILVER_A104)
        else:
            self.click_element(self.ALT_PANELPROFILE_GLOSS_WHITE_A104)
