*** Settings ***
Documentation       A resource file to define the employee api
Library             RequestsLibrary
Library             OperatingSystem
Library             Collections
Variables           endPoint.py

*** Variables ***
${template_user_path}        test_data/user_template.json
${user_data_path}            test_data/user_data.json


*** Keywords ***
#My Session
#    Create Session      mySession   http://dummy.restapiexample.com/    headers=${HEADERS}  cookies= ${COOKIES}
#    [Return]  mySession

Get Employees
    ${response}=    Get Request     mySession   /api/v1/employees
    Status Should Be    200     ${response}
    ${res}=     To Json     ${response.content}
    [Return]        ${res}


Create Employee
    [Arguments]  ${user}
#    ${template_users}=   Get File    ${path}
#    ${j}=       To Json  ${users}
#    ${j}=   To Json     {"name":"test","salary":"123","age":"23"}
    ${body}=    Get Boby For Create Employee    ${user}
    ${response}=    Post Request    mySession   /api/v1/create      json=${body}
    Status Should Be    200     ${response}
    ${res}=     To Json     ${response.content}
    [Return]    ${res}


Delete Employee
    [Arguments]   ${userId}
    ${response}=    Delete Request  mySession   /api/v1/delete/${userId}
    Status Should Be    200     ${response}


Get Template User
    ${template_user}=   Get File    ${template_user_path}
    ${json_data}=   To Json     ${template_user}
    [Return]   ${json_data}

Get One User's Test Data
    [Arguments]   ${user}
    ${test_user}=   Get File    ${user_data_path}
    ${test_user_json}=   To Json    ${test_user}
    [Return]   ${test_user_json}[${user}]


Get Boby For Create Employee
    [Arguments]   ${user}
    ${template_user}=   Get Template User
    ${test_data}=   Get One User's Test Data    ${user}
    FOR     ${key}  ${value}     IN      &{test_data}
        Set To Dictionary   ${template_user}    ${KEY}=${VALUE}
    END
    [Return]     ${template_user}