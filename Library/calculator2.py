def getInput():
    day1=int(input("enter the first date"))
    month1=int(input("enter the first month"))
    year1=int(input("enter the first year"))
    day2=int(input("enter the second date"))
    month2=int(input("enter the second month"))
    year2=int(input("enter the second year"))
    BookType=input("enter book type Standard, Best-Seller, DVD")
    MemberType=input("enter member type: Adult, Student, Senior")
    if year1==year2:
        if month1==month2:
            finalday=day2-day1
        return finalday,BookType,MemberType
def calculateFine(finalday,BookType,MemberType):
    if BookType.lower() == "best-seller":
        rate = 1.00
    elif BookType.lower() == "dvd":
        rate = 2.00
    else:
        rate = 0.50
    fine = finalday * rate
    if MemberType.lower() == "senior":
        fine = fine * 0.50
    elif MemberType.lower() == "student":
        fine = fine * 0.80
    if fine > 15.00:
        fine = 15.00
    return fine
