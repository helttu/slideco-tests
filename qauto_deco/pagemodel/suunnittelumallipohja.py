# -*- coding: utf-8 -*-
# Example for using WebDriver object: driver = get_driver() e.g driver.current_url
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from webframework.extension.util.webtimings import get_measurements
from webframework.extension.parsers.parameter_parser import get_parameter
from time import sleep

class Suunnittelumallipohja(CommonUtils):
    # Pagemodel timestamp: 20160209092322
    # Pagemodel url: http://finndeco.codemen.fi/build/?api=K3JK2FCG
    # Pagemodel area: Full screen
    # Pagemodel screen resolution: (1920, 1080)
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
    # Pagemodel type: dynamic
    # Links found: 0
    # Page model constants:
    CONTAINS_TEXT_VALINTASI = (By.XPATH, u'//p[contains(text(),"valintasi")]') # x: 96 y: 90 width: 1752 height: 20
    CONTAINS_TEXT_VALITSE_MIELEISESI_MALLI_SUUNNITELMASI_POHJAKSI = (By.XPATH, u'//h2[contains(text(),"Valitse mieleisesi malli ")]') # x: 96 y: 126 width: 1752 height: 35
    BODY_PID_N_KIRJOISTA = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[1]/DIV[1]') # x: 96 y: 304 width: 438 height: 214
    BODY_PID_N_MUSIIKISTA_JA_ELOKUVISTA = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[1]/DIV[2]') # x: 534 y: 304 width: 438 height: 214
    BODY_OMISTAN_PALJON_TAKKEJA = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[1]/DIV[3]') # x: 972 y: 304 width: 438 height: 214
    BODY_PID_N_KAUNIISTA_ALUSVAATTEISTA = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[1]/DIV[4]') # x: 1409 y: 304 width: 438 height: 214
    BODY_KOTITOIMISTO_KUULUU_ARKEENI = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[2]/DIV[1]') # x: 96 y: 535 width: 438 height: 214
    BODY_OLEN_HULLUNA_KENKIIN = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[2]/DIV[2]') # x: 534 y: 535 width: 438 height: 214
    BODY_PALJON_SEKALAISTA_PIKKUTAVARAA = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[2]/DIV[3]') # x: 972 y: 535 width: 438 height: 214
    BODY_MEKOT_JA_PUVUT = (By.XPATH, u'//BODY/SECTION[15]/DIV[1]/DIV[1]/DIV[3]/DIV[2]/DIV[2]/DIV[4]') # x: 1409 y: 535 width: 438 height: 214
    CLASS_DISABLE_ELEMENT = (By.CLASS_NAME, u'disable-element') # x: 0 y: 766 width: 192 height: 68
    CLASS_ELEMENT_RESTART = (By.CLASS_NAME, u'element-restart') # x: 288 y: 766 width: 288 height: 68
    CLASS_ELEMENT_ENABLE = (By.CLASS_NAME, u'element-enable') # x: 1632 y: 766 width: 288 height: 68

    def valitse_suunnitelumallipohja(self, parameters=None):
        if parameters['mallipohja'] == "kirjat":
            self.click_element(self.BODY_PID_N_KIRJOISTA)
        elif parameters['mallipohja'] == "musiikki":
             self.click_element(self.BODY_PID_N_MUSIIKISTA_JA_ELOKUVISTA)
        elif parameters['mallipohja'] == "takit":
             self.click_element(self.BODY_OMISTAN_PALJON_TAKKEJA)
        elif parameters['mallipohja'] == "alusvaatteet":
             self.click_element(self.BODY_PID_N_KAUNIISTA_ALUSVAATTEISTA)
        elif parameters['mallipohja'] == "kotitoimisto":
             self.click_element(self.BODY_KOTITOIMISTO_KUULUU_ARKEENI)
        elif parameters['mallipohja'] == "kengat":
             self.click_element(self.BODY_OLEN_HULLUNA_KENKIIN)
        elif parameters['mallipohja'] == "sekalainen":
             self.click_element(self.BODY_PALJON_SEKALAISTA_PIKKUTAVARAA)
        elif parameters['mallipohja'] == "mekot_puvut":
             self.click_element(self.BODY_MEKOT_JA_PUVUT)
        else:
            self.click_element(self.BODY_PID_N_MUSIIKISTA_JA_ELOKUVISTA)

    def click_seuraava_vaihe(self, parameters=None):
        self.click_element(self.CLASS_ELEMENT_ENABLE)
