"""
Read doc.txt file using Python File handling concept and return only the even length string from
the file

"""


with open('doc.txt', 'r') as file:
    # reading each line
    for line in file:

        # reading each word
        for word in line.split():
            if len(word) % 2 == 0:
                print(word)
