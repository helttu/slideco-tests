*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Navigate To Dashboard And List Incoming Customer Orders
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa REG Kodin Terra Jyväskylä Dashboard
    Klikkaa Track Orders
    [Teardown]    Close Browser

Navigate To Dashboard And Display All Variations
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa REG Kodin Terra Jyväskylä Dashboard
    Klikkaa See Variations
    [Teardown]    Close Browser

Navigate To Dashboard And List Applications
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa REG Kodin Terra Jyväskylä Dashboard
    Klikkaa Configure Applications
    [Teardown]    Close Browser

Navigate To Dashboard And List Retailers
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa REG Kodin Terra Jyväskylä Dashboard
    Klikkaa Retailers
    [Teardown]    Close Browser

Navigate To Dashboard And Open Set Prices Page
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa REG Kodin Terra Jyväskylä Dashboard
    Klikkaa Set Prices
    [Teardown]    Close Browser

Navigate To Dashboard And List Users
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa REG Kodin Terra Jyväskylä Dashboard
    Klikkaa Managers
    [Teardown]    Close Browser

Navigate To Dashboard And Open My Account Page
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    FinnDSami#9
    Klikkaa REG Kodin Terra Jyväskylä Dashboard
    Klikkaa My Account
    [Teardown]    Close Browser