*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource           ../business_resource/resource.robot
Library           ../libs/Rest.py
Library           RequestsLibrary
Force Tags        valid_user_api2


*** Variables ***
${get_user_url}        http://localhost:5000/api/user?uid=uid2



*** Test Cases ***
Get Valid Second User
    ${response}       Rest.get request     ${get_user_url}
    should be equal as integers    ${response.status_code}     200
    ${resp}           to json   ${response.content}
    Log     ${resp}
    should be equal    ${resp["data"]["name"]}      Johnson