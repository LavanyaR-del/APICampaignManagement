Feature: Verify login success

  @smoke
  Scenario Outline: Verify Login API functionality
    Given the URL and the login credentials <login> and <password>
    When we execute the Login PostAPI method
    Then Login should be successfull
    And status code should be 200
    #code reusability has been implemented
    And error code should be False
    Then extract token and save it
      Examples:
         | login                          | password|
         | test@aiquire.com               | 123456  |
         | qa_user1@pyxistestaccount.com  | Pyxis@123|

  @smoke
  Scenario Outline: Step 2 - Get clients associated with the logged in user
      Given the Authorization
      When the Clients GetAPI is executed
      And error should be false
      Then store the client ID <ClientName>
      And status code should be 200
      Examples:
        | ClientName |
        | Brandtrack  |
        | Testclient  |