a=int(input("enter a number :"))

#if statement
if a>0:
    print(f"{a} is a positive number")

#nested if statement
if a>0:
    if a>10:
        print(f"{a} is positive and greater than 10")


#if-else statement
if a%2==0:
    print(a,"is an even number")
else:
    print(a,"is an odd number ")

#nested if else statement
if a>0:
    if a%2==0:
        print(f"{a} is positive and even number")
    else:
        print(f"{a}is positive and odd number")
else:
    if a%2==0:
        print(f"{a} is negative even number ")
    else:
        print(f"{a} is negative odd number ")

 #if-elif-else statement
if a>0:
    print(a,"is a positive number")
elif a<0:
    print(a,"is a negative number")
else:
    print(a,"is zero ")