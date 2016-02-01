# -*- coding: utf-8 -*-
from webframework.extension.base.baseTest import BaseTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from time import sleep
from pagemodel.open_application import Open_application
from pagemodel.ala_palkki import Ala_palkki
from pagemodel.aloita_suunnitelu import Aloita_suunnitelu
from pagemodel.valinta_kork_ja_lev import Valinta_kork_ja_lev
from pagemodel.valitse_ovien_maara import Valitse_ovien_maara
from pagemodel.liukovet_profiili import Liukovet_profiili
from pagemodel.s100_profiili import S100_profiili
from pagemodel.liukuoven_hidastimet import Liukuoven_hidastimet
from pagemodel.runkoosat import Runkoosat
from pagemodel.ovimallit import Ovimallit
from pagemodel.jakolistat import Jakolistat
from pagemodel.pintamateriaalit import Pintamateriaalit
from pagemodel.maalatut_lasit import Maalatut_lasit
from pagemodel.hinta_ja_laheta import Hinta_ja_laheta
from pagemodel.kehasavy import Kehasavy
from pagemodel.huomio_popup import Huomio_popup
from pagemodel.taustalevyt import Taustalevyt

class Finndeco(BaseTest):
    parameters = get_all_parameters()
    common_utils = CommonUtils()
    open_application = Open_application()
    ala_palkki = Ala_palkki()
    aloita_suunnitelu = Aloita_suunnitelu()
    valinta_kork_ja_lev = Valinta_kork_ja_lev()
    valitse_ovien_maara = Valitse_ovien_maara()
    liukovet_profiili = Liukovet_profiili()
    s100_profiili = S100_profiili()
    liukuoven_hidastimet = Liukuoven_hidastimet()
    runkoosat = Runkoosat()
    ovimallit = Ovimallit()
    jakolistat = Jakolistat()
    pintamateriaalit = Pintamateriaalit()
    maalatut_lasit = Maalatut_lasit()
    hinta_ja_laheta = Hinta_ja_laheta()
    kehasavy = Kehasavy()
    huomio_popup = Huomio_popup()
    taustalevyt = Taustalevyt()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_suunnittelu_liukuovet(self):
        self.open_application.open_application_url(u'http://finndeco.codemen.fi/build/?api=K3JK2FCG')
        self.ala_palkki.wait_for_visible_measure_title_mittaa_ja_rakenna()
        self.aloita_suunnitelu.click_aloita_suunnittelu()
        self.valinta_kork_ja_lev.valitse_korkeus_ja_leveys(self.parameters[u'korkeus_ja_leveys'])
        self.valinta_kork_ja_lev.click_seuraava_vaihe()
        self.valitse_ovien_maara.valitse_ovien_maara(self.parameters[u'ovet'])
        self.valitse_ovien_maara.click_seuraava_vaihe()
        self.liukovet_profiili.valitse_liukuoviprofiili(self.parameters[u'liukuovi_profiili'])
        valittu_profiili = self.parameters[u'liukuovi_profiili'][u'profiili']
        if valittu_profiili == u's100':
            self.s100_profiili.valitse_profiili_materiaali(self.parameters[u'profiili_materiaalit'])
        else:
            pass
        self.liukovet_profiili.click_seuraava_vaihe()
        self.liukuoven_hidastimet.click_seuraava_vaihe()
        self.runkoosat.valitse_runkoosat(self.parameters[u'runkoosat'])
        self.runkoosat.click_seuraava_vaihe()
        self.kehasavy.click_seuraava_vaihe()
        self.ovimallit.valitse_ovimalli(self.parameters[u'ovimallit'])
        self.ovimallit.click_seuraava_vaihe()
        self.jakolistat.valitse_seuraava_vaihe()
        self.pintamateriaalit.valitse_pintamateriaalit(self.parameters[u'pintamateriaalit'])
        self.maalatut_lasit.valitse_pintamateriaali_vaihtoehto(self.parameters[u'pintamateriaalit'])
        self.pintamateriaalit.click_seuraava_vaihe()
        self.huomio_popup.click_jatka()
        self.hinta_ja_laheta.syota_yhteystiedot_ja_tallenna(self.parameters[u'yhteystiedot'])
        sleep(5)
