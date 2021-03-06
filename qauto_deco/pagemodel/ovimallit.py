# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Ovimallit(CommonUtils):
    # Pagemodel timestamp: 20160121150428
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
    CLASS_TAB_SEPARATORS_LAYOUT = (By.CLASS_NAME, u'tab-separators-layout') # x: 1232 y: 0 width: 368 height: 62
    CONTENT_SEPARATORS_LAYOUT_STYLE_VALITSE_MIELEISESI_OVIMALLI_T_ST = (By.CSS_SELECTOR, u'.content-separators-layout>.style-header>h2') # x: 1240 y: 80 width: 352 height: 28
    STYLE_ACTIVE_SELECTION_CHECKED_BG = (By.CSS_SELECTOR, u'div.style.active>.selection-checked>.bg') # x: 1268 y: 136 width: 80 height: 80
    STYLE_ACTIVE_SELECTION_CHECKED_ICON = (By.CSS_SELECTOR, u'div.style.active>.selection-checked>.icon') # x: 1268 y: 136 width: 80 height: 80
    SEPARATORS_ELEMENT = (By.CSS_SELECTOR, u'div.separators-element') # x: 1287 y: 142 width: 38 height: 62
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22

    # Dynamic objects:
    OVI_PYSTY_KAKSI = (By.XPATH, u'//BODY/SECTION[12]/DIV[2]/DIV[1]/DIV[2]/DIV[2]/DIV[1]')     # x: 1364 y: 136 width: 76 height: 76 # Dynamic object
    OVI_PYSTY_KOLME = (By.XPATH, u'//BODY/SECTION[12]/DIV[2]/DIV[1]/DIV[2]/DIV[3]/DIV[1]')     # x: 1460 y: 136 width: 76 height: 76 # Dynamic object
    CONTAINS_TEXT_LIUKUOVIEN_SUUNNITTELU = (By.XPATH, u'//h2[contains(text(),"Liukuovien suunnittelu")]')     # x: 145 y: 612 width: 190 height: 60 # Dynamic object
    BODY_LIUKUOVIEN_SUUNNITTELU_VALITSE_VAKIOMALLEISTA = (By.XPATH, u'//BODY/SECTION[6]/DIV[1]')     # x: 125 y: 572 width: 230 height: 174 # Dynamic object
    CONTAINS_TEXT_VALITSE_VAKIOMALLEISTA = (By.XPATH, u'//p[contains(text(),"Valitse vakiomalleista")]')     # x: 145 y: 688 width: 190 height: 18 # Dynamic object

    def valitse_ovimalli(self, parameters=None):
        if parameters['ovimalli'] == "ovi_pysty_2":
            self.click_element(self.OVI_PYSTY_KAKSI)
        elif parameters['ovimalli'] == "ovi_pysty_3":
            self.click_element(self.OVI_PYSTY_KOLME)
        else:
            self.click_element(self.STYLE_ACTIVE_SELECTION_CHECKED_BG)

    def click_seuraava_vaihe(self, parameters=None):
        self.click_element(self.ELEMENT_ENABLE_SEURAAVA_VAIHE)

    def show_help(self, parameters=None):
        self.mouse_over(self.ELEMENT_HELP)
        self.element_text_should_be(self.CONTAINS_TEXT_LIUKUOVIEN_SUUNNITTELU, u'Liukuovien suunnittelu')
