*** Variables ***
@{COLORS}   Red   Green   Blue
@{NAMES}    Pavani   Kalla   Krishna

*** Test Cases ***
Print colors using for loop with list
    FOR    ${Color}    IN    @{COLORS}
        Log    Color: ${Color}
    END

Print names using for loop
    FOR    ${name}    IN    @{NAMES}
        Log    Name: ${name}
    END
