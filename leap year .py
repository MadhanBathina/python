# leap year checker 

def isleapyear(year):

    if year.isnumeric:
        year=int(year)
        if type(year) == int:
            if year%4 == 0:
                if year%100 == 0:
                    if year%400 == 0:
                        return True
                    else:
                        return False
                else:
                        return True
            else:
                return False
    else :
        return "pleae enter int value"
year=input()
print(isleapyear(year))