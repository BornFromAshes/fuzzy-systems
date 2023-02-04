import inference
import defuzzification

class fuzzifier(object):
    def __init__(self, input_dict):
        self.chest_pain = {'typical_anginal': 0, 'atypical_anginal': 0, 'non_aginal_pain': 0, 'asymptomatic': 0}
        self.cholestrol = {'low': 0, 'medium': 0, 'high': 0, 'very_high': 0}
        self.blood_pressure = {'low': 0, 'medium': 0, 'high': 0, 'very_high': 0}
        self.age = {'young': 0, 'mild': 0, 'old': 0, 'very_old': 0}
        self.blood_sugar = {'true': 0, 'false': 0}
        self.exercise = {'true': 0, 'false': 0}
        self.sex = {'male': 0, 'female': 0}
        self.thallium = {'normal': 0, 'medium': 0, 'high': 0}
        self.ECG = {'normal': 0, 'abnormal': 0, 'hypertrophy': 0}
        self.maximum_heart_rate = {'low': 0, 'medium': 0, 'high': 0}
        self.old_peak = {'low': 0, 'terrible': 0, 'risk': 0}
        self.health = {'healthy': 0, 'sick_1': 0, 'sick_2': 0, 'sick_3': 0, 'sick_4': 0}
        self.fuzzy(input_dict)
        infer = inference.inf(self.chest_pain, self.cholestrol, self.blood_pressure, self.age,
                              self.blood_sugar, self.exercise, self.sex, self.thallium, self.ECG,
                              self.maximum_heart_rate, self.old_peak, self.health)
        # print(infer)
        self.health.update(infer)
        output = defuzzification.defuzzy().run(self.health)
        print(output)

    def fuzzy(self, input_dict):
        for input in input_dict:
            if input == 'chest_pain':
                self.chest(input_dict[input])
            elif input == 'cholestrol':
                self.chol(input_dict[input])
            elif input == 'blood_pressure':
                self.blood(input_dict[input])
            elif input == 'age':
                self.fage(input_dict[input])
            elif input == 'blood_sugar':
                self.bloods(input_dict[input])
            elif input == 'exercise':
                self.exer(input_dict[input])
            elif input == 'thallium_scan':
                self.thall(input_dict[input])
            elif input == 'sex':
                self.gen(input_dict[input])
            elif input == 'ecg':
                self.fecg(input_dict[input])
            elif input == 'heart_rate':
                self.heart(input_dict[input])
            elif input == 'old_peak':
                self.old(input_dict[input])

    def chest(self, x):
        out = {list(self.chest_pain.keys())[int(x) - 1]: 1}
        self.chest_pain.update(out)

    def chol(self, x):
        x = int(x)
        if x <= 151:
            self.cholestrol.update({'low': 1})
        if x >= 197:
            self.cholestrol.update({'low': 0})
        if 197 > x > 151:
            self.cholestrol.update({'low': ((197 - x) / (197 - 151))})
        if x <= 188:
            self.cholestrol.update({'medium': 0})
        if x >= 250:
            self.cholestrol.update({'medium': 0})
        if 215 >= x > 188:
            self.cholestrol.update({'medium': ((x - 188) / (215 - 188))})
        if 250 > x > 215:
            self.cholestrol.update({'medium': (250 - x) / (250 - 215)})
        if x <= 217:
            self.cholestrol.update({'high': 0})
        if x >= 307:
            self.cholestrol.update({'high': 0})
        if 263 >= x > 217:
            self.cholestrol.update({'high': ((x - 217) / (263 - 217))})
        if 307 > x > 263:
            self.cholestrol.update({'high': (307 - x) / (307 - 263)})
        if x <= 281:
            self.cholestrol.update({'very_high': 0})
        if x >= 347:
            self.cholestrol.update({'very_high': 1})
        if 347 >= x > 281:
            self.cholestrol.update({'very_high': ((x - 281) / (347 - 281))})

    def blood(self, x):
        x = int(x)
        if x <= 111:
            self.blood_pressure.update({'low': 1})
        if x >= 134:
            self.blood_pressure.update({'low': 0})
        if 134 > x > 111:
            self.blood_pressure.update({'low': ((134 - x) / (134 - 111))})
        if x <= 127:
            self.blood_pressure.update({'medium': 0})
        if x >= 153:
            self.blood_pressure.update({'medium': 0})
        if 139 >= x > 127:
            self.blood_pressure.update({'medium': ((x - 127) / (139 - 127))})
        if 153 > x > 139:
            self.blood_pressure.update({'medium': (153 - x) / (153 - 139)})
        if x <= 142:
            self.blood_pressure.update({'high': 0})
        if x >= 172:
            self.blood_pressure.update({'high': 0})
        if 157 >= x > 142:
            self.blood_pressure.update({'high': ((x - 142) / (157 - 142))})
        if 172 > x > 157:
            self.blood_pressure.update({'high': (172 - x) / (172 - 157)})
        if x <= 154:
            self.blood_pressure.update({'very_high': 0})
        if x >= 171:
            self.blood_pressure.update({'very_high': 1})
        if 171 >= x > 154:
            self.blood_pressure.update({'very_high': ((x - 154) / (171 - 154))})

    def fage(self, x):
        x = int(x)
        if x <= 29:
            self.age.update({'young': 1})
        if x >= 38:
            self.age.update({'young': 0})
        if 38 > x > 29:
            self.age.update({'young': ((38 - x) / (38 - 29))})
        if x <= 33:
            self.age.update({'mild': 0})
        if x >= 45:
            self.age.update({'mild': 0})
        if 38 >= x > 33:
            self.age.update({'mild': ((x - 33) / (38 - 33))})
        if 45 > x > 38:
            self.age.update({'mild': (45 - x) / (45 - 38)})
        if x <= 40:
            self.age.update({'old': 0})
        if x >= 58:
            self.age.update({'old': 0})
        if 48 >= x > 40:
            self.age.update({'old': ((x - 40) / (48 - 40))})
        if 58 > x > 48:
            self.age.update({'old': (58 - x) / (58 - 48)})
        if x <= 52:
            self.age.update({'very_old': 0})
        if x >= 60:
            self.age.update({'very_old': 1})
        if 60 >= x > 52:
            self.age.update({'very_old': ((x - 52) / (60 - 52))})

    def bloods(self, x):
        x = int(x)
        if x >= 120:
            out = {'true': 1}
        elif x <= 105:
            out = {'false': 1}
        else:
            x = (120 - x) / 15
            out = {'false': x, 'true': (1 - x)}
        self.blood_sugar.update(out)

    def thall(self, x):
        x = int(x)
        if x == 7:
            x = 9
        out = {list(self.thallium.keys())[int(x / 3) - 1]: 1}
        self.thallium.update(out)

    def gen(self, x):
        out = {list(self.sex.keys())[int(x)]: 1}
        self.sex.update(out)

    def fecg(self, x):
        x = float(x)
        if x <= 0:
            self.ECG.update({'normal': 1})
        if x >= 0.4:
            self.ECG.update({'normal': 0})
        if 0.4 > x > 0:
            self.ECG.update({'normal': ((0.4 - x) / (0.4 - 0))})
        if x <= 0.2:
            self.ECG.update({'abnormal': 0})
        if x >= 1.8:
            self.ECG.update({'abnormal': 0})
        if 1 >= x > 0.2:
            self.ECG.update({'abnormal': ((x - 0.2) / (1 - 0.2))})
        if 1.8 > x > 1:
            self.ECG.update({'abnormal': (1.8 - x) / (1.8 - 1)})
        if x <= 1.4:
            self.ECG.update({'hypertrophy': 0})
        if x >= 1.9:
            self.ECG.update({'hypertrophy': 1})
        if 1.9 >= x > 1.4:
            self.ECG.update({'hypertrophy': ((x - 1.4) / (1.9 - 1.4))})

    def heart(self, x):
        x = int(x)
        if x <= 100:
            self.maximum_heart_rate.update({'low': 1})
        if x >= 141:
            self.maximum_heart_rate.update({'low': 0})
        if 141 > x > 100:
            self.maximum_heart_rate.update({'low': ((141 - x) / (141 - 100))})
        if x <= 111:
            self.maximum_heart_rate.update({'medium': 0})
        if x >= 194:
            self.maximum_heart_rate.update({'medium': 0})
        if 152 >= x > 111:
            self.maximum_heart_rate.update({'medium': ((x - 111) / (152 - 111))})
        if 194 > x > 152:
            self.maximum_heart_rate.update({'medium': (194 - x) / (194 - 152)})
        if x <= 152:
            self.maximum_heart_rate.update({'high': 0})
        if x >= 210:
            self.maximum_heart_rate.update({'high': 1})
        if 210 >= x > 152:
            self.maximum_heart_rate.update({'high': ((x - 152) / (210 - 152))})

    def old(self, x):
        x = float(x)
        if x <= 1:
            self.old_peak.update({'low': 1})
        if x >= 2:
            self.old_peak.update({'low': 0})
        if 2 > x > 1:
            self.old_peak.update({'low': ((2 - x) / (2 - 1))})
        if x <= 1.5:
            self.old_peak.update({'terrible': 0})
        if x >= 4.2:
            self.old_peak.update({'terrible': 0})
        if 2.8 >= x > 1.5:
            self.old_peak.update({'terrible': ((x - 1.5) / (2.8 - 1.5))})
        if 4.2 > x > 2.8:
            self.old_peak.update({'terrible': (4.2 - x) / (4.2 - 2.8)})
        if x <= 2.5:
            self.old_peak.update({'risk': 0})
        if x >= 4:
            self.old_peak.update({'risk': 1})
        if 4 >= x > 2.5:
            self.old_peak.update({'risk': ((x - 2.5) / (4 - 2.5))})

    def exer(self, x):
        out = {list(self.exercise.keys())[int(x)]: 1}
        self.exercise.update(out)
