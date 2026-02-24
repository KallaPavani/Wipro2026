*** Settings ***
Library    SeleniumLibrary
Library    String

*** Keywords ***
Register New User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${password}    ${confirm_password}   ${gender}

    # 1. Generate a unique email
    ${random}=    Generate Random String    4    [NUMBERS]
    ${parts}=    Split String    ${email}    @
    ${unique_email}=    Set Variable    ${parts[0]}${random}@${parts[1]}

    Log    ===== Step: Starting Registration for ${unique_email} =====

    Click Link    xpath://a[text()='Register']
    Wait Until Element Is Visible    id:FirstName    10s

    # Select gender dynamically
    Run Keyword If    '${gender}' == 'Male'      Click Element    id:gender-male
    Run Keyword If    '${gender}' == 'Female'    Click Element    id:gender-female

    Input Text    id:FirstName    ${firstname}
    Input Text    id:LastName     ${lastname}
    Input Text    id:Email        ${unique_email}
    Input Text    id:Password     ${password}
    Input Text    id:ConfirmPassword    ${confirm_password}

    Click Button    id:register-button

    Wait Until Page Contains    Your registration completed    10s
    Log    ===== Registration Successful for ${unique_email} =====

    # 2. Return the unique email to the main test flow
    RETURN    ${unique_email}