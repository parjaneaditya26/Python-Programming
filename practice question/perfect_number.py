num=int(input("Enter a number to finds it is perfect number or not:- "))
print(f"The factors of {num} are :- ")
add_fac=0
for i in range(1,num):
    if num%i==0:
        add_fac=add_fac+i

if add_fac==num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")