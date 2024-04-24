import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32++++34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-2",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number: str) -> str:
   #  delete all non-digit characters
    normalized_number = re.sub(r'\D', '', phone_number)
   #  check if number starts with the country code
    if normalized_number.startswith('380'):
      #   add '+' to the beginning of the number if country code exists
        normalized_number = '+' + normalized_number
    else:
      #   add country code +38 if it is missing
        normalized_number = '+38' + normalized_number

    return normalized_number


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
