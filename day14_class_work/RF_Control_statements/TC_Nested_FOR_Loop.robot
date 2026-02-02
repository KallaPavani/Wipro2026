*** Test Cases ***
Nested FOR loop
   FOR    ${i}    IN RANGE    1    4
     FOR    ${j}    IN RANGE    1    3
         Log    i=${i},j=${j}

     END

   END