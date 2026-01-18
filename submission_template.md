# AI Code Review Assignment (Python)

## Candidate
- Name:
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- incorrect logic, dividing by the total number of variables when we are supposed to divide by the number of not cancelled orders
- dividing by zero
- TypeError from invalid operations
- not making sure that the the 'amount' is numeric
- KeyError from missing dictionary keys

### Edge cases & risks
- Handling invalid inputs like non-iterables
- invalied value for 'amount' attribute
- missing an essintial attribute like 'amount' or 'status'
- not having any orders at all
- all the orders were cancelled

### Code quality / design issues
- names of the variables weren't clear
- No error handling or logging
- lack of comments which made the code a bit confusing at first

## 2) Proposed Fixes / Improvements
### Summary of changes
- started counting the cancelled orders and divide by this number to find the average
- checked if 'orders' empty (no orders), if so then just return 0
- check first if the main two attributes 'amount' and 'status' do exist 
- convert the amount to a string to ensure it's validity
- created another function (is_numeric_string) for making sure that the 'amount' has a valied value to proceed with the calculations
- after looping over the orders, if the number of cancelled orders is zero then return 0 (all the orders were cacelled) to avoid dividing by zero
- to calculate the average divid by the number of cancelled orders not the total number of orders
- added dome testcases to test my code while working on it

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- will review the code quickly to understand what is going on in there, making sure that the code is clean , contains some comments, the variables have names that referes to the values or porpose, having a reasonable amount of spacing between the lines of code dividing the different parts of the code, if i can't understand the code i won't be able to check whether it is working or not
- will work at first as a programmer who wants to cod the whole thing from scratch and then generate a couple of test cases trying to makre the code fail as much as i can to handle all the types of users my code could face

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- dividing by the number of orders not the cancelled orders
- as a result to the previous point, we didn't actually correctly exclude cancelled orders from the calculations

### Rewritten explanation
- this functions calculates the average values of non-cancelled orders, by adding the amount of non-cancelled orders and dividing by the number of non-cancelled orders with the help of helper function (is_numeric_string) for further checking for some edge cases, it correctly excludes and ignore the cancelled orders and orders with invalied amount value

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
