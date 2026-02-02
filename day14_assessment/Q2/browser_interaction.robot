*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Form Interaction Using Selenium
    Open Browser    https://formy-project.herokuapp.com/form    chrome
    Maximize Browser Window

    Input Text    id:first-name    Pavani
    Input Text    id:last-name     Kalla
    Capture Page Screenshot    # after text input

    Click Element    id:radio-button-2
    Capture Page Screenshot    # after radio button selection

    Click Element    id:checkbox-1
    Capture Page Screenshot    # after checkbox selection

    Select From List By Value    id:select-menu    2
    Capture Page Screenshot    # after dropdown selection

    Run Keyword If    '${True}'=='${True}'    Log    Form filled successfully

    Close Browser
