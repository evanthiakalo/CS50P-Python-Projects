import sys
import inflect
from datetime import date

p = inflect.engine()

def main():
    birth_date_str = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    total_minutes = get_minutes(birth_date, today)
    output = format_words(total_minutes)
    print (output)



def get_minutes(start_date, end_date):
    diff = end_date - start_date
    return diff.days * 24 *60

def format_words(n):
    words = p.number_to_words(n, andword="")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
