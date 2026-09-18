# ==========================================
#        CALENDAR & DATE UTILITY
# ==========================================

import calendar
from datetime import date, datetime, timedelta


# ==========================================
#              HELPER FUNCTIONS
# ==========================================

def get_valid_date():
    """Take a date from the user and return a date object."""

    while True:
        try:
            date_input = input(
                "Enter date (DD/MM/YYYY): "
            )

            selected_date = datetime.strptime(
                date_input, "%d/%m/%Y"
            ).date()

            return selected_date

        except ValueError:
            print(
                "\nError: Invalid date!"
                "\nPlease use DD/MM/YYYY format."
            )


def get_valid_month():
    """Take a valid month number from the user."""

    while True:
        try:
            month = int(
                input("Enter month number (1-12): ")
            )

            if 1 <= month <= 12:
                return month

            print("\nError: Month must be between 1 and 12.")

        except ValueError:
            print("\nError: Please enter a valid number.")


def get_valid_year():
    """Take a valid year from the user."""

    while True:
        try:
            year = int(
                input("Enter year: ")
            )

            if year > 0:
                return year

            print("\nError: Year must be greater than 0.")

        except ValueError:
            print("\nError: Please enter a valid year.")


# ==========================================
#          DISPLAY FULL YEAR
# ==========================================

def display_full_year(year):

    cal = calendar.TextCalendar(calendar.SUNDAY)

    print("\n")
    print("=" * 70)
    print("                    CALENDAR")
    print("=" * 70)

    print(
        cal.formatyear(
            year,
            2,
            1,
            6,
            3
        )
    )


# ==========================================
#          DISPLAY SPECIFIC MONTH
# ==========================================

def display_month(year):

    month = get_valid_month()

    print("\n")
    print("=" * 40)

    cal = calendar.TextCalendar(calendar.SUNDAY)

    cal.prmonth(year, month)

    print("=" * 40)


# ==========================================
#          CURRENT MONTH CALENDAR
# ==========================================

def current_month():

    today = date.today()

    print("\n")
    print("=" * 40)
    print("          CURRENT MONTH")
    print("=" * 40)

    cal = calendar.TextCalendar(calendar.SUNDAY)

    cal.prmonth(today.year, today.month)

    print("=" * 40)


# ==========================================
#             LEAP YEAR CHECK
# ==========================================

def check_leap_year():

    year = get_valid_year()

    if calendar.isleap(year):

        print(
            "\n%d is a LEAP YEAR." % year
        )

    else:

        print(
            "\n%d is NOT a leap year." % year
        )


# ==========================================
#          DAYS IN A MONTH
# ==========================================

def days_in_month():

    year = get_valid_year()
    month = get_valid_month()

    days = calendar.monthrange(
        year,
        month
    )[1]

    month_name = calendar.month_name[month]

    print(
        "\n%s %d has %d days."
        % (month_name, year, days)
    )


# ==========================================
#          FIND DAY OF THE WEEK
# ==========================================

def find_day():

    selected_date = get_valid_date()

    day_name = selected_date.strftime("%A")

    print(
        "\n%s is a %s."
        % (
            selected_date.strftime("%d/%m/%Y"),
            day_name
        )
    )


# ==========================================
#             TODAY'S DATE
# ==========================================

def todays_date():

    today = date.today()

    print("\n")
    print("==========================================")
    print("              TODAY'S DATE")
    print("==========================================")

    print(
        "\nDate        : %s"
        % today.strftime("%d/%m/%Y")
    )

    print(
        "Day         : %s"
        % today.strftime("%A")
    )

    print(
        "Month       : %s"
        % today.strftime("%B")
    )

    print(
        "Year        : %d"
        % today.year
    )

    print(
        "Day of Year : %d"
        % today.timetuple().tm_yday
    )


# ==========================================
#          DAYS REMAINING IN YEAR
# ==========================================

def days_remaining():

    today = date.today()

    last_day = date(
        today.year,
        12,
        31
    )

    remaining = (
        last_day - today
    ).days

    print(
        "\nThere are %d days remaining in %d."
        % (remaining, today.year)
    )


# ==========================================
#              WEEK NUMBER
# ==========================================

def week_number():

    selected_date = get_valid_date()

    week = selected_date.isocalendar().week

    print(
        "\n%s belongs to ISO week number %d."
        % (
            selected_date.strftime("%d/%m/%Y"),
            week
        )
    )


# ==========================================
#             DATE DIFFERENCE
# ==========================================

def date_difference():

    print("\nEnter the first date:")

    date1 = get_valid_date()

    print("\nEnter the second date:")

    date2 = get_valid_date()

    difference = abs(
        (date2 - date1).days
    )

    print(
        "\nThe difference between the two dates is:"
    )

    print(
        "%d days" % difference
    )


# ==========================================
#       DATE AFTER / BEFORE N DAYS
# ==========================================

def date_after_before():

    selected_date = get_valid_date()

    while True:

        try:

            days = int(
                input(
                    "Enter number of days: "
                )
            )

            break

        except ValueError:

            print(
                "\nError: Please enter a valid number."
            )

    print("\nChoose an option:")

    print("1. Date after these days")
    print("2. Date before these days")

    while True:

        try:

            choice = int(
                input("Enter your choice: ")
            )

            if choice in [1, 2]:
                break

            print(
                "\nPlease choose 1 or 2."
            )

        except ValueError:

            print(
                "\nError: Enter 1 or 2."
            )

    if choice == 1:

        result = selected_date + timedelta(
            days=days
        )

        print(
            "\nDate after %d days: %s"
            % (
                days,
                result.strftime("%d/%m/%Y")
            )
        )

    else:

        result = selected_date - timedelta(
            days=days
        )

        print(
            "\nDate before %d days: %s"
            % (
                days,
                result.strftime("%d/%m/%Y")
            )
        )


# ==========================================
#        WEEKDAY / WEEKEND CHECK
# ==========================================

def weekday_weekend():

    selected_date = get_valid_date()

    day = selected_date.weekday()

    if day >= 5:

        print(
            "\n%s is a WEEKEND."
            % selected_date.strftime("%A")
        )

    else:

        print(
            "\n%s is a WEEKDAY."
            % selected_date.strftime("%A")
        )


# ==========================================
#        PREVIOUS / NEXT MONTH
# ==========================================

def navigate_month():

    year = get_valid_year()
    month = get_valid_month()

    print("\nChoose an option:")

    print("1. Previous Month")
    print("2. Next Month")

    while True:

        try:

            choice = int(
                input("Enter your choice: ")
            )

            if choice in [1, 2]:
                break

            print(
                "\nPlease choose 1 or 2."
            )

        except ValueError:

            print(
                "\nError: Enter a valid choice."
            )

    # Previous month
    if choice == 1:

        if month == 1:

            month = 12
            year -= 1

        else:

            month -= 1

    # Next month
    else:

        if month == 12:

            month = 1
            year += 1

        else:

            month += 1

    print("\n")

    cal = calendar.TextCalendar(
        calendar.SUNDAY
    )

    cal.prmonth(
        year,
        month
    )


# ==========================================
#       MONTH NAME / MONTH NUMBER
# ==========================================

def month_information():

    print("\nChoose an option:")

    print("1. Month Number → Month Name")
    print("2. Month Name → Month Number")

    while True:

        try:

            choice = int(
                input("Enter your choice: ")
            )

            if choice in [1, 2]:
                break

            print(
                "\nPlease choose 1 or 2."
            )

        except ValueError:

            print(
                "\nError: Enter a valid choice."
            )

    # Number to name
    if choice == 1:

        month = get_valid_month()

        print(
            "\nMonth %d is %s."
            % (
                month,
                calendar.month_name[month]
            )
        )

    # Name to number
    else:

        month_name = input(
            "\nEnter month name: "
        ).strip().lower()

        found = False

        for i in range(1, 13):

            if calendar.month_name[i].lower() == month_name:

                print(
                    "\n%s is month number %d."
                    % (
                        calendar.month_name[i],
                        i
                    )
                )

                found = True
                break

        if not found:

            print(
                "\nError: Invalid month name."
            )


# ==========================================
#             MAIN PROGRAM
# ==========================================

print("\n")
print("==========================================")
print("        CALENDAR & DATE UTILITY")
print("==========================================")

year = get_valid_year()


while True:

    print("\n")
    print("------------------------------------------")
    print("             MAIN MENU")
    print("------------------------------------------")

    print("1.  Display Full Year")
    print("2.  Display Specific Month")
    print("3.  Display Current Month")
    print("4.  Check Leap Year")
    print("5.  Days in a Month")
    print("6.  Find Day of the Week")
    print("7.  Today's Date")
    print("8.  Days Remaining in Year")
    print("9.  Week Number")
    print("10. Date Difference")
    print("11. Date After / Before N Days")
    print("12. Weekday / Weekend Checker")
    print("13. Previous / Next Month")
    print("14. Month Information")
    print("15. Change Year")
    print("16. Exit")

    print("------------------------------------------")


    # ======================================
    #       DISPLAY FULL YEAR
    # ======================================

    if_choice = None

    try:

        choice = int(
            input("Enter your choice: ")
        )

    except ValueError:

        print(
            "\nError: Please enter a number "
            "between 1 and 16."
        )

        continue


    # ======================================
    #              OPTIONS
    # ======================================

    if choice == 1:

        display_full_year(year)


    elif choice == 2:

        display_month(year)


    elif choice == 3:

        current_month()


    elif choice == 4:

        check_leap_year()


    elif choice == 5:

        days_in_month()


    elif choice == 6:

        find_day()


    elif choice == 7:

        todays_date()


    elif choice == 8:

        days_remaining()


    elif choice == 9:

        week_number()


    elif choice == 10:

        date_difference()


    elif choice == 11:

        date_after_before()


    elif choice == 12:

        weekday_weekend()


    elif choice == 13:

        navigate_month()


    elif choice == 14:

        month_information()


    # ======================================
    #             CHANGE YEAR
    # ======================================

    elif choice == 15:

        year = get_valid_year()

        print(
            "\nYear successfully changed to %d."
            % year
        )


    # ======================================
    #                 EXIT
    # ======================================

    elif choice == 16:

        print("\n")
        print("==========================================")
        print("       THANK YOU FOR USING")
        print("        CALENDAR & DATE UTILITY")
        print("==========================================")
        print("                 Goodbye!")
        print("==========================================")

        break


    # ======================================
    #          INVALID CHOICE
    # ======================================

    else:

        print(
            "\nError: Invalid choice!"
        )

        print(
            "Please select a number between 1 and 16."
        )
