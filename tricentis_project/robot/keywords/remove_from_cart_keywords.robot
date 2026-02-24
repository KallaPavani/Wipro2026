*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Remove Item From Cart
    Log    ===== Step: Removing Item from Cart =====

    Wait Until Element Is Visible    name:removefromcart    10s
    Select Checkbox    name:removefromcart
    Click Button       name:updatecart

    # Verify the cart is empty
    Wait Until Page Contains    Your Shopping Cart is empty!    10s
    Log    ===== Cart Cleared =====