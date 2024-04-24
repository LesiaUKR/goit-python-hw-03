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

## Task 3

Your company is running an active marketing campaign using SMS broadcasts. To do this, you collect customer phone numbers from the database, but often encounter numbers in different formats. For example:

```
" +38(050)123-32-34"
" 0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11 "
```

Your broadcasting service can effectively send messages only when phone numbers are in the correct format. Therefore, you need a function that automatically normalizes phone numbers to the required format by removing all unnecessary characters and adding the country's international code if necessary.

Develop the normalize_phone(phone_number) function, which normalizes phone numbers to a standard format, leaving only digits and the '+' symbol at the beginning. The function takes one argument - a string with the phone number in any format and transforms it into a standardized format, leaving only digits and the '+' symbol. If the number does not contain an international code, the function automatically adds the '+38' code (for Ukraine). This ensures that all numbers are suitable for SMS sending.

### Requirements for the task:

1. The phone_number parameter of the function is a string with the phone number in various formats.
2. The function removes all characters except digits and the '+' symbol.
   If the international code is missing, the function adds the '+38' code.
3. This covers cases where the number starts with '380' (only '+' is added) and when the number starts without a code ('+38' is added).
4. The function returns the normalized phone number as a string.

### Recommendations for implementation:

1. Use the re module for regular expressions to remove unnecessary characters.
2. Check if the number starts with '+', and adjust the prefix accordingly.
3. Remove all characters except digits and '+', from the phone number.
4. Don't forget to return the normalized phone number from the function.

### Evaluation Criteria:

1. Correctness of the function: the function should correctly process different number formats, taking into account the presence or absence of the international code.
2. Code readability: the code should be clean, well-organized, and well-documented.
3. Proper use of regular expressions to remove unnecessary characters and format the number.

### Example of usage:

```
raw_numbers = [
"067\\t123 4567",
"(095) 234-5678\\n",
"+380 44 123 4567",
"380501234567",
" +38(050)123-32-34",
" 0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11 ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS broadcasting:", sanitized_numbers)
```

As a result, you should get a list of numbers in standard format, ready for use in SMS broadcasts.

```
Normalized phone numbers for SMS broadcasting: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```

## Task 4

Within your organization, you are responsible for organizing birthday greetings for colleagues. To optimize this process, you need to create a function get_upcoming_birthdays that will help you determine who among your colleagues needs to be greeted. The function should return a list of all colleagues whose birthdays are within the next 7 days, including the current day.

You have a list called users, each element of which contains information about the user's name and their birthday. Since colleagues' birthdays may fall on weekends, your function should also consider this and move the greeting date to the next working day if necessary.

### Requirements for the task:

1. The users parameter of the function is a list of dictionaries, where each dictionary contains the keys name (user's name, string) and birthday (birthday date, string in the format 'year.month.day').
2. The function should determine whose birthdays fall within the next 7 days, including the current day. If a birthday falls on a weekend, the greeting date should be moved to the next Monday.
3. The function returns a list of dictionaries, where each dictionary contains information about the user (key name) and the congratulation date (key congratulation_date, data in the format 'year.month.day').

### Recommendations for implementation:

1. Assume that you have received a list called users, where each dictionary contains name (user's name) and birthday (birthday date in the format 'year.month.day'). You should convert birthday dates from strings to datetime objects. Convert the birthday date from string to datetime object - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Since only the date (without time) is needed, use .date() to get only the date.
2. Determine the current system date using datetime.today().date().
3. Iterate through the users list and analyze the birthdays of each user (for user in users:).
4. Check if the birthday has already passed this year (if birthday_this_year < today). If so, consider the date for the next year.
5. Calculate the difference between the birthday and the current day to determine the birthdays for the next week.
6. Check if the birthday falls on a weekend. If so, move the greeting date to the next Monday.
7. Create a data structure that stores the user's name and the corresponding greeting date if the birthday occurs within the next week.
8. Output the collected data as a list of dictionaries with user names and greeting dates.

### Evaluation Criteria:

1. Accuracy and correctness in determining birthdays for the next 7 days.
2. Proper handling of cases where birthdays fall on weekends.
3. Code readability and structure.

### Example:

Suppose you have a list of users:
```
users = [
{"name": "John Doe", "birthday": "1985.01.23"},
{"name": "Jane Smith", "birthday": "1990.01.27"}
]
```
Using the get_upcoming_birthdays function:
```
upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings for this week:", upcoming_birthdays)
```
If today is 2024.01.22, the result could be:
```
[
{'name': 'John Doe', 'congratulation_date': '2024.01.23'},
{'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]
```
This list contains information about who and when needs to be greeted on their birthday.
