*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://localhost:5000

*** Test Cases ***
Reset Application
    Create Session    foodie    ${BASE_URL}
    POST On Session    foodie    /api/v1/reset

Place Order
    # Create Restaurant
    ${restaurant}=    Create Dictionary
    ...    name=Order Hotel
    ...    category=Indian
    ...    location=Hyderabad
    ...    contact=9999999999

    ${res}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${restaurant}

    ${restaurant_id}=    Set Variable    ${res.json()["id"]}

    # Create Dish
    ${dish}=    Create Dictionary
    ...    name=Biryani
    ...    type=Main Course
    ...    price=250
    ...    available_time=Lunch

    ${dish_res}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants/${restaurant_id}/dishes
    ...    json=${dish}

    ${dish_id}=    Set Variable    ${dish_res.json()["id"]}

    # Create User
    ${user}=    Create Dictionary
    ...    name=Pavani
    ...    email=pavani@test.com
    ...    phone=9999999999
    ...    address=Hyderabad

    ${user_res}=    POST On Session
    ...    foodie
    ...    /api/v1/users
    ...    json=${user}

    ${user_id}=    Set Variable    ${user_res.json()["id"]}

    ${dish_list}=    Create List    ${dish_id}

    ${order}=    Create Dictionary
    ...    user_id=${user_id}
    ...    restaurant_id=${restaurant_id}
    ...    dish_ids=${dish_list}



    ${response}=    POST On Session
    ...    foodie
    ...    /api/v1/orders
    ...    json=${order}

    Status Should Be    201    ${response}
