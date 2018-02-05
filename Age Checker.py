Age = eval(input("Please input your age: "))


if (Age >= 1) and (Age <= 18):
    print("Important Birthday")
elif Age == 21 or Age == 50:
    print("Important Birthday")
elif not (Age <= 65 ):
    print(" Important Birthday")
else:
    print("Not important Birthday")