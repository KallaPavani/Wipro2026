*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Add Product To Cart

    Log    Adding product to cart
    Click Element    xpath://input[contains(@class,'add-to-cart-button')]

    Wait Until Page Contains    The product has been added    10s
    Log    ===== Product Added To Cart Successfully =====
