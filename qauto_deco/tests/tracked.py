# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from time import sleep
from pagemodel.open_application import Open_application

class Tracked(BaseTest):
    common_utils = CommonUtils()
    open_application = Open_application()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_jijiji(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/manage/')
