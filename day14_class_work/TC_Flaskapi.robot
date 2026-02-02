*** Settings ***
Library    RequestsLibrary

*** Variables ***
${baseurl}   http://127.0.0.1:5001

*** Test Cases ***
Create new user
      ${data}=      Create Dictionary     name=Pavan
      Create Session    mysession       ${baseurl}
      ${response}=   POST On Session    mysession    /users    json=${data}
      Status Should Be    201     ${response}
      ${res_json}   To Json    ${response.content}
      Log    ${res_json}   console=True

Update User
         ${data}=      Create Dictionary     name=Ganesh
         Create Session    mysession       ${baseurl}
         ${response}=   PUT On Session    mysession    /users/5    json=${data}
         Status Should Be    200     ${response}
         ${res_json}   To Json    ${response.content}
         Log    ${res_json}   console=True

Patch User
         Create Session    patchmysession    ${baseurl}
         ${data}=     Create Dictionary    name="Jannat Rehman(Patched)"
         ${response}=  PATCH On Session   mysession     /users/6    json=${data}
         Status Should Be    200     ${response}
         ${res_json}   To Json    ${response.content}
         Log    ${res_json}   console=True

Verify Get_ALL_Users
         Create Session    postmysession       ${baseurl}
         ${response}=   GET On session    mysession   /users
         Status Should Be    200     ${response}
         ${res_json}   To Json    ${response.content}
         Log    ${res_json}   console=True

Verify Get_Single_User
         Create Session    mysession       ${baseurl}
         ${response}=   GET On session    mysession   /users/2
         Status Should Be    200     ${response}
         ${res_json}   To Json    ${response.content}
         Log    ${res_json}   console=True

Verify Get_Single_User not found
         Create Session    mysession       ${baseurl}
         ${response}=   GET On session    mysession   /users/50
         Status Should Be    200     ${response}
         ${res_json}   To Json    ${response.content}
         Log    ${res_json}   console=True

Delete User by user_id
         Create Session    deletesession    ${baseurl}
         ${response}=   GET On Session    mysession   /users/7
         Status Should Be    200     ${response}
         ${res_json}   To Json    ${response.content}
         Log    ${res_json}   console=True

Verify Get_ALL_Users
         Create Session    postmysession       ${baseurl}
         ${response}=   GET On session    mysession   /users
         Status Should Be    200     ${response}
         ${res_json}   To Json    ${response.content}
         Log    ${res_json}   console=True

