def is_leap(year):
    if year % 4 != 0:
        print("為平年")
        return False
    elif (year % 4 == 0) and (year % 100 != 0):
        print("為閏年")
        return True
    elif (year % 100 == 0) and (year % 400 != 0):
        print("為平年")
        return False
    elif (year % 400 == 0) and (year % 3200 != 0):
        print("為閏年")
        return True


is_leap(2005)
print(is_leap(2005))
