def progression ():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


count = 0

for number in progression():
    count += 1
    if count == 5:
        print(number)
    if count == 200:
        print(number)
    if count == 1000:
        print(number)
    if count == 100000:
        print(number)
        break
