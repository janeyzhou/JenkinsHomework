Feature: Login & Logout

    @login @login_fail
    Scenario: Login valid user
        Given I navigate to login page
        Then I login with "abc" and "abcabc"
        Then I login Successfully
