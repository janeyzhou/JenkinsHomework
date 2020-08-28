Feature: Selenium

  @example
  Scenario: Login with user without password
    Given I have a valid account
    Given I am not logged in
    When I navigate to the home page
    Then I should see the login form
    When I fill in username
    When I press login button
    Then I should see the alert contains correct text
    """
    Please fill in your password
    """

    # Homework below:
    # Login without input username
    # Login with user and password
    # Navigate to Work item page and update the row: 1, 3, 5, 7 to completed