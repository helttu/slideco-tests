# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Ala_palkki(CommonUtils):
    # Pagemodel timestamp: 20160121111843
    # Pagemodel url: http://finndeco.codemen.fi/build/?api=K3JK2FCG
    # Pagemodel area: (1, 670, 1600, 120)
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
    MEASURE_TITLE_MITTAA_JA_RAKENNA = (By.CSS_SELECTOR, u'.section-measure>.section-title>span') # x: 0 y: 694 width: 533 height: 23
    DESIGN_TITLE_LIUKUOVIEN_SUUNNITTELU = (By.CSS_SELECTOR, u'.section-design>.section-title>span') # x: 533 y: 694 width: 533 height: 23
    SAVE_TITLE_TALLENNUS_JA_YHTEYDENOTTO = (By.CSS_SELECTOR, u'.section-save>.section-title>span') # x: 1067 y: 694 width: 533 height: 23
    CRUMB_FIVEWAY_1 = (By.CSS_SELECTOR, u'.section-crumb-fiveway>.crumb-1') # x: 103 y: 757 width: 13 height: 13
    CRUMB_FIVEWAY_2 = (By.CSS_SELECTOR, u'.section-crumb-fiveway>.crumb-2') # x: 182 y: 757 width: 13 height: 13
    CRUMB_FIVEWAY_3 = (By.CSS_SELECTOR, u'.section-crumb-fiveway>.crumb-3') # x: 262 y: 757 width: 13 height: 13
    CLASS_CRUMB_4 = (By.CLASS_NAME, u'crumb-4') # x: 342 y: 757 width: 13 height: 13
    CLASS_CRUMB_5 = (By.CLASS_NAME, u'crumb-5') # x: 422 y: 757 width: 13 height: 13
    DESIGN_CRUMB_THREEWAY_1 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-1') # x: 636 y: 757 width: 13 height: 13
    DESIGN_CRUMB_THREEWAY_2 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-2') # x: 796 y: 757 width: 13 height: 13
    DESIGN_CRUMB_THREEWAY_3 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.crumb-3') # x: 956 y: 757 width: 13 height: 13
    SAVE_CRUMB_THREEWAY_1 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-1') # x: 1169 y: 757 width: 13 height: 13
    SAVE_CRUMB_THREEWAY_2 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-2') # x: 1329 y: 757 width: 13 height: 13
    SAVE_CRUMB_THREEWAY_3 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.crumb-3') # x: 1489 y: 757 width: 13 height: 13
    CRUMB_FIVEWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-crumb-fiveway>.line-1') # x: 107 y: 761 width: 80 height: 1
    CRUMB_FIVEWAY_LINE_2 = (By.CSS_SELECTOR, u'.section-crumb-fiveway>.line-2') # x: 187 y: 761 width: 80 height: 1
    CLASS_LINE_3 = (By.CLASS_NAME, u'line-3') # x: 267 y: 761 width: 80 height: 1
    CLASS_LINE_4 = (By.CLASS_NAME, u'line-4') # x: 347 y: 761 width: 80 height: 1
    DESIGN_CRUMB_THREEWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.line-1') # x: 640 y: 761 width: 160 height: 1
    DESIGN_CRUMB_THREEWAY_LINE_2 = (By.CSS_SELECTOR, u'.section-design>.section-crumb-threeway>.line-2') # x: 800 y: 761 width: 160 height: 1
    SAVE_CRUMB_THREEWAY_LINE_1 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.line-1') # x: 1173 y: 761 width: 160 height: 1
    SAVE_CRUMB_THREEWAY_LINE_2 = (By.CSS_SELECTOR, u'.section-save>.section-crumb-threeway>.line-2') # x: 1333 y: 761 width: 160 height: 1

    def wait_for_visible_measure_title_mittaa_ja_rakenna(self):
        self.wait_until_element_is_visible(self.MEASURE_TITLE_MITTAA_JA_RAKENNA)
