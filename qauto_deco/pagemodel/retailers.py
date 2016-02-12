# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Retailers(CommonUtils):
    # Pagemodel timestamp: 20160205144055
    # Pagemodel url: http://finndeco.codemen.fi/manage/#/dash/retailers/5/retailers
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
    EMBER857_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember857>.glyphicon-user') # x: 1162 y: 18 width: 12 height: 12
    EMBER942_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember942>.glyphicon-briefcase') # x: 1258 y: 18 width: 12 height: 12
    CLASS_GLYPHICON_QUESTION_SIGN = (By.CLASS_NAME, u'glyphicon-question-sign') # x: 1444 y: 18 width: 12 height: 12
    EMBER757_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember757>.glyphicon-log-out') # x: 1477 y: 18 width: 12 height: 12
    CLASS_LOGO_MAIN = (By.CLASS_NAME, u'logo-main') # x: 80 y: 20 width: 100 height: 100
    CLASS_NOTIFICATION = (By.CLASS_NAME, u'notification') # x: 180 y: 30 width: 4 height: 4
    GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'h1>.glyphicon-briefcase') # x: 452 y: 106 width: 31 height: 31
    CLASS_GLYPHICON_DASHBOARD = (By.CLASS_NAME, u'glyphicon-dashboard') # x: 32 y: 166 width: 14 height: 14
    RETAILERS = (By.CSS_SELECTOR, u'h2') # x: 467 y: 172 width: 910 height: 33
    EMBER992_GLYPHICON_SHOPPING_CART = (By.CSS_SELECTOR, u'#ember992>.glyphicon-shopping-cart') # x: 32 y: 202 width: 14 height: 14
    ID_RETAILER_CONTENT_FLOATED_1 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/THEAD[1]/TR[1]/TH[1]') # x: 467 y: 215 width: 199 height: 38
    CONTAINS_TEXT_LOCATION = (By.XPATH, u'//th[contains(text(),"Location")]') # x: 666 y: 215 width: 84 height: 38
    CONTAINS_TEXT_APPLICATIONS = (By.XPATH, u'//th[contains(text(),"Applications")]') # x: 750 y: 215 width: 113 height: 38
    CONTAINS_TEXT_MANAGER_COUNT = (By.XPATH, u'//th[contains(text(),"Manager count")]') # x: 863 y: 215 width: 131 height: 38
    CONTAINS_TEXT_CHILD_RETAILER_COUNT = (By.XPATH, u'//th[contains(text(),"Child retailer count")]') # x: 994 y: 215 width: 163 height: 38
    ID_RETAILER_CONTENT_FLOATED_7 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/THEAD[1]/TR[1]/TH[6]') # x: 1157 y: 215 width: 220 height: 38
    EMBER1013_GLYPHICON = (By.CSS_SELECTOR, u'#ember1013>.glyphicon-th') # x: 32 y: 238 width: 14 height: 14
    ID_EMBER1386 = (By.ID, u'ember1386') # x: 1165 y: 262 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_0 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[1]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 262 width: 30 height: 30
    ID_EMBER1406 = (By.ID, u'ember1406') # x: 1305 y: 262 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_KOSTI_TESTAA = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[1]/TD[1]/STRONG[1]') # x: 475 y: 264 width: 102 height: 16
    EMBER1371_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1371>img[alt="Brand"]') # x: 475 y: 265 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF_14 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[1]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 267 width: 1 height: 1
    EMBER1035_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember1035>.glyphicon-certificate') # x: 32 y: 274 width: 14 height: 14
    ID_RETAILER_CONTENT_FLOATED_8 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[1]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 276 width: 8 height: 4
    EMBER1378_TEXT = (By.CSS_SELECTOR, u'#ember1378>.text-center') # x: 758 y: 282 width: 97 height: 20
    EMBER1046_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember1046>.glyphicon-briefcase') # x: 32 y: 310 width: 14 height: 14
    ID_EMBER1423 = (By.ID, u'ember1423') # x: 1165 y: 319 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_8 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[2]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 319 width: 30 height: 30
    ID_EMBER1443 = (By.ID, u'ember1443') # x: 1305 y: 319 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_REG_JKL_KESKUSTA = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[2]/TD[1]/STRONG[1]') # x: 475 y: 321 width: 153 height: 16
    EMBER1408_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1408>img[alt="Brand"]') # x: 475 y: 322 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[2]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 324 width: 1 height: 1
    ID_RETAILER_CONTENT_FLOATED = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[2]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 333 width: 8 height: 4
    EMBER1415_TEXT = (By.CSS_SELECTOR, u'#ember1415>.text-center') # x: 758 y: 339 width: 97 height: 20
    EMBER1055_GLYPHICON_GBP = (By.CSS_SELECTOR, u'#ember1055>.glyphicon-gbp') # x: 32 y: 346 width: 14 height: 14
    ID_EMBER1460 = (By.ID, u'ember1460') # x: 1165 y: 376 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_9 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[3]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 376 width: 30 height: 30
    ID_EMBER1480 = (By.ID, u'ember1480') # x: 1305 y: 376 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_REG_JKL_UIMAHARJU = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[3]/TD[1]/STRONG[1]') # x: 475 y: 378 width: 158 height: 16
    EMBER1445_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1445>img[alt="Brand"]') # x: 475 y: 379 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF_3 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[3]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 381 width: 1 height: 1
    EMBER1070_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember1070>.glyphicon-user') # x: 32 y: 382 width: 14 height: 14
    ID_RETAILER_CONTENT_FLOATED_14 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[3]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 390 width: 8 height: 4
    EMBER1452_TEXT = (By.CSS_SELECTOR, u'#ember1452>.text-center') # x: 758 y: 396 width: 97 height: 20
    CLASS_GLYPHICON_COG = (By.CLASS_NAME, u'glyphicon-cog') # x: 32 y: 418 width: 14 height: 14
    ID_EMBER1497 = (By.ID, u'ember1497') # x: 1165 y: 433 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_6 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[4]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 433 width: 30 height: 30
    ID_EMBER1517 = (By.ID, u'ember1517') # x: 1305 y: 433 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_REG_JKL_PUPUHUHTA = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[4]/TD[1]/STRONG[1]') # x: 475 y: 435 width: 165 height: 16
    EMBER1482_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1482>img[alt="Brand"]') # x: 475 y: 436 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF_4 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[4]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 438 width: 1 height: 1
    ID_RETAILER_CONTENT_FLOATED_12 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[4]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 447 width: 8 height: 4
    EMBER1489_TEXT = (By.CSS_SELECTOR, u'#ember1489>.text-center') # x: 758 y: 453 width: 97 height: 20
    RETAILER_SIDEBAR = (By.CSS_SELECTOR, u'#retailer-sidebar>hr') # x: 0 y: 464 width: 260 height: 2
    ID_EMBER1534 = (By.ID, u'ember1534') # x: 1165 y: 490 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_12 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[5]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 490 width: 30 height: 30
    ID_EMBER1554 = (By.ID, u'ember1554') # x: 1305 y: 490 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_REG_JKL_SAARELA = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[5]/TD[1]/STRONG[1]') # x: 475 y: 492 width: 139 height: 16
    EMBER1519_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1519>img[alt="Brand"]') # x: 475 y: 493 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF_5 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[5]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 495 width: 1 height: 1
    EMBER770_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember770>.glyphicon-user') # x: 32 y: 496 width: 14 height: 14
    ID_RETAILER_CONTENT_FLOATED_0 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[5]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 504 width: 8 height: 4
    EMBER1526_TEXT = (By.CSS_SELECTOR, u'#ember1526>.text-center') # x: 758 y: 510 width: 97 height: 20
    EMBER772_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember772>.glyphicon-log-out') # x: 32 y: 532 width: 14 height: 14
    ID_RETAILER_CONTENT_FLOATED_11 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[6]/TD[2]/DIV[1]') # x: 674 y: 547 width: 68 height: 20
    ID_EMBER1571 = (By.ID, u'ember1571') # x: 1165 y: 547 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_2 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[6]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 547 width: 30 height: 30
    ID_EMBER1591 = (By.ID, u'ember1591') # x: 1305 y: 547 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_10 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[6]/TD[1]/STRONG[1]') # x: 475 y: 549 width: 16 height: 16
    EMBER1556_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1556>img[alt="Brand"]') # x: 475 y: 550 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF_11 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[6]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 552 width: 1 height: 1
    ID_RETAILER_CONTENT_FLOATED_2 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[6]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 561 width: 8 height: 4
    EMBER1556_TEXT = (By.CSS_SELECTOR, u'#ember1556>.text-center') # x: 475 y: 567 width: 183 height: 20
    EMBER1563_TEXT = (By.CSS_SELECTOR, u'#ember1563>.text-center') # x: 758 y: 567 width: 97 height: 20
    ID_RETAILER_CONTENT_FLOATED_13 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[7]/TD[2]/DIV[1]') # x: 674 y: 604 width: 68 height: 20
    ID_EMBER1608 = (By.ID, u'ember1608') # x: 1165 y: 604 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_13 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[7]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 604 width: 30 height: 30
    ID_EMBER1628 = (By.ID, u'ember1628') # x: 1305 y: 604 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_6 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[7]/TD[1]/STRONG[1]') # x: 475 y: 606 width: 16 height: 16
    EMBER1593_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1593>img[alt="Brand"]') # x: 475 y: 607 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF_7 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[7]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 609 width: 1 height: 1
    ID_RETAILER_CONTENT_FLOATED_5 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[7]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 618 width: 8 height: 4
    EMBER1593_TEXT = (By.CSS_SELECTOR, u'#ember1593>.text-center') # x: 475 y: 624 width: 183 height: 20
    EMBER1600_TEXT = (By.CSS_SELECTOR, u'#ember1600>.text-center') # x: 758 y: 624 width: 97 height: 20
    ID_RETAILER_CONTENT_FLOATED_3 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[8]/TD[2]/DIV[1]') # x: 674 y: 661 width: 68 height: 20
    ID_EMBER1645 = (By.ID, u'ember1645') # x: 1165 y: 661 width: 83 height: 30
    ID_RETAILER_CONTENT_FLOATED_ON_OF_1 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[8]/TD[6]/DIV[1]/BUTTON[1]') # x: 1247 y: 661 width: 30 height: 30
    ID_EMBER1665 = (By.ID, u'ember1665') # x: 1305 y: 661 width: 53 height: 30
    ID_RETAILER_CONTENT_FLOATED_4 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[8]/TD[1]/STRONG[1]') # x: 475 y: 663 width: 16 height: 16
    EMBER1630_ALT_BRAND = (By.CSS_SELECTOR, u'#ember1630>img[alt="Brand"]') # x: 475 y: 664 width: 16 height: 16
    ID_RETAILER_CONTENT_FLOATED_ON_OF_10 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[8]/TD[6]/DIV[1]/BUTTON[1]/SPAN[2]') # x: 1265 y: 666 width: 1 height: 1
    ID_RETAILER_CONTENT_FLOATED_9 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/TABLE[1]/TBODY[1]/TR[8]/TD[6]/DIV[1]/BUTTON[1]/SPAN[1]') # x: 1258 y: 675 width: 8 height: 4
    EMBER1630_TEXT = (By.CSS_SELECTOR, u'#ember1630>.text-center') # x: 475 y: 681 width: 183 height: 20
    EMBER1637_TEXT = (By.CSS_SELECTOR, u'#ember1637>.text-center') # x: 758 y: 681 width: 97 height: 20
    CLASS_BTN_LINK = (By.CLASS_NAME, u'btn-link') # x: 1227 y: 718 width: 81 height: 34
    TEXT_8 = (By.CSS_SELECTOR, u'td.text-center>strong') # x: 781 y: 720 width: 9 height: 16

    # Dynamic objects:
    RETAILERS_LINK = (By.LINK_TEXT, u'Retailers')     # x: 0 y: 300 width: 260 height: 36 # Dynamic object


    def click_retailers_link(self):
        self.click(self.RETAILERS_LINK)

    def click_element_retailers_link(self):
        self.click_element(self.RETAILERS_LINK)

    def wait_until_element_is_visible_kosti_testaa_link(self):
        self.wait_until_element_is_visible(self.ID_RETAILER_CONTENT_FLOATED_KOSTI_TESTAA)
