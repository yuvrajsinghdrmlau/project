def check_leap_year():
    year = int(input("Enter the Year Do you want to check: "))
    
    if (year % 4==0 and year != 100) or year %400 == 0:
        print("leap year")
    else :
        print("not leap year")


check_leap_year()
    
    