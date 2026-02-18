from random import randint, choice

salary = int(input("Enter your salary: "))
bonus = choice([True, False])
if bonus == True:
    random_bonus = randint(40, 1000) + salary
    print(f"{salary}, {bonus} - '${random_bonus}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")




