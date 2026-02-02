*** Test Cases ***
Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log    Test Failed
