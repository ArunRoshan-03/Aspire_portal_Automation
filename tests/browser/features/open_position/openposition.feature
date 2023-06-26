Feature: Open position module
  Open position page displays job openings, contact information, experience, and status.

  Background:
    Given Aspire application is launched
    And login into aspire portal page as a employee

  Scenario: Validate the open position link is displayed on home page
    Then validate user navigating to aspire portal home page
    And verify the open position link is displayed on homepage.

  Scenario: Validate that the open position page title is visible.
    When click on the open position link on the homepage
    Then validate user navigating to open position page
    And verify the open position page title that appears on the open sheet page.

  Scenario: Validate the job title list is visible on the open position page.
    When click on the open position link on the homepage
    And navigating to open position page
    Then validate the job title list that appears on the open position page.