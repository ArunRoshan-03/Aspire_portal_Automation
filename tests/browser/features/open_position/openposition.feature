Feature: Open position module
  Open position page displays job openings, contact information, experience, and status.

  Background:
    Given Aspire application is launched
    And I login into aspire portal page as a employee
    And I navigated to aspire portal home page


  Scenario: Validate the open position link on home page
    Then I validate the open position link


  Scenario: Validate the job openings page
    When I click on the open position link
    And I navigated to job openings page
    Then I validate the job openings page


  Scenario: Validate the list job openings
    When I click on the open position link
    And I navigated to job openings page
    Then I validate the list of job openings