Feature: Register Account functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter below details into mandatory fields
        |first_name|last_name|telephone |password |
        |John|Mathew|1234567890|12345|
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created


