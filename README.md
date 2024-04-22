# MODULE 4. HOMEWORK. Work with date, time and advanced work with strings goit-algo-hw-03

## Task 1

Create a function get_days_from_today(date) that calculates the number of days between the given date and the current date.

### Requirements for the task:

1. The function takes one parameter: date — a string representing the date in the 'YYYY-MM-DD' format (for example, '2020-10-09').
2. The function returns an integer indicating the number of days from the given date to the current one. If the specified date is later than the current one, the result should be negative.
3. Only days should be considered in the calculations, ignoring time (hours, minutes, seconds).
4. The datetime module in Python should be used for working with dates.

### Recommendations for implementation:

1. Import the datetime module.
2. Convert the date string in the 'YYYY-MM-DD' format to a datetime object.
3. Get the current date using datetime.today().
4. Calculate the difference between the current date and the specified date.
5. Return the difference in days as an integer.

### Evaluation criteria:

1. Correctness of the function: the function should accurately calculate the number of days between dates.
2. Exception handling: the function should handle incorrect input data formats.
3. Code readability: the code should be clean and well-documented.

### Example:

If today is May 5, 2021, calling get_days_from_today("2021-10-09") should return 157, as October 9, 2021, is 157 days later than May 5, 2021.

## Task 2

To win the jackpot in a lottery, it is necessary to match several numbers on a lottery ticket with randomly drawn numbers within a certain range during the next draw. For example, you need to guess six numbers from 1 to 49 or five numbers from 1 to 36, etc.

You need to write a function get_numbers_ticket(min, max, quantity) that will help generate a set of unique random numbers for such lotteries. It will return a random set of numbers within the specified parameters, with all random numbers in the set being unique.

### Requirements for the task:

1. Function parameters:

- min - the minimum possible number in the set (no less than 1).
- max - the maximum possible number in the set (no more than 1000).
- quantity - the number of numbers to select (a value between min and max).

2. The function generates the specified number of unique numbers within the given range.
3. The function returns a list of randomly selected, sorted numbers. Numbers in the set should not repeat. If the parameters do not meet the specified constraints, the function returns an empty list.

### Recommendations for implementation:

1. Ensure that the input parameters meet the specified constraints.
2. Use the random module to generate random numbers.
3. Use a set or another mechanism to ensure the uniqueness of numbers.
4. Remember that the get_numbers_ticket function returns a sorted list of unique numbers.

### Evaluation criteria:

1. Validity of input data: the function should validate the parameters.
2. Uniqueness of the result: all numbers in the output should be unique.
3. Compliance with requirements: the result should be in the form of a sorted list.
4. Code readability: the code should be clean and well-documented.

### Example:

Suppose you need to select 6 unique numbers for a lottery ticket, where numbers should be in the range from 1 to 49. You can use your function like this:

```
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
```

This code calls the get_numbers_ticket function with the parameters min=1, max=49, and quantity=6. As a result, you will get a list of 6 random, unique, and sorted numbers, for example, [4, 15, 23, 28, 37, 45]. Each time you call the function, you will get a different set of numbers.
