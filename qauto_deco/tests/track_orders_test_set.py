# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from time import sleep
from pagemodel.open_application import Open_application
from pagemodel.kauppias_login import Kauppias_login
from pagemodel.kauppias_account import Kauppias_account
from pagemodel.track_orders import Track_orders

class Track_orders_test_set(BaseTest):
    parameters = get_all_parameters()
    common_utils = CommonUtils()
    open_application = Open_application()
    kauppias_login = Kauppias_login()
    kauppias_account = Kauppias_account()
    track_orders = Track_orders()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search_by_cust_name_or_by_ref_number(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
        # syötä username ja password
        self.kauppias_login.syota_userid(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.syota_pwd(self.parameters[u'kauppias_login'][u'pwd'])
        # klikkaa Login-painiketta
        self.kauppias_login.klikkaa_login_painiketta()
        # valitse Track orders
        self.kauppias_account.klikkaa_track_orders()
        # syötä Customer name
        self.track_orders.type_ref_cust_name(self.parameters[u'track_orders'][u'ref_cust_name'])
        # tarkista order
        self.track_orders.wait_for_visible_reg_kodin_terra_jkl_linkki()

    def test_search_orders_by_filters(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
        # syötä username ja password
        self.kauppias_login.syota_userid(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.syota_pwd(self.parameters[u'kauppias_login'][u'pwd'])
        # klikkaa Login-painiketta
        self.kauppias_login.klikkaa_login_painiketta()
        # valitse Track orders
        self.kauppias_account.klikkaa_track_orders()
        #
