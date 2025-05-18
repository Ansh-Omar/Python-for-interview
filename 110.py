# Program 110
'''
Create a function that takes a single string as argument and returns an ordered list
containing the indices of all capital letters in the string.
Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]
index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
index_of_caps("determine") ➞ []
index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
index_of_caps("sUn") ➞ [1]'''

def index_of_caps(b):
    c=[]
    for x in range(len(b)):
        if b[x].isupper():
            c.append(x)
    print(c)
index_of_caps("eDaBiT")
index_of_caps("eQuINoX") 
index_of_caps("determine")
index_of_caps("STRIKE")
index_of_caps("sUn")