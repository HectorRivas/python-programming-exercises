###
#This program will determine if a year is a leap year or not.
#A leap year is a year that is divisible by 4, but not divisible by 100, unless it is divisible by 400.
###

def is_leap_year(year):
    """
    Determines whether a year is a leap year.

    A year is a leap year if it is divisible by 4, but not by 100,
    unless it is also divisible by 400.

    Arguments:
    year: The year to check (integer).

    Returns:
    True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
