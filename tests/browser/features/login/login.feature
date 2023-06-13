Feature: Aspire login page

  Background:
    Given Aspire application is launched
    And login into aspire portal page as a employee

  Scenario: Validate the users logs with employee valid credentials
    Then validate user logs with employee credentials and access Aspire portal homepage.

