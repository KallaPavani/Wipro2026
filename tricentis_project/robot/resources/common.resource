*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
#${BASE_URL}    http://demowebshop.tricentis.com
#${BROWSER}     chrome

#${BASE_URL}    https://demowebshop.tricentis.com
#${BROWSER}     firefox

${BASE_URL}    https://demowebshop.tricentis.com
${BROWSER}     edge

*** Keywords ***
Open Browser To Application

    IF    '${BROWSER}' == 'chrome'
        ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
        Call Method    ${options}    add_argument    --ignore-certificate-errors
        Call Method    ${options}    add_argument    --allow-insecure-localhost
        Create Webdriver    Chrome    options=${options}

    ELSE IF    '${BROWSER}' == 'edge'
        ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys
        Call Method    ${options}    add_argument    --ignore-certificate-errors
        Call Method    ${options}    add_argument    --allow-insecure-localhost
        Create Webdriver    Edge    options=${options}

    ELSE IF    '${BROWSER}' == 'firefox'
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys
    Call Method    ${options}    set_preference    dom.webnotifications.enabled    False
    Call Method    ${options}    set_preference    security.enterprise_roots.enabled    True
    Create Webdriver    Firefox    options=${options}

    ELSE
        Fail    Unsupported browser: ${BROWSER}
    END

    Go To    ${BASE_URL}
    Maximize Browser Window
    Set Selenium Timeout        10s
    Set Selenium Implicit Wait  2s
    Set Selenium Speed          0


Close Browser Session
    Close All Browsers


Individual Test Teardown
    Run Keyword If Test Failed    Capture Page Screenshot


# --- Robust Interaction Keywords ---

Click Element Safe
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}    15s
    Wait Until Element Is Enabled    ${locator}    15s
    Click Element    ${locator}

Input Text Safe
    [Arguments]    ${locator}    ${text}
    Wait Until Element Is Visible    ${locator}    15s
    Clear Element Text    ${locator}
    Input Text    ${locator}    ${text}

Wait And Verify Text
    [Arguments]    ${text}
    Wait Until Page Contains    ${text}    15s
    Page Should Contain    ${text}