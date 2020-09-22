"""
You are given a string .
 contains alphanumeric characters only.
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Output Format

Output the sorted string .

Sample Input

Sorting1234

Sample Output

ginortS1324

Brilliant Answer:
"""

l,u,o,e=[],[],[],[]

for i in sorted(input()):
    if i.isalpha():
        x = u if i.isupper() else l
    else:
        x = o if int(i)%2 else e
    x.append(i)
print("".join(l+u+o+e))
