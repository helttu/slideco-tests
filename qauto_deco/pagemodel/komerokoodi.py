# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Komerokoodi(CommonUtils):
    # Pagemodel timestamp: 20160122062828
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
    ARVIOITU_HINTA = (By.CSS_SELECTOR, u'h3') # x: 1242 y: 10 width: 348 height: 32
    CONST_365_99 = (By.CSS_SELECTOR, u'strong') # x: 1374 y: 53 width: 83 height: 27
    STORAGE_BLOCK_ITEM_GROUP_CLICKABLE_CONTENT_ESIKATSELU = (By.CSS_SELECTOR, u'.storage-block-item-group-clickable>.storage-block-item-content-label>p') # x: 1292 y: 100 width: 87 height: 25
    ALT_PREVIEW_ICON = (By.CSS_SELECTOR, u'img[alt="Preview icon"]') # x: 1252 y: 106 width: 22 height: 13
    STORAGE_BLOCK_ITEM_GROUP_SAVE_CONTENT_TALLENNA_SUUNNITELMA = (By.CSS_SELECTOR, u'.storage-block-item-group-save>.storage-block-item-content-label>p') # x: 1292 y: 150 width: 183 height: 25
    ALT_SAVE_ICON = (By.CSS_SELECTOR, u'img[alt="Save icon"]') # x: 1252 y: 153 width: 21 height: 21
    SAVED = (By.CSS_SELECTOR, u'.saved>img') # x: 1360 y: 213 width: 112 height: 80
    SAVED_TALLENNETTU_AINUTLAATUINEN_KOMEROKOODISI_ON = (By.CSS_SELECTOR, u'.saved>div') # x: 1232 y: 298 width: 368 height: 27
    INPUTTED_6Q = (By.CSS_SELECTOR, u'.inputted>span') # x: 1362 y: 345 width: 27 height: 19
    STORAGE_BLOCK_ITEM_NEW_SEURAAVA = (By.CSS_SELECTOR, u'.storage-block-item-form-new>button') # x: 1250 y: 385 width: 331 height: 44
    STORAGE_BLOCK_ITEM_GROUP_SHARE_CONTENT_JAA_T_SIVU = (By.CSS_SELECTOR, u'.storage-block-item-group-share>.storage-block-item-content-label>p') # x: 1292 y: 531 width: 114 height: 25
    ALT_SHARE_ICON = (By.CSS_SELECTOR, u'img[alt="Share icon"]') # x: 1252 y: 534 width: 21 height: 24
    CLASS_STORAGE_BLOCK_ITEM_GROUP_CALL = (By.CLASS_NAME, u'storage-block-item-group-call') # x: 1232 y: 573 width: 368 height: 50
    DISABLE_ELEMENT_TAKAISIN = (By.CSS_SELECTOR, u'.disable-element>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22


