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
        # sisäänkirjautuminen
        self.kauppias_login.input_text_username_field(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.input_text_password_field(self.parameters[u'kauppias_login'][u'pwd'])
        self.kauppias_login.click_login_button()
        # track orders linkki
        self.kauppias_account.click_element_track_orders_link()
        # customer name
        self.track_orders.input_text_reference_customer_name_field(self.parameters[u'track_orders'][u'cust_name'])
        sleep(2)
        # tarkistus
        self.track_orders.wait_until_element_is_visible_kodin_terra_link()

    def test_sort_orders_by_date(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
        # sisäänkirjautuminen
        self.kauppias_login.input_text_username_field(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.input_text_password_field(self.parameters[u'kauppias_login'][u'pwd'])
        self.kauppias_login.click_login_button()
        # valitse track orders
        self.kauppias_account.click_element_track_orders_link()
        # klikkaa descending ja tarkista ascending-linkki
        self.track_orders.click_element_descending()
        self.track_orders.wait_until_element_is_visible_ascending()
        # klikkaa ascending ja tarkista kodin terra -linkki
        self.track_orders.click_element_ascending()
        self.track_orders.wait_until_element_is_visible_kodin_terra_link()

    def test_search_orders_by_filters(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
        # sisäänkirjautuminen
        self.kauppias_login.input_text_username_field(self.parameters[u'kauppias_login'][u'user'])
        self.kauppias_login.input_text_password_field(self.parameters[u'kauppias_login'][u'pwd'])
        self.kauppias_login.click_login_button()
        # valitse track orders
        self.kauppias_account.click_element_track_orders_link()
        self.track_orders.wait_until_element_is_visible_creator_list()
        # todo: valitse customer listasta
        self.track_orders.select_from_list_by_label_creator_list(self.parameters[u'track_orders'][u'creator_list'])
        self.track_orders.wait_until_element_is_visible_reg_kodin_terra_jkl()
