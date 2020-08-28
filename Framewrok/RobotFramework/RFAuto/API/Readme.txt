Tips
1. we could create session in suite setup
2. for the dependent data, we could set as global variable by call the keyword
        ${NEWEMPLOYEE}=     Create Employee     user1
        Set Global Variable     ${NEWEMPLOYEE}
3. json file, can read data by keyword directly
    e.g. Get One User's Test Data
            [Arguments]   ${user}
            ${test_user}=   Get File    ${user_data_path}
            ${test_user_json}=   To Json    ${test_user}
            [Return]   ${test_user_json}[${user}]
4. read data from file, we can change to json by To Json, and then send the body as json
    e.g.    Create Employee
                [Arguments]  ${user}
                ${template_users}=   Get File    ${path}
                ${j}=       To Json  ${users}
                ${j}=   To Json     {"name":"test","salary":"123","age":"23"}
                ${body}=    Get Boby For Create Employee    ${user}
                ${response}=    Post Request    mySession   /api/v1/create      json=${body}
5. header and headers can be put in config folder
6. we can also set customer library, e.g  mylibrary.py
        ${result}=  myLibrary.is_new_user_displayed    ${employee_list}    ${new_user_id}
7. for each test case, please remember to add assert


Library
robotframework-requets