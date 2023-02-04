def inf(chest_pain, cholestrol, blood_pressure, age,
        blood_sugar, exercise, sex, thallium, ECG,
        maximum_heart_rate, old_peak, health):
    file = open('C:/Users/parham/OneDrive/Desktop/PR2/rules.fcl', 'r')
    lines = file.readlines()
    for line in lines:
        flag = 0
        key2 = []
        value2 = []
        out = []
        oper = ''
        words = line.split()
        words[3] = words[3][1:]
        words[5] = words[5][:-1]
        if words[7] != 'health':
            words[7] = words[7][1:]
            words[9] = words[9][:-1]
            words[13] = words[13][:-1]
            key2 = words[7]
            value2 = words[9]
            out.append(words[13])
            flag = 1
            if words[6] == 'AND':
                oper = 'min'
            if words[6] == 'OR':
                oper = 'max'

        else:
            words[9] = words[9][:-1]
            out.append(words[9])
        key = words[3]
        value = words[5]
        val = vals(chest_pain, cholestrol, blood_pressure, age,
                   blood_sugar, exercise, sex, thallium, ECG,
                   maximum_heart_rate, old_peak, key, value)
        if flag == 1:
            val2 = vals(chest_pain, cholestrol, blood_pressure, age,
                        blood_sugar, exercise, sex, thallium, ECG,
                        maximum_heart_rate, old_peak, key2, value2)
            if oper == 'min':
                val = min(val, val2)
            elif oper == 'max':
                val = max(val, val2)
        health[out[0]] = max(health[out[0]], val)
    return health


def vals(chest_pain, cholestrol, blood_pressure, age,
         blood_sugar, exercise, sex, thallium, ECG,
         maximum_heart_rate, old_peak, key, value):
    if key == 'chest_pain':
        out = chest_pain[value]
    elif key == 'cholesterol':
        out = cholestrol[value]
    elif key == 'blood_pressure':
        out = blood_pressure[value]
    elif key == 'age':
        out = age[value]
    elif key == 'blood_sugar':
        out = blood_sugar[value]
    elif key == 'exercise':
        out = exercise[value]
    elif key == 'sex':
        out = sex[value]
    elif key == 'thallium':
        out = thallium[value]
    elif key == 'ECG':
        out = ECG[value]
    elif key == 'maximum_heart_rate':
        out = maximum_heart_rate[value]
    else:
        out = old_peak[value]
    return out
