# Created by craig.herring at 3/21/25
Feature: Main page UI test

  Scenario: Verify header links has at least 1 link
    Given Open Target main page
    Then Verify at least 1 link shown

  Scenario: Verify all header links shown
    Given Open Target main page
    Then Verify 6 links shown

  Scenario: Verify that logged out user can access Sign In
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened
