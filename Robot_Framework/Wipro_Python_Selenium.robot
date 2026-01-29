*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Sleep    3s

*** Test Cases ***
tc001.robot
    Open Application
    Title Should Be    Google
    Sleep    3s
    Close Browser
