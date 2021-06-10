import pandas as pd


def read_filename():
    base_rules = pd.read_excel('BaseRules.xlsx', engine='openpyxl')
    base_rules = base_rules.drop([24])
    print(base_rules)
    return base_rules


def check_output(base_rules, inputs):
    output = []
    for i in range(len(base_rules)):
        if base_rules.iloc[i][0] == inputs[0] and base_rules.iloc[i][1] == inputs[1] \
                and base_rules.iloc[i][2] == inputs[2]:
            output.append(base_rules.iloc[i][3])
            output.append(base_rules.iloc[i][4])
            print(output)
            return output
    return "These inputs are not allowed"


def defuzzification(output_values, min_values):
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
    base_rules = read_filename()
    # a3ml call llfunctions hna
    

if __name__ == '__main__':
    main()
