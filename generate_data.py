import random
with open("data.csv", "w") as f:
    for i in range(1000):
        f.write(f"{i},{random.randint(0,10)} \n")