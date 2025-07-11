import random
states_of_america = ["Delaware", "Pennsylvanie", "New Jersey", "Géorgie", "Connecticut", "Massachusetts", "Maryland", "Caroline du Sud", "New Hampshire",
                     "Virginie", "New York", "Caroline du Nord", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiane", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Floride", "Texas", "Iowa", "Wisconsin", "Californie", "Minnesota", "Oregon",
                     "Kansas", "Virginie-Occidentale", "Nevada", "Nebraska", "Colorado", "Dakota du Nord", "Dakota du Sud", "Montana", "Washington", "Idaho",
                     "Wyoming", "Utah", "Oklahoma", "Nouveau-Mexique", "Arizona", "Alaska", "Hawaï"
]
print(states_of_america[0])

states_of_america[0] = "delaware"

print(states_of_america[0])

states_of_america.append(input("choisi l'etat a rajouter : "))



states_of_america.extend([input(" choisis un nouvel état"), random.randint(1234,4567), "hbdksk"])


print(states_of_america)


