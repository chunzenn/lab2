def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = " + str(weight))
    bmi = (weight/(height**2))
    print(f'Bmi = {bmi:.1f}')
    determine_weight_category(bmi)


def determine_weight_category(bmi):
    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif 18.5 <= bmi < 25:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1

calculate_bmi(weight=57, height=1.73)