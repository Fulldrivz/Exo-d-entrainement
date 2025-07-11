print("Welcome to python pizza délivery ")
bill =0
size = input("what size pizza do you whant ? S , M or L ? ")
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("please enter a valid size ")


pepperoni = input("do you whant pepperoni on your pizza ? Y or N ? ")
if pepperoni == "Y" and size == "S":
    bill +=2
elif pepperoni == "Y" and (size  == "M" or size == "L"):
    bill +=3
extra_cheese = input("do you whant extra cheese ? Y or N ? ")
if extra_cheese == "Y ":
    bill +=1

print ("your final bill is " + str(bill) + " $ please .")
