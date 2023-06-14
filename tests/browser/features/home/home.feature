Feature: Home Page module

  Background:
    Given Aspire application is launched
    And login into aspire portal page as a employee


  Scenario: Validated users have access to the home page's list of links.
    Then validate the list of links that appears on the home page sidebar.
    And verify that the user is navigating the particular page.
