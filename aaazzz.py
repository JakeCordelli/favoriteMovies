'''This program is designed to create a dictionary of values ranging from AAA-ZZZ'''


'''Generate a list of values from AAA-ZZZ'''
import string
ltrs=list(string.ascii_lowercase)
'''x holds the list we need'''
x=[''.join([a,b,c]) for a in ltrs for b in ltrs for c in ltrs]
print(x)


'''Map these values to a dictionary'''
