"""The pages package contains all Page Object Model (POM) classes.

Each page of the OrangeHRM application is represented by one class that knows:
    * the locators (how to find elements on that page), and
    * the actions a user can perform on that page.

Tests then talk to these page objects instead of touching raw selectors,
which keeps the tests readable and easy to maintain.
"""
