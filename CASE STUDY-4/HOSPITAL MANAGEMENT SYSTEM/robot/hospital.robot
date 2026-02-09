*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Application
Suite Teardown    Close Browser

*** Variables ***
${URL}     http://127.0.0.1:5002
${BROWSER}   chrome

*** Test Cases ***
Patient Registration Flow
    Capture Page Screenshot
    Sleep    2s

    Fill Patient Registration Form
    Capture Page Screenshot
    Sleep    2s

    Submit Form
    Sleep    3s
    Capture Page Screenshot


*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Fill Patient Registration Form
    Input Text    name=name       Pavani
    Input Text    name=age        23
    Click Element    xpath=//input[@value='Female']
    Input Text    name=contact    9876543210
    Input Text    name=disease    Fever
    Input Text    name=doctor     Dr. Rao

Submit Form
    Click Button    xpath=//button[text()='Register Patient']
