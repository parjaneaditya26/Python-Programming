num=int(input("Enter a number upto which you want to sum:- "))
sum=0
for i in range(0,num+1):
    sum=sum+i
print(f"sum of first {num} natural number is {sum}.")