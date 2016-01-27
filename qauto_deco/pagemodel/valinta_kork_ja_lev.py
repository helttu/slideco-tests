# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Valinta_kork_ja_lev(CommonUtils):
    # Pagemodel timestamp: 20160121125641
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
    SELECTABLE_VALUE_0_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-0>.inner-num') # x: 1231 y: 16 width: 10 height: 10
    SELECTABLE_VALUE_1_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-1>.inner-num') # x: 1231 y: 78 width: 10 height: 10
    SELECTABLE_VALUE_2_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-2>.inner-num') # x: 1231 y: 141 width: 10 height: 10
    SELECTABLE_VALUE_3_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-3>.inner-num') # x: 1231 y: 203 width: 10 height: 10
    CLASS_SELECTED_VALUE_GROUP_LABEL_HEIGHT = (By.CLASS_NAME, u'selected-value-group-label-height') # x: 304 y: 237 width: 480 height: 44
    CLASS_SELECTED_VALUE_GROUP_LABEL_WIDTH = (By.CLASS_NAME, u'selected-value-group-label-width') # x: 816 y: 237 width: 480 height: 44
    SELECTABLE_VALUE_4_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-4>.inner-num') # x: 1231 y: 265 width: 10 height: 10
    SELECTED_VALUE_GROUP_HEIGHT_0_INNER_NUM_2 = (By.CSS_SELECTOR, u'.selected-value-group-height>.selected-value-0>.inner-num') # x: 359 y: 297 width: 10 height: 10
    SELECTED_VALUE_GROUP_HEIGHT_1_INNER_NUM_5 = (By.CSS_SELECTOR, u'.selected-value-group-height>.selected-value-1>.inner-num') # x: 479 y: 297 width: 10 height: 10
    SELECTED_VALUE_GROUP_HEIGHT_2_INNER_NUM_0 = (By.CSS_SELECTOR, u'.selected-value-group-height>.selected-value-2>.inner-num') # x: 599 y: 297 width: 10 height: 10
    SELECTED_VALUE_GROUP_HEIGHT_3_INNER_NUM_0 = (By.CSS_SELECTOR, u'.selected-value-group-height>.selected-value-3>.inner-num') # x: 719 y: 297 width: 10 height: 10
    SELECTED_VALUE_GROUP_WIDTH_0_INNER_NUM = (By.CSS_SELECTOR, u'.selected-value-group-width>.selected-value-0>.inner-num') # x: 871 y: 297 width: 10 height: 10
    SELECTED_VALUE_GROUP_WIDTH_1_INNER_NUM_2 = (By.CSS_SELECTOR, u'.selected-value-group-width>.selected-value-1>.inner-num') # x: 991 y: 297 width: 10 height: 10
    SELECTED_VALUE_GROUP_WIDTH_2_INNER_NUM_0 = (By.CSS_SELECTOR, u'.selected-value-group-width>.selected-value-2>.inner-num') # x: 1111 y: 297 width: 10 height: 10
    SELECTED_VALUE_GROUP_WIDTH_3_INNER_NUM_0 = (By.CSS_SELECTOR, u'.selected-value-group-width>.selected-value-3>.inner-num') # x: 1231 y: 297 width: 10 height: 10
    SELECTABLE_VALUE_5_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-5>.inner-num') # x: 1231 y: 328 width: 10 height: 10
    SELECTABLE_VALUE_6_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-6>.inner-num') # x: 1231 y: 390 width: 10 height: 10
    SELECTABLE_VALUE_7_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-7>.inner-num') # x: 1231 y: 452 width: 10 height: 10
    SELECTABLE_VALUE_8_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-8>.inner-num') # x: 1231 y: 515 width: 10 height: 10
    SELECTABLE_VALUE_9_INNER_NUM = (By.CSS_SELECTOR, u'.selectable-value-9>.inner-num') # x: 1231 y: 577 width: 10 height: 10
    ELEMENT_BACK_TAKAISIN = (By.CSS_SELECTOR, u'.element-back>span') # x: 0 y: 637 width: 160 height: 23
    ELEMENT_HELP = (By.CSS_SELECTOR, u'.element-help>span') # x: 160 y: 637 width: 80 height: 23
    ELEMENT_RESTART_ALOITA_ALUSTA = (By.CSS_SELECTOR, u'.element-restart>span') # x: 240 y: 637 width: 240 height: 23
    ELEMENT_ENABLE_SEURAAVA_VAIHE = (By.CSS_SELECTOR, u'.element-enable>span') # x: 1360 y: 637 width: 240 height: 23
    CLASS_CURRENCY = (By.CLASS_NAME, u'currency') # x: 1175 y: 639 width: 9 height: 22
    CLASS_PRICE = (By.CLASS_NAME, u'price') # x: 1190 y: 639 width: 52 height: 22

    def valitse_korkeus_ja_leveys(self, parameters=None):
        # valitaan korkeus 1
        CUSTOM_ELEMENT_K1 = (By.CSS_SELECTOR, '.selectable-value-' + parameters[u'korkeus1'] + '>.inner-num')
        self.click(CUSTOM_ELEMENT_K1)
        sleep(1)
        # valitaan korkeus 2
        CUSTOM_ELEMENT_KORK2 = (By.CSS_SELECTOR, ".selectable-value-" + parameters[u'korkeus2'] + ">.inner-num")
        self.click(CUSTOM_ELEMENT_KORK2)
        # valitaan korkeus 3
        sleep(1)
        CUSTOM_ELEMENT_KORK3 = (By.CSS_SELECTOR, '.selectable-value-' + parameters[u'korkeus3'] + '>.inner-num')
        self.click(CUSTOM_ELEMENT_KORK3)
        # valitaan korkeus 4
        sleep(1)
        CUSTOM_ELEMENT_KORK4 = (By.CSS_SELECTOR,  '.selectable-value-' + parameters[u'korkeus4'] + '>.inner-num')
        self.click(CUSTOM_ELEMENT_KORK4)
        sleep(1)
        # valitaan leveys 1
        CUSTOM_ELEMENT_LEV1 = (By.CSS_SELECTOR,  '.selectable-value-' + parameters[u'leveys1'] + '>.inner-num')
        self.click(CUSTOM_ELEMENT_LEV1)
        # valitaan leveys 2
        CUSTOM_ELEMENT_LEV2 = (By.CSS_SELECTOR,'.selectable-value-' + parameters[u'leveys2'] + '>.inner-num')
        self.click(CUSTOM_ELEMENT_LEV2)
        # valitaan leveys 3
        CUSTOM_ELEMENT_LEV3 = (By.CSS_SELECTOR, '.selectable-value-' + parameters[u'leveys3'] + '>.inner-num')
        self.click(CUSTOM_ELEMENT_LEV3)
        # valitaan leveys 4
        CUSTOM_ELEMENT_LEV4 = (By.CSS_SELECTOR, '.selectable-value-' + parameters[u'leveys4'] + '>.inner-num')
        self.click(CUSTOM_ELEMENT_LEV4)

    def click_seuraava_vaihe(self):
        self.click(self.ELEMENT_ENABLE_SEURAAVA_VAIHE)
