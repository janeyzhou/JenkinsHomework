Feature: Login
  user is able to login with valid username and password, otherwise user is not able to access the home page

#  Scenario: Login without input username
#    Given a set of valid user account
#      | username         | password    |
#      |                  | @A12345b    |
#    Given I am not logged in
#    When I login without username
#    Then I should see the alert message
#    """
#    Plase fill in your email address
#    """

  @valid
  Scenario Outline: login with valid user account
    Given I am not logged in
    When  I login with valid account "<username>" "<password>"
    Then I should login successfully

    Examples: valid user account
      | username             | password    |
      | janey_zhou@epam.com  | @A12345b    |

