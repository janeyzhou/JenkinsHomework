*** Settings ***
Documentation   test employee API
Resource        ../employee_api/employee_resource.robot
Resource        ../business_resource/operate_employee.robot
#Variables       ../employee_api/endPoint.py
#Suite Setup     Create Session      mySession   http://dummy.restapiexample.com    headers=${HEADERS}

*** Test Cases ***
Get employee list
    [Tags]  GET
    Get Employees

Create a specified employee
    [Tags]  Create
    Create Employee     user1

Delete an employee
    [Tags]  Delete
    Delete Employee     54

Verify valid employee is created succesffully
    [Tags]  Verify
    [Template]      Create Valid Employee
    user1
    user2
    user3

Verify new employee is displayed on employee list
    [Tags]  Display
    New Employee In Employee List  user1

Verify new employee can be deleted successfully
    [Tags]  Delete
    Delete The Created Employee     user1