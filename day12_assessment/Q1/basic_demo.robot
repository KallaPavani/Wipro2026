*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${NAME}   PavaniKalla
${ROLE}   Learner
@{SKILLS}  Python  Selenium  Java

*** Test Cases ***
Log Scalar Variables
    Log    User Name is ${NAME}
    Log    User Role is ${ROLE}
    Log To Console    Running test for ${NAME}
    
    
Log List Variables
    Log    User Skills are: ${SKILLS}
    Log To Console    First skill is ${SKILLS}[0]
    Log To Console    All skills are ${SKILLS}