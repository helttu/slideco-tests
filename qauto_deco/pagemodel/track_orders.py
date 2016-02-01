# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Track_orders(CommonUtils):
    # Pagemodel timestamp: 20160129113030
    # Pagemodel url: http://finndeco.codemen.fi/manage/#/dash/retailers/5/orders
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
    # Links found: 1
    # Page model constants:
    EMBER857_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember857>.glyphicon-user') # x: 1162 y: 18 width: 12 height: 12
    EMBER942_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember942>.glyphicon-briefcase') # x: 1258 y: 18 width: 12 height: 12
    CLASS_GLYPHICON_QUESTION_SIGN = (By.CLASS_NAME, u'glyphicon-question-sign') # x: 1444 y: 18 width: 12 height: 12
    EMBER757_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember757>.glyphicon-log-out') # x: 1477 y: 18 width: 12 height: 12
    CLASS_LOGO_MAIN = (By.CLASS_NAME, u'logo-main') # x: 80 y: 20 width: 100 height: 100
    CLASS_NOTIFICATION = (By.CLASS_NAME, u'notification') # x: 180 y: 30 width: 4 height: 4
    ID_EMBER1310 = (By.ID, u'ember1310') # x: 1252 y: 83 width: 285 height: 34
    GLYPHICON_SHOPPING_CART = (By.CSS_SELECTOR, u'h1>.glyphicon-shopping-cart') # x: 308 y: 104 width: 36 height: 36
    ORDERS = (By.LINK_TEXT, u'Orders') # x: 308 y: 155 width: 76 height: 42
    PULL_RIGHT_BTN_DEFAULT_SM_DESIGNER_VIEW = (By.CSS_SELECTOR, u'button.pull-right.btn.btn-default.btn-sm') # x: 1405 y: 155 width: 131 height: 30
    CLASS_GLYPHICON_PLUS = (By.CLASS_NAME, u'glyphicon-plus') # x: 1416 y: 163 width: 12 height: 12
    CLASS_GLYPHICON_DASHBOARD = (By.CLASS_NAME, u'glyphicon-dashboard') # x: 32 y: 166 width: 14 height: 14
    EMBER992_GLYPHICON_SHOPPING_CART = (By.CSS_SELECTOR, u'#ember992>.glyphicon-shopping-cart') # x: 32 y: 202 width: 14 height: 14
    CLASS_GLYPHICON_TH = (By.CLASS_NAME, u'glyphicon-th') # x: 32 y: 238 width: 14 height: 14
    SEARCH = (By.CSS_SELECTOR, u'h2') # x: 413 y: 249 width: 1123 height: 33
    EMBER1035_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember1035>.glyphicon-certificate') # x: 32 y: 274 width: 14 height: 14
    XS_2_OFFSET_1_REFERENCE_CUSTOMER_NAME = (By.CSS_SELECTOR, u'div.col-xs-2.col-xs-offset-1>h4') # x: 413 y: 302 width: 180 height: 38
    CONTAINS_TEXT_PAYMENT_0 = (By.XPATH, u'//h4[contains(text(),"Payment")]') # x: 623 y: 302 width: 180 height: 19
    CONTAINS_TEXT_STATUS = (By.XPATH, u'//h4[contains(text(),"Status")]') # x: 833 y: 302 width: 180 height: 19
    CONTAINS_TEXT_CREATOR = (By.XPATH, u'//h4[contains(text(),"Creator")]') # x: 1042 y: 302 width: 180 height: 19
    CONTAINS_TEXT_SORT_BY_DATE = (By.XPATH, u'//h4[contains(text(),"Sort By Date")]') # x: 1252 y: 302 width: 180 height: 19
    EMBER1046_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember1046>.glyphicon-briefcase') # x: 32 y: 310 width: 14 height: 14
    CLASS_GLYPHICON_GBP = (By.CLASS_NAME, u'glyphicon-gbp') # x: 32 y: 346 width: 14 height: 14
    ID_EMBER1317 = (By.ID, u'ember1317') # x: 413 y: 350 width: 180 height: 34
    ID_EMBER1320 = (By.ID, u'ember1320') # x: 623 y: 350 width: 180 height: 34
    ID_EMBER1342 = (By.ID, u'ember1342') # x: 833 y: 350 width: 180 height: 34
    ID_EMBER1358 = (By.ID, u'ember1358') # x: 1042 y: 350 width: 180 height: 34
    BTN_SM_DEFAULT_ACTIVE_ASCENDING = (By.CSS_SELECTOR, u'button.btn.btn-sm.btn-default.active') # x: 1251 y: 350 width: 80 height: 30
    CONTAINS_TEXT_DESCENDING = (By.XPATH, u'//button[contains(text(),"Descending")]') # x: 1329 y: 350 width: 88 height: 30
    EMBER1070_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember1070>.glyphicon-user') # x: 32 y: 382 width: 14 height: 14
    CONTAINS_TEXT_REFERENCE = (By.XPATH, u'//th[contains(text(),"Reference")]') # x: 293 y: 395 width: 130 height: 51
    ID_ORDERS_LIST_CREATED = (By.XPATH, u'id(\'table-orders-list\')/THEAD[1]/TR[1]/TH[2]') # x: 423 y: 395 width: 80 height: 51
    CONTAINS_TEXT_CUSTOMER_NAME = (By.XPATH, u'//th[contains(text(),"Customer name")]') # x: 503 y: 395 width: 258 height: 51
    CONTAINS_TEXT_TOTAL = (By.XPATH, u'//th[contains(text(),"Total")]') # x: 761 y: 395 width: 81 height: 51
    ID_ORDERS_LIST_0 = (By.XPATH, u'id(\'table-orders-list\')/THEAD[1]/TR[1]/TH[5]') # x: 842 y: 395 width: 20 height: 51
    CONTAINS_TEXT_PAYMENT = (By.XPATH, u'//th[contains(text(),"Payment")]') # x: 862 y: 395 width: 118 height: 51
    CONTAINS_TEXT_STATUS_0 = (By.XPATH, u'//th[contains(text(),"Status")]') # x: 980 y: 395 width: 161 height: 51
    CONTAINS_TEXT_CREATED_BY = (By.XPATH, u'//th[contains(text(),"Created by")]') # x: 1141 y: 395 width: 80 height: 51
    CONTAINS_TEXT_CURRENT_RETAILER = (By.XPATH, u'//th[contains(text(),"Current Retailer")]') # x: 1221 y: 395 width: 80 height: 51
    ID_ORDERS_LIST = (By.XPATH, u'id(\'table-orders-list\')/THEAD[1]/TR[1]/TH[10]') # x: 1301 y: 395 width: 250 height: 51
    CLASS_GLYPHICON_COG = (By.CLASS_NAME, u'glyphicon-cog') # x: 32 y: 418 width: 14 height: 14
    EMBER18627_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18627>.glyphicon-briefcase') # x: 1223 y: 451 width: 14 height: 14
    RETAILER_SIDEBAR = (By.CSS_SELECTOR, u'#retailer-sidebar>hr') # x: 0 y: 464 width: 260 height: 2
    ID_EMBER18631 = (By.LINK_TEXT, u'Details »') # x: 1303 y: 464 width: 70 height: 30
    GDL_ORDER_354_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_354>td>.btn-group>.btn-danger') # x: 1405 y: 464 width: 58 height: 30
    ALT_AKU_HULKKONEN = (By.CSS_SELECTOR, u'.img[alt="Aku Hulkkonen"]') # x: 1169 y: 467 width: 24 height: 24
    GDL_ORDER_354_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_354>td.text-center>.unread') # x: 1041 y: 471 width: 6 height: 16
    GDL_ORDER_354_TEXT = (By.CSS_SELECTOR, u'#gdl_order_354>td.text-center>img') # x: 844 y: 472 width: 16 height: 16
    EMBER18633_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18633>.glyphicon-pencil') # x: 1383 y: 472 width: 12 height: 12
    EMBER770_GLYPHICON_USER = (By.CSS_SELECTOR, u'#ember770>.glyphicon-user') # x: 32 y: 496 width: 14 height: 14
    EMBER18669_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18669>.glyphicon-briefcase') # x: 1223 y: 516 width: 14 height: 14
    ID_EMBER18673 = (By.ID, u'ember18673') # x: 1303 y: 529 width: 70 height: 30
    GDL_ORDER_428_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_428>td>.btn-group>.btn-danger') # x: 1405 y: 529 width: 58 height: 30
    EMBER772_GLYPHICON_LOG_OUT = (By.CSS_SELECTOR, u'#ember772>.glyphicon-log-out') # x: 32 y: 532 width: 14 height: 14
    EMBER19414 = (By.CSS_SELECTOR, u'#ember19414>.img') # x: 1169 y: 532 width: 24 height: 24
    ID_GDL_ORDER_428 = (By.XPATH, u'id(\'gdl_order_428\')/TD[3]/SPAN[1]') # x: 579 y: 536 width: 5 height: 16
    GDL_ORDER_428_GLYPHICON_EARPHONE = (By.CSS_SELECTOR, u'#gdl_order_428>td>a>.glyphicon-earphone') # x: 588 y: 536 width: 14 height: 14
    GDL_ORDER_428_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_428>td.text-center>.unread') # x: 1041 y: 536 width: 6 height: 16
    GDL_ORDER_428_TEXT = (By.CSS_SELECTOR, u'#gdl_order_428>td.text-center>img') # x: 844 y: 537 width: 16 height: 16
    EMBER18675_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18675>.glyphicon-pencil') # x: 1383 y: 537 width: 12 height: 12
    EMBER18708_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18708>.glyphicon-briefcase') # x: 1223 y: 581 width: 14 height: 14
    ID_EMBER18712 = (By.ID, u'ember18712') # x: 1303 y: 594 width: 70 height: 30
    GDL_ORDER_446_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_446>td>.btn-group>.btn-danger') # x: 1405 y: 594 width: 58 height: 30
    EMBER19417 = (By.CSS_SELECTOR, u'#ember19417>.img') # x: 1169 y: 597 width: 24 height: 24
    GDL_ORDER_446_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_446>td.text-center>.unread') # x: 1041 y: 601 width: 6 height: 16
    GDL_ORDER_446_TEXT = (By.CSS_SELECTOR, u'#gdl_order_446>td.text-center>img') # x: 844 y: 602 width: 16 height: 16
    EMBER18714_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18714>.glyphicon-pencil') # x: 1383 y: 602 width: 12 height: 12
    EMBER18747_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18747>.glyphicon-briefcase') # x: 1223 y: 646 width: 14 height: 14
    ID_EMBER18751 = (By.ID, u'ember18751') # x: 1303 y: 659 width: 70 height: 30
    GDL_ORDER_447_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_447>td>.btn-group>.btn-danger') # x: 1405 y: 659 width: 58 height: 30
    EMBER19420 = (By.CSS_SELECTOR, u'#ember19420>.img') # x: 1169 y: 662 width: 24 height: 24
    GDL_ORDER_447_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_447>td.text-center>.unread') # x: 1041 y: 666 width: 6 height: 16
    GDL_ORDER_447_TEXT = (By.CSS_SELECTOR, u'#gdl_order_447>td.text-center>img') # x: 844 y: 667 width: 16 height: 16
    EMBER18753_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18753>.glyphicon-pencil') # x: 1383 y: 667 width: 12 height: 12
    EMBER18786_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18786>.glyphicon-briefcase') # x: 1223 y: 711 width: 14 height: 14
    ID_EMBER18790 = (By.ID, u'ember18790') # x: 1303 y: 724 width: 70 height: 30
    GDL_ORDER_554_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_554>td>.btn-group>.btn-danger') # x: 1405 y: 724 width: 58 height: 30
    EMBER19423 = (By.CSS_SELECTOR, u'#ember19423>.img') # x: 1169 y: 727 width: 24 height: 24
    GDL_ORDER_554_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_554>td.text-center>.unread') # x: 1041 y: 731 width: 6 height: 16
    EMBER18792_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18792>.glyphicon-pencil') # x: 1383 y: 732 width: 12 height: 12
    EMBER18825_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18825>.glyphicon-briefcase') # x: 1223 y: 776 width: 14 height: 14
    ID_EMBER18829 = (By.ID, u'ember18829') # x: 1303 y: 789 width: 70 height: 30
    GDL_ORDER_667_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_667>td>.btn-group>.btn-danger') # x: 1405 y: 789 width: 58 height: 30
    EMBER19426 = (By.CSS_SELECTOR, u'#ember19426>.img') # x: 1169 y: 792 width: 24 height: 24
    GDL_ORDER_667_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_667>td.text-center>.unread') # x: 1041 y: 796 width: 6 height: 16
    EMBER18831_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18831>.glyphicon-pencil') # x: 1383 y: 797 width: 12 height: 12
    EMBER18867_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18867>.glyphicon-briefcase') # x: 1223 y: 841 width: 14 height: 14
    ID_EMBER18871 = (By.ID, u'ember18871') # x: 1303 y: 854 width: 70 height: 30
    GDL_ORDER_668_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_668>td>.btn-group>.btn-danger') # x: 1405 y: 854 width: 58 height: 30
    EMBER19429 = (By.CSS_SELECTOR, u'#ember19429>.img') # x: 1169 y: 857 width: 24 height: 24
    ID_GDL_ORDER_668 = (By.XPATH, u'id(\'gdl_order_668\')/TD[3]/SPAN[1]') # x: 620 y: 861 width: 5 height: 16
    GDL_ORDER_668_GLYPHICON_EARPHONE = (By.CSS_SELECTOR, u'#gdl_order_668>td>a>.glyphicon-earphone') # x: 629 y: 861 width: 14 height: 14
    GDL_ORDER_668_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_668>td.text-center>.unread') # x: 1041 y: 861 width: 6 height: 16
    GDL_ORDER_668_TEXT = (By.CSS_SELECTOR, u'#gdl_order_668>td.text-center>img') # x: 844 y: 862 width: 16 height: 16
    EMBER18873_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18873>.glyphicon-pencil') # x: 1383 y: 862 width: 12 height: 12
    EMBER18906_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18906>.glyphicon-briefcase') # x: 1223 y: 906 width: 14 height: 14
    EMBER19432_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19432>.glyphicon-certificate') # x: 1157 y: 916 width: 14 height: 14
    ID_EMBER18909 = (By.ID, u'ember18909') # x: 1303 y: 919 width: 70 height: 30
    GDL_ORDER_686_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_686>td>.btn-group>.btn-danger') # x: 1405 y: 919 width: 58 height: 30
    GDL_ORDER_686_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_686>td.text-center>.unread') # x: 993 y: 926 width: 6 height: 16
    EMBER18911_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18911>.glyphicon-pencil') # x: 1383 y: 927 width: 12 height: 12
    EMBER18944_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18944>.glyphicon-briefcase') # x: 1223 y: 971 width: 14 height: 14
    EMBER19434_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19434>.glyphicon-certificate') # x: 1157 y: 981 width: 14 height: 14
    ID_EMBER18947 = (By.ID, u'ember18947') # x: 1303 y: 984 width: 70 height: 30
    GDL_ORDER_688_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_688>td>.btn-group>.btn-danger') # x: 1405 y: 984 width: 58 height: 30
    GDL_ORDER_688_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_688>td.text-center>.unread') # x: 993 y: 991 width: 6 height: 16
    EMBER18949_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18949>.glyphicon-pencil') # x: 1383 y: 992 width: 12 height: 12
    EMBER18982_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember18982>.glyphicon-briefcase') # x: 1223 y: 1036 width: 14 height: 14
    EMBER19436_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19436>.glyphicon-certificate') # x: 1157 y: 1046 width: 14 height: 14
    ID_EMBER18985 = (By.ID, u'ember18985') # x: 1303 y: 1049 width: 70 height: 30
    GDL_ORDER_691_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_691>td>.btn-group>.btn-danger') # x: 1405 y: 1049 width: 58 height: 30
    GDL_ORDER_691_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_691>td.text-center>.unread') # x: 993 y: 1056 width: 6 height: 16
    EMBER18987_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember18987>.glyphicon-pencil') # x: 1383 y: 1057 width: 12 height: 12
    EMBER19020_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19020>.glyphicon-briefcase') # x: 1223 y: 1101 width: 14 height: 14
    EMBER19438_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19438>.glyphicon-certificate') # x: 1157 y: 1111 width: 14 height: 14
    ID_EMBER19023 = (By.ID, u'ember19023') # x: 1303 y: 1114 width: 70 height: 30
    GDL_ORDER_765_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_765>td>.btn-group>.btn-danger') # x: 1405 y: 1114 width: 58 height: 30
    GDL_ORDER_765_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_765>td.text-center>.unread') # x: 993 y: 1121 width: 6 height: 16
    EMBER19025_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19025>.glyphicon-pencil') # x: 1383 y: 1122 width: 12 height: 12
    EMBER19058_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19058>.glyphicon-briefcase') # x: 1223 y: 1166 width: 14 height: 14
    EMBER19440_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19440>.glyphicon-certificate') # x: 1157 y: 1176 width: 14 height: 14
    ID_EMBER19061 = (By.ID, u'ember19061') # x: 1303 y: 1179 width: 70 height: 30
    GDL_ORDER_800_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_800>td>.btn-group>.btn-danger') # x: 1405 y: 1179 width: 58 height: 30
    GDL_ORDER_800_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_800>td.text-center>.unread') # x: 993 y: 1186 width: 6 height: 16
    EMBER19063_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19063>.glyphicon-pencil') # x: 1383 y: 1187 width: 12 height: 12
    EMBER19096_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19096>.glyphicon-briefcase') # x: 1223 y: 1231 width: 14 height: 14
    EMBER19442_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19442>.glyphicon-certificate') # x: 1157 y: 1241 width: 14 height: 14
    ID_EMBER19099 = (By.ID, u'ember19099') # x: 1303 y: 1244 width: 70 height: 30
    GDL_ORDER_836_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_836>td>.btn-group>.btn-danger') # x: 1405 y: 1244 width: 58 height: 30
    GDL_ORDER_836_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_836>td.text-center>.unread') # x: 993 y: 1251 width: 6 height: 16
    EMBER19101_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19101>.glyphicon-pencil') # x: 1383 y: 1252 width: 12 height: 12
    EMBER19134_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19134>.glyphicon-briefcase') # x: 1223 y: 1296 width: 14 height: 14
    EMBER19444_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19444>.glyphicon-certificate') # x: 1157 y: 1306 width: 14 height: 14
    ID_EMBER19137 = (By.ID, u'ember19137') # x: 1303 y: 1309 width: 70 height: 30
    GDL_ORDER_879_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_879>td>.btn-group>.btn-danger') # x: 1405 y: 1309 width: 58 height: 30
    GDL_ORDER_879_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_879>td.text-center>.unread') # x: 993 y: 1316 width: 6 height: 16
    EMBER19139_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19139>.glyphicon-pencil') # x: 1383 y: 1317 width: 12 height: 12
    EMBER19172_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19172>.glyphicon-briefcase') # x: 1223 y: 1361 width: 14 height: 14
    EMBER19446_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19446>.glyphicon-certificate') # x: 1157 y: 1371 width: 14 height: 14
    ID_EMBER19175 = (By.ID, u'ember19175') # x: 1303 y: 1374 width: 70 height: 30
    GDL_ORDER_885_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_885>td>.btn-group>.btn-danger') # x: 1405 y: 1374 width: 58 height: 30
    GDL_ORDER_885_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_885>td.text-center>.unread') # x: 993 y: 1381 width: 6 height: 16
    GDL_ORDER_885_TEXT = (By.CSS_SELECTOR, u'#gdl_order_885>td.text-center>img') # x: 844 y: 1382 width: 16 height: 16
    EMBER19177_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19177>.glyphicon-pencil') # x: 1383 y: 1382 width: 12 height: 12
    EMBER19210_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19210>.glyphicon-briefcase') # x: 1223 y: 1426 width: 14 height: 14
    EMBER19448_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19448>.glyphicon-certificate') # x: 1157 y: 1436 width: 14 height: 14
    ID_EMBER19213 = (By.ID, u'ember19213') # x: 1303 y: 1439 width: 70 height: 30
    GDL_ORDER_886_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_886>td>.btn-group>.btn-danger') # x: 1405 y: 1439 width: 58 height: 30
    GDL_ORDER_886_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_886>td.text-center>.unread') # x: 993 y: 1446 width: 6 height: 16
    EMBER19215_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19215>.glyphicon-pencil') # x: 1383 y: 1447 width: 12 height: 12
    EMBER19248_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19248>.glyphicon-briefcase') # x: 1223 y: 1491 width: 14 height: 14
    EMBER19450_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19450>.glyphicon-certificate') # x: 1157 y: 1501 width: 14 height: 14
    ID_EMBER19251 = (By.ID, u'ember19251') # x: 1303 y: 1504 width: 70 height: 30
    GDL_ORDER_887_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_887>td>.btn-group>.btn-danger') # x: 1405 y: 1504 width: 58 height: 30
    GDL_ORDER_887_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_887>td.text-center>.unread') # x: 993 y: 1511 width: 6 height: 16
    EMBER19253_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19253>.glyphicon-pencil') # x: 1383 y: 1512 width: 12 height: 12
    EMBER19286_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19286>.glyphicon-briefcase') # x: 1223 y: 1556 width: 14 height: 14
    EMBER19452_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19452>.glyphicon-certificate') # x: 1157 y: 1566 width: 14 height: 14
    ID_EMBER19289 = (By.ID, u'ember19289') # x: 1303 y: 1569 width: 70 height: 30
    GDL_ORDER_888_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_888>td>.btn-group>.btn-danger') # x: 1405 y: 1569 width: 58 height: 30
    GDL_ORDER_888_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_888>td.text-center>.unread') # x: 993 y: 1576 width: 6 height: 16
    EMBER19291_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19291>.glyphicon-pencil') # x: 1383 y: 1577 width: 12 height: 12
    EMBER19324_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19324>.glyphicon-briefcase') # x: 1223 y: 1621 width: 14 height: 14
    EMBER19454_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19454>.glyphicon-certificate') # x: 1157 y: 1631 width: 14 height: 14
    ID_EMBER19327 = (By.ID, u'ember19327') # x: 1303 y: 1634 width: 70 height: 30
    GDL_ORDER_898_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_898>td>.btn-group>.btn-danger') # x: 1405 y: 1634 width: 58 height: 30
    GDL_ORDER_898_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_898>td.text-center>.unread') # x: 993 y: 1641 width: 6 height: 16
    EMBER19329_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19329>.glyphicon-pencil') # x: 1383 y: 1642 width: 12 height: 12
    EMBER19362_GLYPHICON_BRIEFCASE = (By.CSS_SELECTOR, u'#ember19362>.glyphicon-briefcase') # x: 1223 y: 1686 width: 14 height: 14
    EMBER19456_GLYPHICON_CERTIFICATE = (By.CSS_SELECTOR, u'#ember19456>.glyphicon-certificate') # x: 1157 y: 1696 width: 14 height: 14
    ID_EMBER19365 = (By.ID, u'ember19365') # x: 1303 y: 1699 width: 70 height: 30
    GDL_ORDER_899_BTN_GROUP_DANGER_DELETE = (By.CSS_SELECTOR, u'#gdl_order_899>td>.btn-group>.btn-danger') # x: 1405 y: 1699 width: 58 height: 30
    GDL_ORDER_899_TEXT_UNREAD = (By.CSS_SELECTOR, u'#gdl_order_899>td.text-center>.unread') # x: 993 y: 1706 width: 6 height: 16
    EMBER19367_GLYPHICON_PENCIL = (By.CSS_SELECTOR, u'#ember19367>.glyphicon-pencil') # x: 1383 y: 1707 width: 12 height: 12
    ID_RETAILER_CONTENT_FLOATED = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[5]/DIV[1]/DIV[1]/BUTTON[1]') # x: 308 y: 1798 width: 34 height: 34
    CONTAINS_TEXT_1 = (By.XPATH, u'//button[contains(text(),"1")]') # x: 342 y: 1798 width: 34 height: 34
    CONTAINS_TEXT_2 = (By.XPATH, u'//button[contains(text(),"2")]') # x: 376 y: 1798 width: 34 height: 34
    CONTAINS_TEXT_3 = (By.XPATH, u'//button[contains(text(),"3")]') # x: 410 y: 1798 width: 34 height: 34
    ID_RETAILER_CONTENT_FLOATED_0 = (By.XPATH, u'id(\'retailer-content-floated\')/DIV[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[5]/DIV[1]/DIV[1]/BUTTON[5]') # x: 444 y: 1798 width: 34 height: 34
    CONTAINS_TEXT_0 = (By.XPATH, u'//span[contains(text(),"«")]') # x: 321 y: 1807 width: 8 height: 16
    CONTAINS_TEXT = (By.XPATH, u'//span[contains(text(),"»")]') # x: 457 y: 1807 width: 8 height: 16



    def syota_customer_name(self, parameters=None):
        self.type(self.ID_EMBER1317, parameters)

    def tarkista_details_painike(self):
        self.wait_for_visible(self.ID_EMBER18631)
