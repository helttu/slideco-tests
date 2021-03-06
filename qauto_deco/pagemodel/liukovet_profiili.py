# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Liukovet_profiili(CommonUtils):
    # Pagemodel timestamp: 20160121133447
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
    CLASS_TAB_PROFILE_GROUP = (By.CLASS_NAME, u'tab-profile-group') # x: 1232 y: 0 width: 368 height: 62
    CONTENT_PROFILE_GROUP_STYLE_VALITSE_MIELEISESI_LIUKUOVIPROFIILI = (By.CSS_SELECTOR, u'.content-profile-group>.style-header>h2') # x: 1240 y: 80 width: 352 height: 28
    ALT_S200 = (By.CSS_SELECTOR, u'img[alt="S200"]') # x: 1242 y: 136 width: 76 height: 76
    CONTENT_PROFILE_GROUP_STYLE_CONTAINER_LIST_SELECTION_CHECKED_ICON = (By.CSS_SELECTOR, u'.content-profile-group>.style-container-list>div.style>.selection-checked>.icon') # x: 1242 y: 136 width: 335 height: 80
    CONTENT_PROFILE_GROUP_STYLE_CONTAINER_LIST_SELECTION_CHECKED_BG = (By.CSS_SELECTOR, u'.content-profile-group>.style-container-list>div.style>.selection-checked>.bg') # x: 1242 y: 136 width: 335 height: 80
    CONTENT_PROFILE_GROUP_STYLE_CONTAINER_LIST_S200 = (By.CSS_SELECTOR, u'.content-profile-group>.style-container-list>div.style>div.style-label') # x: 1322 y: 152 width: 255 height: 33
    ALT_S100 = (By.CSS_SELECTOR, u'img[alt="S100"]') # x: 1242 y: 233 width: 76 height: 76
    ALT_A101 = (By.CSS_SELECTOR, u'img[alt="A101"]') # x: 1242 y: 329 width: 76 height: 76
    ALT_A102 = (By.CSS_SELECTOR, u'img[alt="A102"]') # x: 1242 y: 426 width: 76 height: 76
    ALT_A103 = (By.CSS_SELECTOR, u'img[alt="A103"]') # x: 1242 y: 522 width: 76 height: 76
    ALT_A104 = (By.CSS_SELECTOR, u'img[alt="A104"]') # x: 1242 y: 619 width: 76 height: 76
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22

    # Dynamic objects:
    CONTENT_PROFILE_GROUP_STYLE_CONTAINER_LIST_SELECTION_CHECKED_ICON = (By.CSS_SELECTOR, u'.content-profile-group>.style-container-list>div.style>.selection-checked>.icon')     # x: 1242 y: 136 width: 335 height: 80 # Dynamic object
    ALT_S100 = (By.CSS_SELECTOR, u'img[alt="S100"]')     # x: 1242 y: 233 width: 76 height: 76 # Dynamic object
    ALT_A101 = (By.CSS_SELECTOR, u'img[alt="A101"]')     # x: 1242 y: 329 width: 76 height: 76 # Dynamic object
    ALT_A102 = (By.CSS_SELECTOR, u'img[alt="A102"]')     # x: 1242 y: 442 width: 76 height: 76 # Dynamic object
    ALT_A103 = (By.CSS_SELECTOR, u'img[alt="A103"]')     # x: 1242 y: 538 width: 76 height: 76 # Dynamic object
    ALT_A104 = (By.CSS_SELECTOR, u'img[alt="A104"]')     # x: 1242 y: 635 width: 76 height: 76 # Dynamic object
    CONTAINS_TEXT_LIUKUOVIPROFIILIT = (By.XPATH, u'//h2[contains(text(),"Liukuoviprofiilit")]')     # x: 145 y: 552 width: 190 height: 30 # Dynamic object
    BODY_LIUKUOVIPROFIILIT_OVIEN_PROFIILIT_OVAT_LIUKUOVIEN_KEH_PROFIILEJA_S100_JA = (By.XPATH, u'//BODY/SECTION[5]/DIV[1]')     # x: 125 y: 512 width: 230 height: 234 # Dynamic object

    def valitse_liukuoviprofiili(self, parameters=None):
        if parameters['profiili'] == "s200":
            self.click_element(self.ALT_S200)
        elif parameters['profiili'] == "s100":
             self.click_element(self.ALT_S100)
        elif parameters['profiili'] == "a101":
             self.click_element(self.ALT_A101)
        elif parameters['profiili']== "a102":
             self.click_element(self.ALT_A102)
        elif parameters['profiili'] == "a103":
             self.click_element(self.ALT_A103)
        elif parameters['profiili'] == "a104":
             self.click_element(self.ALT_A104)
        else:
            self.click_element(self.ALT_S200)

    def click_seuraava_vaihe(self):
        self.click_element(self.ELEMENT_ENABLE_SEURAAVA_VAIHE)

    def show_help(self, parameters=None):
        self.mouse_over(self.ELEMENT_HELP)
        self.element_text_should_be(self.CONTAINS_TEXT_LIUKUOVIPROFIILIT, u'Liukuoviprofiilit')
