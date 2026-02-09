first_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
              'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
first_text = first_text.split()

for item in first_text:
    if item.endswith(',') or item.endswith("."):
        item = item[:-1] +'ing'
    else:
        item = item + 'ing'

    print(item)
