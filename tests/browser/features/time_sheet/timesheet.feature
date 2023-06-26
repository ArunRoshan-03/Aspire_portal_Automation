Feature: Time sheet module

  On the time sheet page, the user enters working timings details such as working hours, leave, week off,
  and day-to-day activity.

  Background:
    Given Aspire application is launched
    And login into aspire portal page as a employee


  Scenario: Validate the time sheet link is displayed on home page
    Then validate user navigating to aspire portal home page
    And verify the time sheet link is displayed on homepage.


  Scenario: Validate that the timesheet page title is visible.
    When I click on the time sheet link on the homepage
    And timesheet page is loaded
    Then verify the time sheet page title that appears on the time sheet page.


  Scenario: Validate user can see the current week's dates on the time sheet
    When I click on the time sheet link on the homepage
    And timesheet page is loaded
    Then validate the current week's dates that appear on the time sheet page.


  Scenario: Validate users can add activities and save the time sheet for the current week.
    When I click on the time sheet link on the homepage
    And timesheet page is loaded
    And  I enter the working hours for the week and save the timesheet
    Then validate activities saved on the time sheet.

  @ar
  Scenario: Validating the Timesheet Submitted by an Employee as a Manager.
    When I click on the time sheet link on the homepage
    And timesheet page is loaded
    And I enter the working hours for the week and save the timesheet
    And I log out and return to the login page
    And I login into aspire portal page as a manager.
    And I click on the time sheet link on the homepage
    And timesheet page is loaded
    And I click the reports button on the time sheet page.
    And the reports page is loaded.
    And I select the client, start date and end start data on the project wise table.
    And I click the export button
    Then the exported data as appear on the project wise table.
    And I validate the weekday timing of the employee.
    And If the employee has less than working hours,an email should be sent to the employee.