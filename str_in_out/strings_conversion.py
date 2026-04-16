#strings


a="ADITYA PARJANE"
print(a)

#indexing in string
print(a[0]) #output: A
print(a[6]) #output: 
print(a[-1]) #output: E
print(a[-14]) #output: A

#slicing in string
#variable[start:end:step]
print(a[0:6]) #output: ADITYA 
print(a[7:]) #output: PARJANE
print(a[0:14:2]) #output: AIY AJN

print(a[::]) #output: ADITYA PARJANE
print(a[::-1]) #output: ENAJRAP AYTIDA
print(a[::-2]) #output: EARPATD

#type casting or type conversion
#false values in python: 0, 0.0, '', [], {}, (), None, False

num1=10
num2=3.14
print(str(num1)) #output: '10'
print(str(num2)) #output: '3.14'    
num3=5
print(str(num3)) #output: '5'
print(bool(num3)) #output: True
num4=0
print(bool(num4)) #output: False
num5=None
print(bool(num5)) #output: False
num6='5'
print(int(num6)) #output: 5
print(float(num6)) #output: 5.0