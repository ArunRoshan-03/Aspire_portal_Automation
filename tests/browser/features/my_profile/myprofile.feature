Feature: My profile page

  Background:
    Given Aspire application is launched
    And login into aspire portal page as a employee

  Scenario: Validated users can view their profile on the My Profile page.
    When  click on the open my profile link on the homepage
    And navigating to my profile page
    Then validate user can view the their profile on the my profile page.