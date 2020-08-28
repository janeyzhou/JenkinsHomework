*** Settings ***
Documentation       Home Page
Library             SeleniumLibrary


*** Variables ***
${DEVICE URL}       https://www.amazon.com
${BROWSER}          Chrome



*** Keywords ***
Go to Home Page
    Open Browser    ${DEVICE URL}       ${BROWSER}

Select A Department
    [Arguments]     ${departmentName}
    Select From List By Label   css:select[class='nav-search-dropdown searchSelect']    ${departmentName}

Input Search Text
    [Arguments]     ${searchText}
    Input Text      css:.nav-search-field>input     ${searchText}

Click Search Button
    Click Button    css:input[type='submit'][class='nav-input']

