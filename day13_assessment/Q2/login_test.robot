*** Settings ***
Library    SeleniumLibrary
Test Template    Login Using Keywords
Suite Setup    Open Application
Suite Teardown    Close Browser

*** Variables ***
${URL}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}  chrome

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Capture Page Screenshot    open_application.png

Enter Username
    [Arguments]    ${username}
    Wait Until Element Is Visible    name=username    10s
    Input Text    name=username    ${username}
    Capture Page Screenshot    username_entered.png

Enter Password
    [Arguments]    ${password}
    Input Text    name=password    ${password}
    Capture Page Screenshot    password_entered.png

Click Login
    Click Button    xpath=//button[@type='submit']
    Capture Page Screenshot    after_login_click.png

Verify Result
    [Arguments]    ${expected}
    IF    '${expected}' == 'pass'
        Wait Until Page Contains    Dashboard    10s
        Capture Page Screenshot    login_success.png
        Logout From Application
    ELSE
        Wait Until Page Contains    Invalid credentials    10s
        Capture Page Screenshot    login_failed.png
        Reload Page
    END

Logout From Application
    Click Element    xpath=//span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    10s
    Click Element    xpath=//a[text()='Logout']
    Capture Page Screenshot    after_logout.png
    Wait Until Element Is Visible    name=username    10s

Login Using Keywords
    [Arguments]    ${username}    ${password}    ${expected}
    Enter Username    ${username}
    Enter Password    ${password}
    Click Login
    Verify Result     ${expected}

*** Test Cases ***
Login Test From CSV
    [Template]    Login Using Keywords
    Admin    admin123    pass
    Admin    wrong123    fail
    Wrong    admin123    fail
