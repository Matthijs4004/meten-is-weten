
getalA = int(input("Getal A: "))
getalB = int(input("Getal B: "))

if getalA > getalB:
    print("A is het grootste getal")
elif getalA < getalB:
    print("A is het kleinste getal")
else:
    print("A en B zijn even groot")

if getalA > getalB:
    print("Het minimum is: " + str(getalB))
    print("Het maximum is: " + str(getalA))
elif getalA < getalB: 
    print("Het minimum is: " + str(getalA))
    print("Het maximum is: " + str(getalB))