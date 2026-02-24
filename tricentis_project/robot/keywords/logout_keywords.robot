*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Logout User
    Log    ===== Step: Logging Out =====

    # Wait for the link to ensure the page has loaded
    Wait Until Element Is Visible    xpath://a[text()='Log out']    10s
    Click Link    Log out

    # Verify logout by checking for the Log in link
    Wait Until Element Is Visible    xpath://a[text()='Log in']     10s
    Log    ===== Logout Successful =====