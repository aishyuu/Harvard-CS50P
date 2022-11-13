def energy(mass):
    return(mass * (300000000 ** 2))

userMass = int(input("m: "))
print(f"e: {energy(userMass)}")