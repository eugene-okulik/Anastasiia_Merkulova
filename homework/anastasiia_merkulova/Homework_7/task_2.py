words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for key in words:
    i = 0
    string = ''
    while i < words[key]:
        i += 1
        string += key
    print(string)
