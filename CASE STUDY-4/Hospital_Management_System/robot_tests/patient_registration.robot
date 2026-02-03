*** Settings ***
Library    SeleniumLibrary

Suite Setup     Open Browser Suite
Suite Teardown  Close Browser Suite
Test Setup      Start Test
Test Teardown   End Test

*** Variables ***
${URL}       https://the-internet.herokuapp.com/login
${BROWSER}   chrome

*** Keywords ***
Open Browser Suite
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Capture Page Screenshot    #After browser launch

Close Browser Suite
    Capture Page Screenshot    #Before browser closes
    Close Browser

Start Test
    Log    Test Started
    Capture Page Screenshot    #Test start

End Test
    Capture Page Screenshot    #Test ends
    Log    Test Finished

*** Test Cases ***
Register Patient Form
    [Tags]    smoke
    Input Text    id:username    tomsmith
    Input Text    id:password    SuperSecretPassword!
    Capture Page Screenshot    #Credentials entered
    Click Button    css:button[type="submit"]
    Capture Page Screenshot    #After submit
