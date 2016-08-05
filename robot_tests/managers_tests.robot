*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Invite Manager And Remove A Manager
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    aaa
    Klikkaa Managers
    Klikkaa Invite Ja Syötä Retailer Email          robot.framework@testiautomaatio.fi
    Poista Manager                                  robot.framework@testiautomaatio.fi
    [Teardown]    Close Browser