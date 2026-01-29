*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}   https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}   chrome
${username}  admin
${password}  admin123

*** Test Cases ***
TC_004.robot
    Open Browser   ${url}  ${browser}
    sleep  10s
    Input Text     ${username}   name=username
    Input Text     ${password}   name=password
    Click Button   xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
    Close Browser


