# Created by craig.herring at 3/8/25
Feature: Target search test cases

  Scenario: User can search for a tea on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea
    And Verify tea in URL

  Scenario: User can search for a coffee on Target
    Given Open Target main page
    When Search for coffee
    Then Verify correct search results shown for coffee

  Scenario: User can search for a dress on Target
    Given Open Target main page
    When Search for dress
    Then Verify correct search results shown for dress

  Scenario Outline: User can search for a product on Target
    Given Open Target main page
    When Search for <search_word>
    Then Verify correct search results shown for <search_word>
    Examples:
    |search_word    |
    |tea            |
    |iPhone         |
    |dress          |
    |jacket         |

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown

