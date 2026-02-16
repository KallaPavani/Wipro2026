*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://localhost:5000

*** Test Cases ***
Reset Application
    Create Session    foodie    ${BASE_URL}
    POST On Session    foodie    /api/v1/reset

Register User
    ${user}=    Create Dictionary
    ...    name=Pavani
    ...    email=pavani@test.com
    ...    phone=9999999999
    ...    address=Hyderabad

    ${response}=    POST On Session
    ...    foodie
    ...    /api/v1/users
    ...    json=${user}

    Status Should Be    201    ${response}
