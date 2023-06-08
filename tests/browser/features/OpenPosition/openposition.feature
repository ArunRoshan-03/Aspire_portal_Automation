Feature: Open position module

  Background:
    Given user launch browser and user enter Aspire url
    And I navigated to the Aspire login_page is displayed


  Scenario Outline: validate the open position button on home page
    When I fill the username <email_id> and password <password> on login_page
    And I click login button on the login button
    Then I validate the open position page

    Examples:
      | email_id             | password   |
      | testuser1@atmecs.com | Atmecs@123 |

  @ar
  Scenario Outline: validate the list of job openings.
    When I fill the username <email_id> and password <password> on login_page
    And I click login button on the login button
    Then I validate the list of job openings in the job openings table

    Examples:
      | email_id             | password   |
      | testuser1@atmecs.com | Atmecs@123 |