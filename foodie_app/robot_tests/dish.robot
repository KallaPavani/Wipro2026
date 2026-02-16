*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://localhost:5000

*** Test Cases ***
Reset Application
    Create Session    foodie    ${BASE_URL}
    POST On Session    foodie    /api/v1/reset

Add Dish
    ${restaurant}=    Create Dictionary
    ...    name=Dish Hotel
    ...    category=Indian
    ...    location=Hyderabad
    ...    contact=9999999999

    ${res}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${restaurant}

    ${restaurant_id}=    Set Variable    ${res.json()["id"]}

    ${dish}=    Create Dictionary
    ...    name=Biryani
    ...    type=Main Course
    ...    price=250
    ...    available_time=Lunch

    ${response}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants/${restaurant_id}/dishes
    ...    json=${dish}

    Status Should Be    201    ${response}
