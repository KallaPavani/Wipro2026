*** Settings ***
Library    SeleniumLibrary

Suite Setup     Open Browser Suite
Suite Teardown    Close Browser Suite

Test Setup
Task Teardown

*** Variables ***
${URL}     https://www.wikipedia.org
${BROWSER}   chrome

*** Keywords ***
Open Browser Suite
    Open Browser   ${URL}   ${BROWSER}
    Maximize Browser Window
    Capture Page Screenshot    # Screenshot after browser launch

Close Browser Suite
    Capture Page Screenshot    # Screenshot before closing browser
    Close Browser

Start Test
    Log    Test Started
    Capture Page Screenshot    # Screenshot at test start

End Test
    Capture Page Screenshot    # Screenshot at test end
    Log    Test Finished

*** Test Cases ***
Valid Form Test
    [Tags]   smoke    regression
    Log    Executing Valid Form Test
    Capture Page Screenshot    # Screenshot during test execution


Another Simple Test
    Log    Executing another test
    Capture Page Screenshot