*** Test Cases ***
IF ELSE IF EXAMPLE
   ${marks}=  Set Variable  75
   IF    ${marks} >= 90
       Log    GRADE A
   ELSE IF    ${marks} >= 75
       Log    GRADE B
   ELSE
        Log    GRADE C
   END