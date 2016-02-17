# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class S300_profiili(CommonUtils):
    # Pagemodel timestamp: 20160216132957
    # Pagemodel url: http://finndeco.codemen.fi/build/?api=K3JK2FCG
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1920, 1080)
    # Use project settings: True
    # Used filters: default
    # Depth of css path: 9
    # Minimize css selector: True
    # Create automated methods: True
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
    CLASS_TAB_PROFILE_GROUP = (By.CLASS_NAME, u'tab-profile-group') # x: 1478 y: 0 width: 221 height: 77, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CLASS_TAB_ENABLED_2 = (By.CLASS_NAME, u'tab-enabled-2') # x: 1699 y: 0 width: 221 height: 77, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CONTENT_PROFILE_OPTIONS_STYLE_VALITSE_MIELEISESI_PROFIILIS_VY = (By.CSS_SELECTOR, u'.content-profile-options>.style-header>h2') # x: 1486 y: 95 width: 426 height: 28, tag: h2, type: , name: None, form_id: , checkbox: ,href: 
    ALT_PANELPROFILE_WHITE = (By.CSS_SELECTOR, u'img[alt="panelprofile_white"]') # x: 1492 y: 151 width: 69 height: 69, tag: img, type: , name: None, form_id: , checkbox: ,href: None
    CONTENT_PROFILE_OPTIONS_STYLE_CONTAINER_LIST_DATA_SET_SAVE_BINT = (By.CSS_SELECTOR, u'.content-profile-options>.style-container-list>div.style.data-set-save-data-bint>div.style-label') # x: 1568 y: 167 width: 346 height: 33, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    ALT_PANELPROFILE_SILVER = (By.CSS_SELECTOR, u'img[alt="panelprofile_silver"]') # x: 1492 y: 247 width: 69 height: 69, tag: img, type: , name: None, form_id: , checkbox: ,href: None
    ALT_PANELPROFILE_SATIN_GOLD = (By.CSS_SELECTOR, u'img[alt="panelprofile_satin_gold"]') # x: 1492 y: 344 width: 69 height: 69, tag: img, type: , name: None, form_id: , checkbox: ,href: None
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 785 width: 192 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 192 y: 785 width: 96 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 288 y: 785 width: 288 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1632 y: 785 width: 288 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    MAIN_CONTAINER_CURRENCY = (By.CSS_SELECTOR, u'.main-container>.currency') # x: 1410 y: 788 width: 9 height: 22, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1425 y: 788 width: 61 height: 22, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    MEASURE_TITLE_MITTAA_JA_RAKENNA = (By.CSS_SELECTOR, u'.section-measure>.section-title>span') # x: 0 y: 855 width: 480 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    DESIGN_TITLE_LIUKUOVIEN_SUUNNITTELU = (By.CSS_SELECTOR, u'.section-design>.section-title>span') # x: 480 y: 855 width: 480 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    STRUCTURE_TITLE_RUNGON_SUUNNITTELU = (By.CSS_SELECTOR, u'.section-structure>.section-title>span') # x: 960 y: 855 width: 480 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    SAVE_TITLE_TALLENNUS_JA_YHTEYDENOTTO = (By.CSS_SELECTOR, u'.section-save>.section-title>span') # x: 1440 y: 855 width: 480 height: 23, tag: span, type: , name: None, form_id: , checkbox: ,href: None
    CRUMB_1_ACTIVE = (By.CSS_SELECTOR, u'div.crumb.crumb-1.active') # x: 89 y: 928 width: 19 height: 19, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CRUMB_2_ACTIVE = (By.CSS_SELECTOR, u'div.crumb.crumb-2.active') # x: 161 y: 928 width: 19 height: 19, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CLASS_CURRENT = (By.CLASS_NAME, u'current') # x: 236 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CLASS_CRUMB_4 = (By.CLASS_NAME, u'crumb-4') # x: 308 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CLASS_CRUMB_5 = (By.CLASS_NAME, u'crumb-5') # x: 380 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    DESIGN_CRUMB_THREEWAY_1 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-1') # x: 572 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    DESIGN_CRUMB_THREEWAY_2 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-2') # x: 716 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    DESIGN_CRUMB_THREEWAY_3 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-3') # x: 860 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CRUMB_TWOWAY_1 = (By.CSS_SELECTOR, u'.section-crumb-twoway>.crumb-1') # x: 1052 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CRUMB_TWOWAY_2 = (By.CSS_SELECTOR, u'.section-crumb-twoway>.crumb-2') # x: 1340 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    SAVE_CRUMB_THREEWAY_1 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-1') # x: 1532 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    SAVE_CRUMB_THREEWAY_2 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-2') # x: 1676 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    SAVE_CRUMB_THREEWAY_3 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-3') # x: 1820 y: 931 width: 13 height: 13, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    LINE_1_ACTIVE = (By.CSS_SELECTOR, u'div.line.line-1.active') # x: 96 y: 935 width: 72 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    LINE_2_ACTIVE = (By.CSS_SELECTOR, u'div.line.line-2.active') # x: 168 y: 935 width: 72 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CLASS_LINE_3 = (By.CLASS_NAME, u'line-3') # x: 240 y: 935 width: 72 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CLASS_LINE_4 = (By.CLASS_NAME, u'line-4') # x: 312 y: 935 width: 72 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    DESIGN_CRUMB_THREEWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.line-1') # x: 576 y: 935 width: 144 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    DESIGN_CRUMB_THREEWAY_LINE_2 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.line-2') # x: 720 y: 935 width: 144 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    CRUMB_TWOWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-crumb-twoway>.line-1') # x: 1056 y: 935 width: 288 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    SAVE_CRUMB_THREEWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.line-1') # x: 1536 y: 935 width: 144 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 
    SAVE_CRUMB_THREEWAY_LINE_2 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.line-2') # x: 1680 y: 935 width: 144 height: 1, tag: div, type: , name: None, form_id: , checkbox: ,href: 

    def click_img_link_alt_panelprofile_white(self, parameters=None): # AutoGen method
        self.click_element(self.ALT_PANELPROFILE_WHITE)

    def click_img_link_alt_panelprofile_silver(self, parameters=None): # AutoGen method
        self.click_element(self.ALT_PANELPROFILE_SILVER)

    def click_img_link_alt_panelprofile_satin_gold(self, parameters=None): # AutoGen method
        self.click_element(self.ALT_PANELPROFILE_SATIN_GOLD)

    def click_link_disable_element_takaisin(self, parameters=None): # AutoGen method
        self.click_element(self.DISABLE_ELEMENT_TAKAISIN)

    def click_link_element_help(self, parameters=None): # AutoGen method
        self.click_element(self.ELEMENT_HELP)

    def click_link_element_restart_aloita_alusta(self, parameters=None): # AutoGen method
        self.click_element(self.ELEMENT_RESTART_ALOITA_ALUSTA)

    def click_link_element_enable_seuraava_vaihe(self, parameters=None): # AutoGen method
        self.click_element(self.ELEMENT_ENABLE_SEURAAVA_VAIHE)

    def click_link_main_container_currency(self, parameters=None): # AutoGen method
        self.click_element(self.MAIN_CONTAINER_CURRENCY)

    def click_link_class_price(self, parameters=None): # AutoGen method
        self.click_element(self.CLASS_PRICE)

    def click_link_measure_title_mittaa_ja_rakenna(self, parameters=None): # AutoGen method
        self.click_element(self.MEASURE_TITLE_MITTAA_JA_RAKENNA)

    def click_link_design_title_liukuovien_suunnittelu(self, parameters=None): # AutoGen method
        self.click_element(self.DESIGN_TITLE_LIUKUOVIEN_SUUNNITTELU)

    def click_link_structure_title_rungon_suunnittelu(self, parameters=None): # AutoGen method
        self.click_element(self.STRUCTURE_TITLE_RUNGON_SUUNNITTELU)

    def click_link_save_title_tallennus_ja_yhteydenotto(self, parameters=None): # AutoGen method
        self.click_element(self.SAVE_TITLE_TALLENNUS_JA_YHTEYDENOTTO)
