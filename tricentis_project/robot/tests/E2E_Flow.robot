*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../variables/users.csv    encoding=utf-8    dialect=unix
Resource   ../keywords/register_keywords.robot
Resource   ../keywords/login_keywords.robot
Resource   ../keywords/search_keywords.robot
Resource   ../keywords/product_details_keywords.robot
Resource   ../keywords/add_to_cart_keywords.robot
Resource   ../keywords/update_cart.robot
Resource   ../keywords/remove_from_cart_keywords.robot
Resource   ../keywords/logout_keywords.robot
Resource   ../resources/common.resource
Test Template     Execute Complete Flow
Test Setup        Open Browser To Application
Test Teardown     Close Browser Session
#Test Teardown    Individual Test Teardown

*** Test Cases ***
Complete E2E Flow for ${firstname}

*** Keywords ***
Execute Complete Flow
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${password}    ${confirm_password}  ${gender}  ${search_item}    ${quantity}
    Log    ===== Starting Complete E2E Flow =====

    # 1. Capture the unique email
    ${generated_email}=    Register New User    ${firstname}    ${lastname}    ${email}    ${password}    ${confirm_password}   ${gender}

    Logout User
    Login User    ${generated_email}    ${password}
    Search Product    ${search_item}
    Open First Product Details
    Add Product To Cart

    Open Cart
    # 2. Use the quantity variable here
    Update Cart Quantity    ${quantity}

    Remove Item From Cart
    Logout User

#robot -d results2/chrome -v BROWSER:chrome E2E_flow.robot
#robot -d results2/firefox -v BROWSER:firefox E2E_flow.robot
#robot -d results2/edge -v BROWSER:edge E2E_flow.robot