*** Settings ***
Library   SeleniumLibrary
Library   DataDriver    file=registerdata.xlsx    sheet_name=Sheet1
Test Template    Register With Excel
Suite Setup     Open Register Page
Suite Teardown    Close All Browsers

*** Variables ***
${URL}   https://tutorialsninja.com/demo/index.php?route=account/register
${BROWSER}   chrome

*** Keywords ***
Open Register Page
     Open Browser    ${URL}    ${BROWSER}
     Maximize Browser Window
     Sleep    5s
     Wait Until Element Is Visible    id=input-firstname    10s

Register With Excel
     [Arguments]    ${firstname}   ${lastname}    ${email}    ${telephone}   ${password}   ${confirm_password}
     Go To         ${URL}
     Wait Until Element Is Visible   id=input-firstname    15s

     Input Text    id=input-firstname    ${firstname}
     Input Text    id=input-lastname     ${lastname}
     Input Text    id=input-email        ${email}
     Input Text    id=input-telephone    ${telephone}
     Input Text    id=input-password     ${password}
     Input Text    id=input-confirm     ${confirm_password}
     Sleep   2s
     Select Checkbox    name=agree
     Click Button     xpath=//input[@value='Continue']
     Sleep    3s
     Wait Until Page Contains   Your Account Has Been Created!
     Go To    https://tutorialsninja.com/demo/index.php?route=account/logout

*** Test Cases ***
Register Test Using Excel    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}    ${confirm_password}
