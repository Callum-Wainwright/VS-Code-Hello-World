from datetime import date

def calculateDays(day1, month1, year1, day2, month2, year2):
    """Calculates the exact number of days between two dates using Python's datetime library."""
    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)
    return (date2 - date1).days

def getInput():
    """Prompts user for input and calculates days overdue."""
    day1 = int(input("enter the first date: "))
    month1 = int(input("enter the first month: "))
    year1 = int(input("enter the first year: "))
    day2 = int(input("enter the second date: "))
    month2 = int(input("enter the second month: "))
    year2 = int(input("enter the second year: "))
    BookType = input("enter book type Standard, Best-Seller, DVD: ")
    MemberType = input("enter member type: Adult, Student, Senior: ")
    
    finalday = calculateDays(day1, month1, year1, day2, month2, year2)
    return finalday, BookType, MemberType

def calculateFine(finalday, BookType, MemberType):
    """Calculates late fine based on item type, member discounts, and a £15.00 maximum fine cap."""
    book = BookType.lower()
    if book == "best-seller":
        rate = 1.00
    elif book == "dvd":
        rate = 2.00
    else:
        rate = 0.50

    fine = finalday * rate

    member = MemberType.lower()
    if member == "senior":
        fine *= 0.50 
    elif member == "student":
        fine *= 0.80  

    if fine > 15.00:
        fine = 15.00

    return fine