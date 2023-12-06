name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))

BMI = round((weight * 703) / (height * height), 2)

print("Your Body Mass Index (BMI) is: ", BMI)

if BMI>0:
    if(BMI < 18.5):
        print(name +", you are underweight.")
    elif (BMI <= 24.9):
        print(name +", you are normal weight.")
    elif (BMI <= 29.9):
        print(name +", you are overweight.")
    elif (BMI <= 34.9):
        print(name +", you are obese.")
    elif (BMI <= 39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Please enter valid input")