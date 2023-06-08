Feature: Aspire login page

  Background:
    Given user launch browser and user enter Aspire url
    And I navigated to the Aspire login_page is displayed


  Scenario Outline: validate the login credentials on the login page
    When I fill the username <email_id> and password <password> on login_page
    And I click login button on the login button
    Then I validate user logs with valid credentials

    Examples:
      | email_id             | password   |
      | testuser1@atmecs.com | Atmecs@123 |