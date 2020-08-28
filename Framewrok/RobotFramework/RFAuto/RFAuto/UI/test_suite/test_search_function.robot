*** Settings ***
Documentation       a test case to search device
Resource            ../business_resource/search_resource.robot
Library             SeleniumLibrary
Test Teardown       Close All Browsers
Force Tags          StoryNumber-001
Default Tags        Owner-Janey smoke
Variables           ../test_data/test_data.yaml
Library             Screenshot  ../report
Suite Setup
Suite Teardown
Test Setup
Test Teardown


#setup
#timeout


*** Test Cases ***
#behavior driven style
User is able to search and view title and price of the object
    [Tags]      Not-Ready
    Given Open Browser to Go to Home Page
    When Search "kindle" From "Electronics"
    Then View Title and Price From Search Result Items

#data driven style
User search different products from different deparments
    [Tags]      data
    [Template]  Search Different Products From Different Departments
    Baby    food
    Books   Breath
    Computers   monitor
    Girls' Fashion      red dress


#read data from files
User search products from departments
    [Tags]  YML
    Open Browser to Go to Home Page
    Search Products From Departments     &{searchDict}