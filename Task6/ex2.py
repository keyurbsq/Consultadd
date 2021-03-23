"""
 Write a program to construct a dictionary from the two lists containing the names of students and
 their corresponding subjects. The dictionary should map the students with their respective subjects.
 Let’s see how to do this using for loops and dictionary comprehension
"""

students_keys = ['Smit', 'Jaya', 'Rayyan']
subjects_values = ['CSE', 'Networking', 'Operating System']

#res = {students_keys[i]: subjects_values[i] for i in range(len(students_keys))}

res = dict(zip(students_keys, subjects_values))

print("Students with their respective subjects: " + str(res))
