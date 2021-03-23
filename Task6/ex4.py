# Write a program in Python using generators to reverse the string.

def reverse_string(input_str):
    str = ''
    for i in input_str:
        str = i + str
    yield str


input_str = 'Consultadd Training”'

reverse_string(input_str)
for i in reverse_string(input_str):
    print(i)
