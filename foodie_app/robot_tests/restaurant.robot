*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://localhost:5000

*** Test Cases ***
Reset Application
    Create Session    foodie    ${BASE_URL}
    POST On Session    foodie    /api/v1/reset

Add Restaurant
    ${restaurant}=    Create Dictionary
    ...    name=Test Hotel
    ...    category=Indian
    ...    location=Hyderabad
    ...    contact=9999999999

    ${response}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${restaurant}

    Status Should Be    201    ${response}
