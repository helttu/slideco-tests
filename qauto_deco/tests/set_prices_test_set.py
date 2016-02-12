# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from time import sleep
from pagemodel.open_application import Open_application
from pagemodel.kauppias_login import Kauppias_login
from pagemodel.kauppias_account import Kauppias_account
from pagemodel.track_orders import Track_orders
from pagemodel.set_prices import Set_prices

class Set_prices_test_set(BaseTest):
    parameters = get_all_parameters()
    common_utils = CommonUtils()
    open_application = Open_application()
    kauppias_login = Kauppias_login()
    kauppias_account = Kauppias_account()
    track_orders = Track_orders()
    set_prices = Set_prices()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dont_allow_string_values(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
        # sisäänkirjautuminen
        self.kauppias_login.input_text_username_field(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.input_text_password_field(self.parameters[u'kauppias_login'][u'pwd'])
        self.kauppias_login.click_element_login_button()
        # valitse set prices
        self.set_prices.click_element_set_prices_link()
        self.set_prices.wait_until_element_is_visible_vat_multiplier_field()
        # syötä merkkijono
        self.set_prices.input_text_vat_multiplier_field(self.parameters[u'set_prices'][u'vat_multiplier'])
