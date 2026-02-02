*** Test Cases ***
Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log    Test Passed
