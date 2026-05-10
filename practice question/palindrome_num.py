num=int(input("Enter a number to check palindrome or not :- "))
rem=0
temp=0
clone=num
while num>0:
    rem=num%10
    num=num//10
    temp=temp*10+rem
if clone==temp:
    print(f"{clone} is a palindrome number.")
else:
    print(f"{clone} is not a palindrome number.")
    