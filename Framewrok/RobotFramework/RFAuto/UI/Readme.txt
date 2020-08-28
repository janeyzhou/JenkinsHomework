Run test case
Robot -i/e tagename test_case_path
Robot -V yaml_file_path UI/test_suite/test_search_function.robot

Tips
1. page resource .robot --- only contain the page element
2. business resource .robot --- contain assert and workflow
3. read file from yaml, please import to settings firstly --- Variables   yaml_file_path
4. please remember to set your driver to path, or just put to python root
5. add external tool for robot runner, the runner is python/scripts/robot.bat
6. -d is used to change the report directory
7. please user scalar type to operate list and dictionary
    e.g. Get Price From Search Result Items
            @{result}=  Get WebElements     css:div[data-component-type='s-search-result'] span[data-a-color='base'] span[class='a-offscreen']
            @{priceList}=   Create List
            FOR     ${element}      IN      @{result}
                ${price}=   Get Element Attribute    ${element}     innerHTML
                Append To List      ${priceList}    ${price}
            END
            [Return]  @{priceList}


Library and Plugin
Intellibo
Selenium2Library
pyyaml

Reference Document
https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
https://robotframework.org/robotframework/latest/libraries/Collections.html
https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
https://www.cnblogs.com/newtom/p/11750799.html