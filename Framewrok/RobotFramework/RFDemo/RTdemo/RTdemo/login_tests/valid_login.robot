*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource           ../business_resource/resource.robot
Library           SeleniumLibrary
Force Tags        valid_login

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Login With Account And Password     demo    mode
    Welcome Page Should Be Open
    [Teardown]    Close Broswser
