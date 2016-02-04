*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Invite Manager And Remove A Manager
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa Managers
    Klikkaa Invite Ja Syötä Retailer Email          testi@automaatio.fi
    Poista Manager                                  testi@automaatio.fi
    [Teardown]    Close Browser