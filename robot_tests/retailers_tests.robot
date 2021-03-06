*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
List Retailers
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    aaa
    Klikkaa Retailers
    Tarkista Retailersien Listaus                   Kosti testaa        REG, JKL Keskusta    REG, JKL Uimaharju    REG, JKL Pupuhuhta    REG, JKL Saarela
    [Teardown]    Close Browser

Head Retailer Shorcuts
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    aaa
    Klikkaa Retailers
    Klikkaa Edit ja Tarkista Tiedot                 Kosti testaa
    [Teardown]    Close Browser

