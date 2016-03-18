*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Search By Customer Name Or By Reference Number
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Syötä Customer Name Ja Tarkista 				Jesun testi    €608.92
    [Teardown]    Close Browser

Search Orders By Filters
	[Tags]  creator poistettu käyttöliittymästä
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Valitse Creator Ja Tarkista 					Customer    Sanna Salmio Jyväskylä    €718.00
    [Teardown]    Close Browser

Sort Orders By Date
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Valitse Descending Ja Tarkista                  Jesu Testaa
    Valitse Ascending Ja Tarkista                   Maarit Ilola
    [Teardown]    Close Browser
