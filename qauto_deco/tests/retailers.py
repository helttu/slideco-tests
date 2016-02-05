# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from time import sleep
from pagemodel.open_application import Open_application
from pagemodel.set_prices import Set_prices

class Retailers(BaseTest):
    parameters = get_all_parameters()
    common_utils = CommonUtils()
    open_application = Open_application()
    set_prices = Set_prices()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_retailers(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
        # syötä username ja password
        self.kauppias_login.syota_userid(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.syota_pwd(self.parameters[u'kauppias_login'][u'pwd'])
        # klikkaa login-painiketta
        self.kauppias_login.klikkaa_login_painiketta()
        # valitse retailers
        self.set_prices.click_set_prices_link()
