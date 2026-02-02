*** Test Cases ***
Try Except FINALLY Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log    Error handled
    FINALLY
        Log    Always executed
    END
