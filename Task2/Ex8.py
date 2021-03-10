word = input('Please enter string:')
digits = 0
letters = 0
for x in word:
    if x.isdigit():
        digits += 1
    else:
        letters += 1

print('Letters:', letters, 'Digits:', digits)
