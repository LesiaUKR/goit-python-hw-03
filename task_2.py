import random


def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000):
        print("Error: min or max is out of range")
        return []
    try:
        lottery_numbers = random.sample(range(min, max), quantity)
        lottery_numbers.sort()
        return lottery_numbers
    except ValueError:
        print("The quantity of numbers should be less than the range")
        return


lottery_numbers = get_numbers_ticket(1, 49, 10)
print("Your lottery digits:", lottery_numbers)
