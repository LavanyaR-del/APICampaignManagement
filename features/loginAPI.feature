Feature: Verify login success
  Scenario: Verify Login API functionality
    Given the provided credential
    When we execute the Login PostAPI method
    Then Login should be successfull