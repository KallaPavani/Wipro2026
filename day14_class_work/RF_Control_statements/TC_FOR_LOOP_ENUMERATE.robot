*** Test Cases ***
FOR Loop ENUMERATE
    FOR    ${index}    ${value}    IN ENUMERATE    a   b   c
        Log    ${index}: ${value}

    END