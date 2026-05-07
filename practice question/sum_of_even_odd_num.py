num=int(input("Enter a number upto which you want to sum of even or odd numbers in that range :- "))
even_sum=0
odd_sum=0
for i in range(1,num+1):
    if i%2==0:
        even_sum=even_sum +i
    else:
        odd_sum=odd_sum + i 
print(f"Sum of first {num} even number is {even_sum}.")
print(f"Sum of first {num} odd nyumber is {odd_sum}.")   