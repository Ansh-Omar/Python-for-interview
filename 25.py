'''Program 25
 Write a Python Program To Find ASCII value of a character.
 ASCII value:
 ASCII, or American Standard Code for Information Interchange, is a character encoding
 standard that uses numeric values to represent characters. Each ASCII character is
 assigned a unique 7-bit or 8-bit binary number, allowing computers to exchange information
 and display text in a consistent way. The ASCII values range from 0 to 127 (for 7-bit ASCII)
 or 0 to 255 (for 8-bit ASCII), with each value corresponding to a specific character, such as
 letters, digits, punctuation marks, and control characters.'''

#ASCII VALUE OF A CHARACTER

b=0
while b==0:
    a=input("Enter character : ")
    print("The ASCII value of character",a,"is",ord(a),"\n")