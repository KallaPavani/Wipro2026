*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Simple Browser Test
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Title Should Be    Google
    Capture Page Screenshot
    Close Browser
