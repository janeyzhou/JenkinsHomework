*** Settings ***
Documentation           create, delete, get employee
...
Resource                ../employee_api/employee_resource.robot
Library                 ../Libs/myLibrary.py

*** Keywords ***
Create Valid Employee
    [Arguments]     ${user}
    ${act}=     Create Employee     ${user}
    ${exp}=     Get One User's Test Data    ${user}
    ${result}=      myLibrary.compare_result    ${exp}  ${act}
    Should Be True      ${result}

New Employee In Employee List
    [Arguments]     ${user}
    ${new_user}=     Create Employee     ${user}
    ${new_user_id}=  Convert to String    ${new_user}[data][id]
    ${employee_list}=   Get Employees
    ${result}=  myLibrary.is_new_user_displayed    ${employee_list}    ${new_user_id}
    Should Be True      ${result}


Delete The Created Employee
    [Arguments]     ${user}
    ${new_user}=     Create Employee     ${user}
    ${new_user_id}=  Convert to String    ${new_user}[data][id]
    Delete Employee     ${new_user_id}
