*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Search By Customer Name Or By Reference Number
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    	aaa
    Klikkaa Track Orders
    Syötä Customer Name Ja Tarkista 				testaus    					€842.99
    [Teardown]    Close Browser

Sort Orders By Date
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    	aaa
    Klikkaa Track Orders
    Valitse Descending Ja Tarkista                  oinonen mikko
    Valitse Ascending Ja Tarkista                   smoketest
    [Teardown]    Close Browser
