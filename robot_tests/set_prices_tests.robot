*** Settings ***
Resource          ../robot_resources/common_resource.robot

*** Test Cases ***
Don't Allow String Values
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    aaa
    Klikkaa Set Prices
    Syötä Merkkijono VAT Multiplier Kenttään        twenty-three
    Tarkista Että Merkkijonoa Ei Hyväksytä
    [Teardown]    Close Browser

Don't Allow Empty Values
    [Tags]  valmis
    Sisäänkirjaudu Slideco Management System        sami.stedt@q-factory.fi    aaa
    Klikkaa Set Prices
    Syötä Merkkijono VAT Multiplier Kenttään        \
    Tarkista Että Merkkijonoa Ei Hyväksytä
    [Teardown]    Close Browser



