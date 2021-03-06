Feature: Type of triangle
As a triangle app developer
I want to gparse user input string to extract three numbers or an error
So that I can validate user input and then test for a triangle

Scenario Outline: Very small differences.
Given I am testing the input string parser
When I pass in the string <input-string> 
Then I should get <success-or-error>

Examples:
| input-string                     | triangle type      |
| "1, 1.0000000000000001, 1"       | isosceles          |
| "1,2"                            | error              |
| "1  "                            | error              |
| " , "                            | error              |
| "1,2,3"                          | success            |