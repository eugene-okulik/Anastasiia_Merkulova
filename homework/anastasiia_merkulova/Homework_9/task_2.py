temperature = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33]
high_temperature = []
for x in temperature:
    if x > 28:
        high_temperature.append(x)

print(high_temperature)
print(max(high_temperature))
print(min(high_temperature))
print(sum(high_temperature) / len(high_temperature))
