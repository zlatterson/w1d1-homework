def ageCheck(name, age):
    if age >= 18:
        print(name + " has successfully purchased alcohol")
    else:
        yearsLeft = 18 - age
        print(name + " must wait", yearsLeft, "years")


ageCheck("Andrew", 25)
ageCheck("Timmy", 16)