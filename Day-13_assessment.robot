Language: English
*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
TC_Browser_Test
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Title Should Be    Google
    Capture Page Screenshot
    Close Browser
