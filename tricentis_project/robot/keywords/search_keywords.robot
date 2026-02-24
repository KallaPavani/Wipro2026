*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Search Product
    [Arguments]    ${search_item}
    Log    ===== Step: Searching for ${search_item} =====

    Wait Until Element Is Visible    id:small-searchterms    10s
    Input Text      id:small-searchterms    ${search_item}
    Click Button    xpath://input[@value='Search']

    # Verify that the search results page loaded
    Wait Until Page Contains    ${search_item}    10s
    Page Should Contain    ${search_item}