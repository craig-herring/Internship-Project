# Created by craig.herring at 3/21/25
Feature: Cart tests

    Scenario: 'Your cart is empty' message is shown for empty cart
        Given Open Target main page
        When Click on Cart icon
        Then Verify 'Your cart is empty' message is shown
        And Verify cart page opens


    Scenario: User can add a product to cart
        Given Open target main page
        When Search for mug
        And Click on Add to Cart button
        And Store product name
        And Confirm Add to Cart button from side navigation
        And Open cart page
        Then Verify cart has 1 item(s)
        Then Verify cart has correct product

