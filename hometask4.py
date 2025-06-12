from datetime import datetime, timedelta


def get_upcoming_birthdays(users:list[dict[str,str]]) -> list[dict[str,str]]:
    """
    Function return a list of users whose birthdays occur within the next 7 days,
    adjusting for leap-year dates and weekend celebrations.

    Args:
        users (list[dict[str, str]]): A list of user dictionaries, each with "name" and "birthday" (YYYY.MM.DD).
    Returns:
        list[dict[str, str]]: A list of dictionaries, each with "name" and "congratulation_date" (YYYY.MM.DD)
                              for birthdays falling within the next 7 days.
                              Weekend birthdays are shifted to the following Monday.
                              Feb 29 birthdays in non-leap years are shifted to March 1.
    """
    today = datetime.today().date()
    result: list[dict[str, str]] = []  

    for user in users:
        try:
            user_birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        except (KeyError, ValueError, TypeError):
            # If the birthday format is incorrect or missing, skip this user
            continue

        try:
            birthday_this_year = user_birthday.replace(year=today.year)
        except ValueError:
            # If it was February 29 and the year is not a leap year, we celebrate March 1
            birthday_this_year = datetime(today.year, 3, 1).date()

        if birthday_this_year < today:
            try:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            except ValueError:   
                # If it will February 29 and the year is not a leap year, we celebrate March 1
                birthday_this_year = datetime(today.year+1, 3, 1).date()

        days_count= (birthday_this_year - today).days

        if 0 <= days_count <= 7:
            iso_weekday = birthday_this_year.isoweekday()
            if iso_weekday >= 6: # Saturday or Sunday
                    congratulation_date=birthday_this_year+ timedelta(days= 8 - iso_weekday)
            else:
                    congratulation_date=birthday_this_year

            result.append({"name": user["name"],"congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return result

                
                     



