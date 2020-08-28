*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource           ../business_resource/resource.robot
Library           RequestsLibrary
Force Tags        valid_user_api


*** Variables ***
${host}         http://localhost:5000
${data}         uid=uid1

*** Test Cases ***
Get Valid User
    create session    httpbin    ${host}
    ${response}       get request   httpbin   /api/user     params=${data}
    should be equal as integers    ${response.status_code}     200
    ${resp}           to json   ${response.content}
    Log     ${resp}
    should be equal    ${resp["data"]["name"]}      Johnson