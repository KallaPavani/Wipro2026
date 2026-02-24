*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Login User
    [Arguments]    ${email}    ${password}

    Log    ===== Step: Logging in as ${email} =====

    Click Link    Log in
    Wait Until Element Is Visible    id:Email    10s

    Input Text    id:Email       ${email}
    Input Text    id:Password    ${password}

    # Using the value attribute for the login button as it's common in Tricentis
    Click Button    xpath://input[@value='Log in']

    # Verify login was successful by checking for the Logout link
    Wait Until Element Is Visible    xpath://a[text()='Log out']    10s
    Log    ===== Login Successful for ${email} =====