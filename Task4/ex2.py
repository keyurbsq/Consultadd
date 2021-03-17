# Write a function that accepts a string and prints the number of uppercase letters and lowercase letters

str = input('Please enter string which you would like to count letters by uppercase & lowercase:')


def count_letters(str):
    u_count = 0
    l_count = 0
    for i in str:
        if i.isupper():
            u_count += 1
        else:
            l_count += 1
    return 'Uppercase Letters:', u_count, 'Lowercase Letters:', l_count


print(count_letters(str))
