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


def main():
    base_rules = read_filename()
    check_output(base_rules,  [0.0,  1.0,  1.0])


if __name__ == '__main__':
    main()

