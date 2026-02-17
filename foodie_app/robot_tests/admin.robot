*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           String

Suite Setup       Create Session    foodie    http://localhost:5000/api/v1
Suite Teardown    Delete All Sessions


*** Test Cases ***

Admin Approve Restaurant
    [Documentation]    Admin should approve a newly created restaurant

    # Generate Unique Restaurant Name
    ${random}=    Generate Random String    5
    ${restaurant_name}=    Set Variable    TestHotel_${random}

    ${body}=    Create Dictionary    name=${restaurant_name}

    # Step 1: Create Restaurant
    ${create_response}=    POST On Session    foodie    /restaurants    json=${body}    expected_status=any
    Should Be Equal As Integers    ${create_response.status_code}    201

    ${response_json}=    Set Variable    ${create_response.json()}
    ${restaurant_id}=    Get From Dictionary    ${response_json}    id

    Log    Created Restaurant ID: ${restaurant_id}

    # Step 2: Approve Restaurant
    ${approve_response}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/approve    expected_status=any
    Should Be Equal As Integers    ${approve_response.status_code}    200

    Log    Approve Response: ${approve_response.json()}



Admin View Orders
    ${response}=    GET On Session    foodie    /admin/orders
    Should Be Equal As Integers    ${response.status_code}    200


Admin View Ratings
    ${response}=    GET On Session    foodie    /admin/ratings
    Should Be Equal As Integers    ${response.status_code}    200
