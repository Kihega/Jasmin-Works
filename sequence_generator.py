heads = 35
legs = 94

for chickens in range(heads + 1):
    rabbits = heads - chickens

    if (chickens * 2 + rabbits * 4) == legs:
        print("Chickens:", chickens)
        print("Rabbits:", rabbits)
