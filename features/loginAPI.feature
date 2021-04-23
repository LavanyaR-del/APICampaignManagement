Feature: Verify login success
  Scenario: Verify Login API functionality
    Given the provided credential
    When we execute the Login PostAPI method
    Then Login should be successfull
    And status code should be 200
    And error code should be False
    Then extract token and save it