from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Kate Smith", "birthday": "2002.05.01"},
    {"name": "Max Smith", "birthday": "2002.04.29"},
    {"name": "Bob Smith", "birthday": "2002.04.28"}
]


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    upcoming_birthdays = []
    # get today's date
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        # check whether birthday already passed this year
        if birthday_this_year < today:
            # if yes, then birthday will be next year
            birthday = birthday.replace(year=today.year + 1)
        if (birthday - today).days <= 7:
            if birthday.weekday() in [5, 6]:
                # if birthday is on weekend, then congrats on Monday
                birthday_this_year += timedelta(
                    days=(7 - birthday_this_year.weekday()))
            # add user to upcoming_birthdays list
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
