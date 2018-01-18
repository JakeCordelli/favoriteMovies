'''This program is designed to create a dictionary of values ranging from AAA-ZZZ'''


'''Generate a list of strings from AAA-ZZZ'''
import string
ltrs=list(string.ascii_lowercase)
'''x holds the list we need'''
x=[''.join([a,b,c]) for a in ltrs for b in ltrs for c in ltrs]
#print(x)


'''Map these strings to values in a dictionary'''
dictionary={}

for i in range(17576):
    dictionary[x[i]]=i

print (dictionary)

