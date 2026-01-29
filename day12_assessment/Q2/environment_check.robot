*** Settings ***
Library   BuiltIn
Library   SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
   Log To Console    ==== Environment Verification Started ====

   #Verifying Python Installation
   ${python_version}=   Evaluate    sys.version    sys
   Log    Python Version: ${python_version}
   Log To Console    Python is installed

   #Verifying Robot FRamework Installation
   ${robot_version}=   Evaluate    robot.__version__   robot
   Log    Robot Framework Version: ${robot_version}
   Log To Console    Robot Framework version: ${robot_version}

   #Verifying SeleniumLibrary Import
   Log    SeleniumLibrary imported successfully
   Log To Console    SeleniumLibrary is available

   Log To Console    ==== Environment Verification completed successfully ====