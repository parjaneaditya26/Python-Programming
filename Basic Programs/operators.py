#arithmetic operators use BODMAS rule. BODMAS stands for Brackets, Orders, Division, Multiplication, Addition and Subtraction.

a=10
b=20
print(a+b) 
print(a-b)
print(a*b)
print(a/b)
print(a//b) #floor division gives integer value of the division
print(a%b) #modulus gives reminder of the division
print(a**b) #exponentiation gives the value of a raised to the power of b

#compound assignment operators
a=10 #assining value
a+=5 #a=a+5
a-=5 #a=a-5
a*=5 #a=a*5
a/=5 #a=a/5
a//=5 #a=a//5
a%=5 #a=a%5
a**=5 #a=a**5
print(a)

#comparison operators

x=10
y=50
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#logical operater 
print(x>y and x!=y)
print(x<y or x==y)
print(not(x>y))
print(not(x<y and x!=y))
