Feature: Varify Book name added in the Library
Scenario: Varify Book name
Given Book details
Then Varify book name

# @User information
Scenario Outline: Check login functionality
Given user enters "<name>" and "<password>"
Then user should be logged in
Examples: Credentials
| name   | password |
| user1  | pwd1     |
| user2  | pwd2     |