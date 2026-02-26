temperature = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33]


def check_temperature(x):
    return x > 28


high_temperature = filter(check_temperature, temperature)
high_temperature = list(high_temperature)

print(high_temperature)
print(max(high_temperature))
print(min(high_temperature))
print(sum(high_temperature) / len(high_temperature))
