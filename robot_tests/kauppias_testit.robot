*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Search By Customer Name Or By Reference Number
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Syötä Customer Name Ja Tarkista Tulokset        Testiautomaatio    €549.00
    [Teardown]    Close Browser

Search Orders By Filters
	[Tags]  kehitys
	Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
	Klikkaa Track Orders
	Valitse Creator Ja Tarkista Tulokset            Managers    Maarit Ilola
	[Teardown]    Close Browser


