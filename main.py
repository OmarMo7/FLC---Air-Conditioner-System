UT = input("Enter the user temperature value: ")
DT = input("Enter the difference in temperatue between in and out: ")
EV = input("Enter the electric volt value: ")


def UT_Calculator(UT):
    Low = 0
    Medium = 0
    High = 0
    if (UT > 16 and UT < 22):
        Low = 1
    if(UT > 22 and UT < 25):
        Low = (25-UT)/3
    if(UT > 22 and UT < 25):
        Medium = (UT-22)/3
    if(UT > 25 and UT < 28):
        Medium = (28 - UT)/3
    if(UT > 25 and UT < 28):
        High = (UT-25)/3
    if(UT > 28 and UT < 34):
        High = 1
    return Low, Medium, High
