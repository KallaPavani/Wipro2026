*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}   https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}   chrome
${Username}   Admin
${Password}   admin123

*** Keywords ***
open orangehrm
     Open Browser   ${url}  ${browser}
     Maximize Browser Window
orangehrmlogin
      [Arguments]   ${Username}      ${Password}
      Input Text    name=username    ${Username}
      Input Text    name=password    ${Password}
      Sleep    5s
      Capture Page Screenshot   ./Robot_Framework/before_orangehrmlogin.png
      Click Button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
      Sleep    5s
      Capture Page Screenshot    ./Robot_Framework/after_orangehrmlogin.png
      Sleep    5s
      Close Browser

*** Test Cases ***
TC_005_DataDriven.robot
       open orangehrm
       sleep    5s
       orangehrmlogin    Admin     Admin123