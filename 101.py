# Program 101
'''
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"
Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5
hamming_distance("abcde", "abcde") ➞ 0
hamming_distance("strong", "strung") ➞ 1'''

def a(b,c):
    d=0
    for x in range(len(b)):
        if b[x]!=c[x]:
            d+=1
    print(d)
a("abcde", "bcdef")
a("abcde", "abcde")
a("strong", "strung")        