*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TC_002.robot
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google
    Close Browser
