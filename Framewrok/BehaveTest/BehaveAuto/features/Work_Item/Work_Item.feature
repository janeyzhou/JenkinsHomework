Feature: Work_Item
  user should be able to view and update work item


  @simple
  Scenario: update work item's status
    Given I login in with valid account
    When I update work item status
    Then I update status successfully
