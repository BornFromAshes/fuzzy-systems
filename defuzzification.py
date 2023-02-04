class defuzzy(object):
    def run(self, fuzzy):
        # print(fuzzy)
        n = 1000
        dx = 4.0/n
        integ = 0
        x = 0
        weighted_integ = 0
        for j in range(n):
            r0 = min(self.healthy(x), fuzzy['healthy'])
            r1 = min(self.sick_1(x), fuzzy['sick_1'])
            r2 = min(self.sick_2(x), fuzzy['sick_2'])
            r3 = min(self.sick_3(x), fuzzy['sick_3'])
            r4 = min(self.sick_4(x), fuzzy['sick_4'])

            maxim = max(r0, r1, r2, r3, r4)
            # print(maxim)
            integ += maxim
            weighted_integ += maxim * x

            x += dx

        weighted_integ /= integ
        string = ""
        if weighted_integ < 1.78:
            string += "healthy"
        if 1 < weighted_integ < 2.51:
            if string != "":
                string += " & "
            string += "sick1"
        if 1.78 < weighted_integ < 3.25:
            if string != "":
                string += " & "
            string += "sick2"
        if 1.5 < weighted_integ < 4.5:
            if string != "":
                string += " & "
            string += "sick3"
        if 3.25 < weighted_integ:
            if string != "":
                string += " & "
            string += "sick4"
        return string + ": " + str(weighted_integ)

    def healthy(self, x):
        if x <= 0.25:
            return 1
        if x >= 1:
            return 0
        return (1 - x) / (1 - 0.25)

    def sick_1(self, x):
        if x >= 2:
            return 1
        if 0 <= x <= 1:
            return (x - 0) / (1 - 0)
        if 1 < x < 2:
            return (2 - x) / (2 - 1)

    def sick_2(self, x):
        if x <= 1:
            return 0
        if x >= 3:
            return 0
        if 1 < x <= 2:
            return (x - 1) / (2 - 1)
        if 2 < x < 3:
            return (3 - x) / (3 - 2)

    def sick_3(self, x):
        if x <= 2:
            return 0
        if x >= 4:
            return 0
        if 2 < x <= 3:
            return (x - 2) / (3 - 2)
        if 3 < x < 4:
            return (4 - x) / (4 - 3)

    def sick_4(self, x):
        if x <= 3:
            return 0
        if x >= 3.75:
            return 1
        if 3 < x < 3.75:
            return (x - 3) / (3.75 - 3)
