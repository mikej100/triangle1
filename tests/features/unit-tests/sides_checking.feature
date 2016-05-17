Feature: Input string validation
As a triangle app developer
I want to parse user input string to extract three numbers or an error
So that I can validate user input and then test for a triangle

Scenario Outline: Less than three numbers
Given I am testing the input string parser
When I pass in the string <input-string> 
Then I should get <success-or-error>

Examples:
| input-string                     | success-or-error   |
| "1,2, "                          | error              |
| "1,2"                            | error              |
| "1  "                            | error              |
| " , "                            | error              |
| "1,2,3"                          | success            |