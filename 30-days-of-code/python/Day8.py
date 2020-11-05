# Enter your code here. Read input from STDIN. Print output to STDOUT

inputVal = int(input())
phone_book={}

for i in range(inputVal):
    name_phone=input().split()
    name = name_phone[0]
    phone = int(name_phone[1])
    phone_book[name] = phone


while True:
    try:
        searchVal = input()
        if searchVal in phone_book:
            print('%s=%s' % (searchVal, phone_book[searchVal]))  //I like this representation
        else:
            print('Not found')
    except:
        break

