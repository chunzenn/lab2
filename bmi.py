def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = " + str(weight))
    bmi = (weight/(height**2))
    print(f'Bmi = {bmi:.1f}')
    determine_weight_category(bmi)


def determine_weight_category(bmi):
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi < 25:
        print("Normal Weight")
    else:
        print("Over Weight")

calculate_bmi(weight=57, height=1.73)