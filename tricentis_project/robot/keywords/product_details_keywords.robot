*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open First Product Details

    Log    Opening first product from search results

    # Wait until search results are visible
    Wait Until Page Contains Element    css:.product-item    15s

    Click Element    xpath:(//h2[@class='product-title']/a)[1]

    # Wait for product name (more reliable than product-details-page)
    Wait Until Page Contains Element    css:.product-name    15s

    Log    ===== Product Details Page Loaded =====