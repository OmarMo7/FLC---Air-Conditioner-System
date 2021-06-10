import pandas as pd
UT = int(input("Enter the user temperature value: "))
DT = float(input("Enter the difference in temperatue between in and out: "))
EV = int(input("Enter the electric volt value: "))


def UT_Calculator(UT):
    Low = 0
    Medium = 0
    High = 0
    if (UT >= 16 and UT <= 22):
        Low = 1
    elif(UT >= 22 and UT <= 25):
        Low = (25-UT)/3
        Medium = (UT-22)/3
    if(UT >= 25 and UT <= 28):
        Medium = (28 - UT)/3
        High = (UT-25)/3
    elif(UT >= 28 and UT <= 34):
        High = 1
    return Low, Medium, High


def DT_Calculator(DT):
    Negative = 0
    Zero = 0
    Positive = 0
    Large = 0
    if (DT >= -1 and DT <= -0.9):
        Negative = 1
    elif(DT >= -0.9 and DT <= 0):
        Negative = -0.9 * DT
        Zero = 2*(DT + 0.5)
    if(DT >= 0 and DT <= 0.5):
        Zero = 2*(0.5 - DT)
    if(DT >= 0 and DT <= 1):
        Positive = DT
    if(DT >= 1 and DT <= 2):
        Positive = 2 - DT
        Large = 1 - DT
    elif(DT >= 2 and DT <= 3):
        Large = 1
    return Negative, Zero, Positive, Large


def EV_Calculator(EV):
    Low = 0
    High = 0

    if (EV >= 130 and EV <= 160):
        Low = 1
    elif (EV >= 160 and EV <= 180):
        Low = (180 - EV)/20
    if (EV >= 170 and EV <= 190):
        High = (EV - 170)/20
    elif (EV >= 190 and EV <= 220):
        High = 1
    return Low, High


def Get_Combinations(Fuzzy_UT, Fuzzy_DT, Fuzzy_EV):
    Pos_UT = []
    Pos_DT = []
    Pos_EV = []
    for value in Fuzzy_UT:
        if (value != 0):
            if (not Pos_UT.__contains__(Fuzzy_UT.index(value))):
                Pos_UT.append(Fuzzy_UT.index(value))
            else:
                lastIndex = Fuzzy_UT.index(value)
                Pos_UT.append(Fuzzy_UT.index(value, lastIndex+1))

    for value in Fuzzy_DT:
        if (value != 0):
            if (not Pos_DT.__contains__(Fuzzy_DT.index(value))):
                Pos_DT.append(Fuzzy_DT.index(value))
            else:
                lastIndex = Fuzzy_DT.index(value)
                Pos_DT.append(Fuzzy_DT.index(value, lastIndex+1))
    for value in Fuzzy_EV:
        if (value != 0):
            if (not Pos_EV.__contains__(Fuzzy_EV.index(value))):
                Pos_EV.append(Fuzzy_EV.index(value))
            else:
                lastIndex = Fuzzy_EV.index(value)
                Pos_EV.append(Fuzzy_EV.index(value, lastIndex+1))

    Combinations = []
    for i in Pos_UT:
        for j in Pos_DT:
            for k in Pos_EV:
                Combinations.append([i, j, k])
    return Combinations


def Get_Minimums(Combinations, Fuzzy_UT,
                 Fuzzy_DT,
                 Fuzzy_EV):
    min_values = []
    for i in Combinations:
        min_values.append(min(Fuzzy_UT[i[0]], Fuzzy_DT[i[1]], Fuzzy_EV[i[2]]))
    return min_values


def Read_Filename():
    base_rules = pd.read_excel('BaseRules.xlsx', engine='openpyxl')
    base_rules = base_rules.drop([24])
    print(base_rules)
    return base_rules


def Check_Output(base_rules, inputs):
    output = []
    for i in range(len(base_rules)):
        if base_rules.iloc[i][0] == inputs[0] and base_rules.iloc[i][1] == inputs[1] \
                and base_rules.iloc[i][2] == inputs[2]:
            output.append(base_rules.iloc[i][3])
            output.append(base_rules.iloc[i][4])
            print(output)
            return output
    return "These inputs are not allowed"


def Defuzzification(output_values, min_values):
    low, medium, fast = 0, 0, 0
    for i in range(len(min_values)):
        for j in range(2):
            if output_values[i][j] == 0:
                low += min_values[i] * 30
            elif output_values[i][j] == 1:
                medium += min_values[i] * 60
            elif output_values[i][j] == 2:
                fast += min_values[i] * 90
    return (low + medium + fast) / sum(min_values)


def main():
    base_rules = Read_Filename()
    Fuzzy_UT = UT_Calculator(UT)
    Fuzzy_DT = DT_Calculator(DT)
    Fuzzy_EV = EV_Calculator(EV)

    Combinations = Get_Combinations(Fuzzy_UT,
                                    Fuzzy_DT,
                                    Fuzzy_EV)
    Mins = Get_Minimums(Combinations, Fuzzy_UT,
                        Fuzzy_DT,
                        Fuzzy_EV)
    Outputs = Check_Output(base_rules, Combinations)

    Defuzzification(Outputs, Mins)


if __name__ == '__main__':
    main()
