print("Welcome to the tip calculator ")
tbill =float(input("what was the total bill $ ? "))
tip =int(input("How munch tip do you like to give 10, 12 or 15 ? "))
personne = float(input("how many people split the bill  ? "))
aftertips = (tip * tbill ) /100


finalcost= aftertips+tbill
eachcost= finalcost/personne
print(f"Each person should pay {round(eachcost,2)} $")





