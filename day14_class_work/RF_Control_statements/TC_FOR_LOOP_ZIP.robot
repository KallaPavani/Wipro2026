*** Variables ***
@{USERS}    admin    user
@{PWDS}     admin123    user123

*** Test Cases ***
FOR Loop ZIP
    FOR    ${u}    ${p}    IN ZIP    ${USERS}    ${PWDS}
        Log    ${s} / ${p}

    END