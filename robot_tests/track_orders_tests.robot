*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Search By Customer Name Or By Reference Number
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Syötä Customer Name Ja Tarkista 				Testiautomaatio    Testiautomaatio Helsinki    €0.00
    [Teardown]    Close Browser

Search Orders By Filters
	[Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Valitse Creator Ja Tarkista 					Customer    Sanna Salmio Jyväskylä    €718.00
    [Teardown]    Close Browser

Sort Orders By Date
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Valitse Descending Ja Tarkista                  a day ago
    Valitse Ascending Ja Tarkista                   8 months ago
    [Teardown]    Close Browser
