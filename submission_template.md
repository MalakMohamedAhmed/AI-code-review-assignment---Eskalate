# AI Code Review Assignment (Python)

## Candidate
- Name: Malak Mohamed Ahmed Mohamed Abdelkareem
- Approximate time spent: 2-3 hours

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Error for invalid input
- incorrect logic, dividing by the total number of variables when we are supposed to divide by the number of not cancelled orders
- dividing by zero
- TypeError from invalid operations
- not making sure that the 'amount' is numeric
- KeyError from missing dictionary keys

### Edge cases & risks
- Handling invalid inputs like non-iterables
- invalid value for 'amount' attribute
- missing an essential attribute like 'amount' or 'status.'
- not having any orders at all
- All the orders were cancelled

### Code quality/design issues
- The names of the variables weren't clear
- No error handling or logging
- lack of comments, which made the code a bit confusing at first

## 2) Proposed Fixes / Improvements
### Summary of changes
- checked in the beginning that the given 'orders' parameter is a list or a dictionary
- started counting the not-cancelled orders and divided by this number to find the average
- checked if 'orders' is empty (no orders), if so, then return 0
- checked each order in the list whether it is a dictionary or not
- check first if the two attributes 'amount' and 'status' exist 
- convert the amount to a string to ensure its validity
- created another function (is_numeric_string) for making sure that the 'amount' has a valid value to proceed with the calculations
- after looping over the orders, if the number of not-cancelled orders is zero, then return 0 (all the orders were cancelled) to avoid dividing by zero
- to calculate the average divided by the number of not-cancelled orders, not the total number of orders
- added some testcases to test my code while working on it

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- will review the code quickly to understand what is going on in there, making sure that the code is clean, contains some comments, the variables have names that referes to the values or porpose, and have a reasonable amount of spacing between the lines of code separating the different parts of the code, if i can't understand the code i won't be able to check whether it is working or not
- will work at first as a programmer who wants to code the whole thing from scratch and then generate a couple of test cases, trying to make the code fail as much as I can to handle all the types of users my code could face

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Dividing by the total number of orders, not the number of not-cancelled orders.
- As a result of the previous point, we didn't actually correctly exclude cancelled orders from the calculations

### Rewritten explanation
- this functions calculates the average values of non-cancelled orders by adding the amount of non-cancelled orders and dividing by the number of non-cancelled orders, with the help of a helper function (is_numeric_string) for further checking for some edge cases. It correctly excludes and ignores the cancelled orders and orders with invalid amount values.

## 4) Final Judgment
- Decision: Approve (with minor suggestions)
- Justification: The major logical errors, edge cases, and runtime risks in the original code were correctly identified and fixed. The updated implementation properly excludes cancelled orders, prevents division by zero, validates inputs, and handles invalid or missing data safely. The rewritten explanation accurately reflects the corrected logic, and the added tests improve confidence in correctness.
- Confidence & unknowns: Confidence is high in the solution’s correctness. Remaining unknowns include performance on very large datasets, unclear business rules for partially invalid data, and the lack of logging for production use.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Error for invalid input
- inaccurate output, claiming some strings to be a valid email when they are not
- incorrect logic
- invalid values inside the 'emails' parameter

### Edge cases & risks
- strings containing multiple '@.'
- invalid value for 'email' values (not strings)
- invalid inputs (not a list or a tuple)
- empty 'emails' list or tuple given

### Code quality/design issues
- The names of the variables weren't clear
- No error handling or logging
- lack of comments, which made the code a bit confusing at first

## 2) Proposed Fixes / Improvements
### Summary of changes
- used regular expressions to check whether the emails are valid or not
- checked in the beginning that the given 'emails' parameter is a list or a tuple
- created a regular expression that represents the email constraints
- checked each email in the list whether it is a string or not
- stripped the unnecessary whitespaces for each email (each iteration)

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- will review the code quickly to understand what is going on in there, making sure that the code is clean, contains some comments, the variables have names that referes to the values or porpose, and have a reasonable amount of spacing between the lines of code separating the different parts of the code, if i can't understand the code i won't be able to check whether it is working or not
- will work at first as a programmer who wants to code the whole thing from scratch and then generate a couple of test cases, trying to make the code fail as much as I can to handle all the types of users my code could face

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- doesn't contain any details about how the checking process is going to happen or what tools and techniques 

### Rewritten explanation
- This function counts the number of valid email addresses in an input list by using a regular expression. The process is all about matching each email with a regular expression that represents the email address constraints. If the match is successful, then the email is valid; otherwise, it is not. It successfully ignores empty and invalid inputs.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The main logic and validation issues were fixed by adding proper input checks and using a regular expression to accurately validate emails. The solution now handles invalid types, empty inputs, and edge cases correctly, and the explanation clearly describes the validation approach.
- Confidence & unknowns: Confidence is high in the solution’s correctness. Open considerations include how strict the regex needs to be for business or RFC compliance, performance on very large inputs, and the lack of logging for production use.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Error for invalid input
- incorrect logic, dividing by the total number of variables when we are supposed to divide by the number of not cancelled orders
- dividing by zero
- precision issues
- TypeError from invalid operations

### Edge cases & risks
- Handling invalid inputs like non-iterables
- invalied values
- not having any values
- all the values are null

### Code quality/design issues
- The names of the variables weren't clear
- No error handling or logging
- lack of comments, which made the code a bit confusing at first

## 2) Proposed Fixes / Improvements
### Summary of changes
- checked in the beginning that the given 'values' parameter is a list or a tuple
- started counting the not null values, instead of working with the total number of values
- checked if 'values' is empty (no values), if so, then return 0
- created another function (is_numeric_string) for making sure that the 'value' has a valid value to proceed with the calculations
- after looping over the values, if the number of not null values is zero, then return 0 (all the orders were cancelled) to avoid dividing by zero
- to calculate the average divided by the number of not null values, not the total number of values
- rounded the average before returning it, in case of having precision issues from adding many float numbers
- added some testcases to test my code while working on it

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- will review the code quickly to understand what is going on in there, making sure that the code is clean, contains some comments, the variables have names that referes to the values or porpose, and have a reasonable amount of spacing between the lines of code separating the different parts of the code, if i can't understand the code i won't be able to check whether it is working or not
- will work at first as a programmer who wants to code the whole thing from scratch and then generate a couple of test cases, trying to make the code fail as much as I can to handle all the types of users my code could face


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average.

### Issues in original explanation
- not explaining the process of calculating the average
- Use some unclear words that can have double meanings
- need a bit of details

### Rewritten explanation
- This function calculates the average amount of valid measurements by adding the not null values and dividing the sum by the total number of not null values with the help of another helper function (is_numeric_string) for further checking and avoidance of more edge cases. It safely handles wrong input types and ensures an accurate average.

## 4) Final Judgment
- Decision: Approve
- Justification: The critical logic errors, division by zero risk, and input validation issues were correctly identified and fixed. The updated solution now averages only valid (non-null) values, handles invalid inputs safely, and avoids precision and runtime errors.
- Confidence & unknowns: Confidence is high in the correctness of the solution. Remaining unknowns include performance on very large datasets and whether additional logging or stricter numeric validation is required for production use.


