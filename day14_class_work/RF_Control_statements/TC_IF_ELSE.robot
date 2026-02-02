*** Test Cases ***
IF ELSE EXAMPLE
    ${num}=   Set Variable  20
    IF    ${num} > 20
        Log    Greater than 20
    ELSE
        Log    Less than or equal to 20
    END