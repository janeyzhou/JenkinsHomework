*** Settings ***
Documentation       Search Result Page
Library             Selenium2Library


*** Keywords ***
Wait Search Result List
    Wait Until Page Contains Element    css:div[data-component-type='s-search-result']


Get Title From Search Result Items
    @{result}=  Get WebElements     css:div[data-component-type='s-search-result'] span[class='a-size-medium a-color-base a-text-normal']
    @{titleList}=   Create List
    FOR      ${element}      IN      @{result}
        ${title}=   Get Text    ${element}
        Append To List      ${titleList}    ${title}
    END
    [Return]  @{titleList}

Get Price From Search Result Items
    @{result}=  Get WebElements     css:div[data-component-type='s-search-result'] span[data-a-color='base'] span[class='a-offscreen']
    @{priceList}=   Create List
    FOR     ${element}      IN      @{result}
        ${price}=   Get Element Attribute    ${element}     innerHTML
        Append To List      ${priceList}    ${price}
    END
    [Return]  @{priceList}