def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    Bmi=weight/(height**2)
    if Bmi < -1:
        classification = "Under Weight"
    elif Bmi==0:
        classification = "Normal Weight"
    else:
        classification = "Over Weight"
    print("BMI = {:.2f}".format(Bmi))
    print("Weight Classification: " + classification)
calculate_bmi(weight=57, height=1.73) 