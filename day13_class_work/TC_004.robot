*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}   https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}   chrome
${username}   Admin
${password}   admin123

*** Test Cases ***
TC_004.robot
   Open Browser   ${url}   ${browser}
   sleep    10s
   Input Text    name=username   ${username}
   Input Text    name=password   ${password}
   sleep    10s
   Capture Page Screenshot   ./Robot_Framework/before_login.png
   Click Button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
   sleep    10s
   Capture Page Screenshot   ./Robot_Framework/after_login.png
   Close Browser