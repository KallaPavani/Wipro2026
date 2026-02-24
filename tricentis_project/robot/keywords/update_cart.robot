*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Open Cart
    Log    Opening shopping cart
    Wait Until Element Is Not Visible    css:div.bar-notification.success    5s
    Click Element    class:ico-cart
    Wait Until Element Is Visible    class:qty-input    5s
    Log    ===== Cart Page Opened Successfully =====


Update Cart Quantity
    [Arguments]    ${quantity}

    Log    Updating quantity to: ${quantity}

    Wait Until Element Is Visible    class:qty-input    10s
    Clear Element Text    class:qty-input
    Input Text    class:qty-input    ${quantity}

    Click Button    name:updatecart
    Wait Until Page Contains    Shopping cart    10s

    Log    ===== Quantity Updated Successfully =====