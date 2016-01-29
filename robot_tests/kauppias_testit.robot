*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Search By Customer Name Or By Reference Number
    [Tags]  kehitys
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Track Orders
    Syötä Customer Name Ja Tarkista Tulokset        Testiautomaatio
    [Teardown]    Close Browser