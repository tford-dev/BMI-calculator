class bmi_metric:

    def __init__(self, kgs = 1, m = 1):
        self.kgs = kgs
        self.m = m

    def bmi_met(self):
        return kgs / pow(m, 2)

class bmi_imperial:
    def __init__(self, lbs = 1, ins = 1):
        self.lbs = lbs
        self.ins = ins

    def bmi_imp(self):
        return 703 * lbs / pow(ins, 2)

while True:
    print("Welcome Body Mass Index Powered By @tfordfit")
    print("Enter 1 to use METRIC measurements.")
    print("Enter 2 to use IMPERIAL measurements.")
    print("Enter 3 to calculate height in meters.")
    print("Enter 4 to calculate height in inches.")
    print("Enter 5 to exit.")
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        kgs = float(input("Enter your weight in kgs: "))
        m = float(input("Enter your height in m: "))
        met = bmi_metric(kgs, m)
        print(f"Your BMI is {met.bmi_met()}.")
        if met.bmi_met() < 19:
            print("Based on your BMI, you are considered underweight.")
        elif met.bmi_met() > 25:
            print("Based on your BMI, you are considered overweight, but note that the BMI scale does not take into account muscle mass.")
        elif met.bmi_met() >= 30:
            print("Based on your BMI, you are considered obese, but note that the BMI scale does not take into account muscle mass.")
        else:
            print("You are in the healthy range!")

    elif choice == '2':
        lbs = float(input("Enter your weight in pounds(lbs): "))
        ins = float(input("Enter your height in inches: "))
        imp = bmi_imperial(lbs, ins)
        print(f"Your BMI is {imp.bmi_imp()}.")
        if imp.bmi_imp() < 19:
            print("Based on your BMI, you are considered underweight.")
        elif imp.bmi_imp() > 25:
            print("Based on your BMI, you are considered overweight, but note that the BMI scale does not take into account muscle mass.")
        elif imp.bmi_imp() >= 30:
            print("Based on your BMI, you are considered obese, but note that the BMI scale does not take into account muscle mass.")
        else:
            print("You are in the healthy range!")

    elif choice == '3':
        cm = float(input("Enter your height in centimeters: "))
        m = (cm * .01)
        print(f"Your height in meters is {m}.")

    elif choice == '4':
        ft = int(input("Enter your height in feet(you will enter how many inches next): "))
        ins = float(input("Enter the amount of inches you are in ADDITION to your height in feet: "))
        inches_total = (ft * 12) + ins
        print(f"Your height in inches is {inches_total}.")

    elif choice == '5':
        print("Peace be upon you.")
        break
