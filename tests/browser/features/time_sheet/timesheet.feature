Feature: Time sheet module

  On the time sheet page, the user enters working timings details such as working hours, leave, week off,
  and day-to-day activity.

  Background:
    Given Aspire application is launched
    And I login into aspire portal page as a employee
    And I navigated to aspire portal home page


  Scenario: Validate the time sheet link on home page
    Then I validate the time sheet link

  Scenario: Validate the time sheet page
    When I click on the time sheet link on the homepage
    Then I validate the time sheet page


  Scenario: Validate user can see the current week's dates on the time sheet
    When I click on the time sheet link on the homepage
    Then I validate the current week's dates

  Scenario: Validate users can add activities and save the time sheet for the current week.
    When I click on the time sheet link on the homepage
    And I enter the timings from the entire week to the time sheet
    Then I validate activities and save time sheet.


