*** Settings ***
Library   SeleniumLibrary
Library   DataDriver    file=./testdata.xlsx    sheet_name=Sheet1
Test Template   OrangeHRM Login With Excel
Suite Setup     Open OrangeHRM
Suite Teardown  Close OrangeHRM

*** Variables ***
${URL}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}  chrome

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s

OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains    Dashboard    10s

Close OrangeHRM
    Close Browser

*** Test Cases ***
Login Test Using Excel
      Log    Executed via DataDriver
