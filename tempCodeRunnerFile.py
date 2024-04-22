from datetime import datetime


def get_days_from_today(date):
    try:
      # convert date string in the format 'YYYY-MM-DD' into a datetime object
        date_object = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
      # handle the case when the given date has the wrong format
        print("Incorrect date format, should be YYYY-MM-DD")
        return
   #  get the current date and time
    current_datetime = datetime.today()
   # calculate the difference between the current date and the given date
    delta = current_datetime - date_object
   # return the difference in days
    return delta.days


print(get_days_from_today("2025-10-09"))