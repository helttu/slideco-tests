*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Suunnitelman Tekeminen Ja Komerokoodin Tallennus
    [Tags]  kehitys
    Avaa Wardrobe Builder
    Klikkaa Aloita Suunnittelu Painiketta
    Valitse Korkeus
    Valitse Leveys Ja Klikkaa Seuraava Vaihe
    Valitse Liukuovien Määrä Ja Klikkaa Seuraava Vaihe
    Valitse Mieleisesi Liukuoviprofiili
    Valitse Mieleisesi Profiilisävy Ja Klikkaa Seuraava Vaihe
    Valitse Liukuoven Hidastimet Ja Klikkaa Seuraava Vaihe
    Valitse Runko-osat Ja Klikkaa Seuraava Vaihe
    Valitse Kehäsävy Ja Klikkaa Seuraava Vaihe
    Valitse Mieleisesi Ovimalli Tästä Ja Klikkaa Seuraava Vaihe
    Lisää, Poista Tai Säädä Jakolistoja Mielesi Mukaan Ja Klikkaa Seuraava Vaihe
    Valitse Materiaalit Ja Klikkaa Seuraava Vaihe
    Valitse Runkosävy
    Mihin Käytät Vaatekaappiasi Kysymys 1/2
    Kenen Makuuhuone Kysymys 2/2
    Valitse Mieleisesi Malli Suunnitelmasi Pohjaksi
    Klikkaa Seurava Vaihe Huoneen Kuva Sivulla
    Tallenna Suunnitelma, Lähetä Ja Ota Komerokoodi Talteen
    [Teardown]    Close Browser