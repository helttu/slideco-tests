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
	[Tags]  valmis
	Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
	Klikkaa Track Orders
	Valitse Creator Ja Tarkista Tulokset            Managers    Maarit Ilola
	[Teardown]    Close Browser

Sort Orders By Date
	[Tags]  kehitys
	Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
	Klikkaa Track Orders
	Klikkaa Descending Ja Tarkista Pvm    			5 days ago
	Klikkaa Ascending Ja Tarkista Pvm  				8 months ago
	[Teardown]    Close Browser



