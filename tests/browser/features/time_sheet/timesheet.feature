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
    When click on the time sheet link on the homepage
    Then validate user navigating to timesheet page
    And verify the time sheet page title that appears on the time sheet page.

  Scenario: Validate user can see the current week's dates on the time sheet
    When click on the time sheet link on the homepage
    And navigating to timesheet page
    Then validate the current week's dates that appear on the time sheet page.


  Scenario: Validate users can add activities and save the time sheet for the current week.
    When click on the time sheet link on the homepage
    And navigating to timesheet page
    And enter the times for the entire week and then save the time sheet.
    Then validate activities saved on the time sheet.

  Scenario: Validate users can add activities and submit the weekly time sheet.
    When click on the time sheet link on the homepage
    And navigating to timesheet page
    And enter the times for the entire week and then submit the time sheet.
    Then validate activities submitted on time sheet.

  @ar
  Scenario: Validate the timesheet submitted by an employee when logged in as a manager.
    When I click on the time sheet link on the homepage
    And timesheet page is loaded
    And I am enter the working hours for the week and submit the time sheet.
    And logout and loads the login page.
    And login into aspire portal page as a manager.
    And I click on the time sheet link on the homepage
    And timesheet page is loaded
    And I click the reports button on the time sheet page.
    And reports page is loaded.
    And select the client, start date and end start data on the project wise table.
    And click the export button
    And the export data as appear on the project wise table.
    And the weekday timing of the employee.
    Then validate if employee as more than 45 working hours
    And send email to employee
