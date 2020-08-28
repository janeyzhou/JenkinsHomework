*** Settings ***
Documentation       A resouce  file to search on different deparment
Library             SeleniumLibrary
Library             Collections
Resource            ../page_resource/home_page.robot
Resource            ../page_resource/search_result_page.robot

*** Keywords ***
Open Browser to Go to Home Page
    Go to Home Page
    Home Page Should Be Open


Home Page Should Be Open
    Title Should Be     Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more

Search "${searchText}" From "${departmentName}"
    Select A Department     ${departmentName}
    Input Search Text       ${searchText}
    Click Search Button
    Search Result Page Should be Open   ${searchText}

#Search Something From A Department
#    [Arguments]  ${departmentName}  ${searchText}
#    Select A Department     ${departmentName}
#    Input Search Text       ${searchText}
#    Click Search Button
#    Search Result Page Should be Open   ${searchText}

Search Result Page Should be Open
    [Arguments]     ${searchText}
    Title Should Be     Amazon.com : ${searchText}

Search Different Products From Different Departments
    [Arguments]     ${departmentName}   ${searchText}
    Open Browser to Go to Home Page
    Search "${searchText}" From "${departmentName}"

Search Products From Departments
    [Arguments]  &{searchDict}
    FOR     ${key}  ${value}    IN     &{searchDict}
        Open Browser to Go to Home Page
        Search "${value}" From "${key}"
    END

View Title and Price From Search Result Items
    Wait Search Result List
    @{titles}=   Get Title From Search Result Items
    @{prices}=   Get Price From Search Result Items
    ${length}=  Get Length  ${titles}
    FOR     ${index}    IN RANGE    ${length}
        log     ${titles}[${index}]
        log     ${prices}[${index}]
    END





