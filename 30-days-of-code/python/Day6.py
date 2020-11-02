# Enter your code here. Read input from STDIN. Print output to STDOUT
num_characters = int(input())
for i in range(num_characters):
    s=input()
    print(s[::2],s[1::2])
    
# Using Extended Splices

'''
Input:
2
Hacker
Rank

num_characters = int(input()) => Obtains 2, which indicates the 2 inputs, Hacker and Rank

for i in range(2):   => running through numbers 0,1
s = input() => 1st input: Hacker, 2nd input: Rank
s[::2] ==> Obtains the indices 0,2,4,6,... in the word, so for Hacker, it becomes Hce
s[1::2] ==> Obtains the indices 1,3,5,... start at 1 and increment of 2, so for Hacker, it becomes akr

Output:
Hce akr
Rn ak
'''
