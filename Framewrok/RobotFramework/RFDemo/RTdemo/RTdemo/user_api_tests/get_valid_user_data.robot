*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource           ../business_resource/resource.robot
Library           RequestsLibrary
Library            ../libs/ReadTestData.py
Force Tags        valid_user_api_data


*** Variables ***
${host}         http://localhost:5000
#${data}         uid=uid1

*** Keyword ***
Verify Valid User
    [Arguments]     ${data}     ${expect_result}
    create session    httpbin    ${host}
    ${response}       get request   httpbin   /api/user     params=${data}
    should be equal as integers    ${response.status_code}     200
    ${resp}           to json   ${response.content}
    Log     ${resp}
    should be equal    ${resp["data"]["name"]}      ${expect_result}

*** Test Cases ***
Get Valid Both User
    [Template]  Verify Valid User
        uid=uid1     Johnson
        uid=uid2     Tony
        uid=uid3     Test