weight=input("Weight :")
ans=input("(L)bs or (K)g :")

kilo_to_pounds=int(weight)* 0.45
pounds_to_kilo=int(weight) / 0.45

if ans.upper() == "L":
    print(f"Your weight is {kilo_to_pounds} in pounds")

elif ans.upper() == "K":
    print(f"Your weight is {pounds_to_kilo} in pounds")
