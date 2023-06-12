Feature: Aspire login page

  Background:
    Given Aspire application is launched
    And I login into aspire portal page as a employee

  @ar
  Scenario: Validate the users logs valid credentials
    Then I validate user logs with credentials and access Aspire portal homepage.

