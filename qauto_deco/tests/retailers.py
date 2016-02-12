# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from time import sleep
from pagemodel.open_application import Open_application
from pagemodel.set_prices import Set_prices
from pagemodel.retailers import Retailers
from pagemodel.kauppias_login import Kauppias_login

class Retailers(BaseTest):
    parameters = get_all_parameters()
    common_utils = CommonUtils()
    open_application = Open_application()
    set_prices = Set_prices()
    retailers = Retailers()
    kauppias_login = Kauppias_login()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_retailers(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
        # sisäänkirjautuminen
        self.kauppias_login.input_text_username_field(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.input_text_password_field(self.parameters[u'kauppias_login'][u'pwd'])
        self.kauppias_login.click_element_login_button()
        # retailers linkki
        self.retailers.click_element_retailers_link()
        # kosti testaa -linkki
        self.retailers.wait_until_element_is_visible_kosti_testaa_link()
