#output 
#1.standerd output: print() function is used to display output on the console.
#2.formatted output: we can use formatted string to display output in a specific format. we can use f-string or format() method to format the output.
name="aditya"
age=19
print(f"My name is {name} and I am {age} years old.") #output: My name is aditya and I am 19 years old.formatted output using f-string
print("My name is ",name," and my age is ",age) #output: My name is  aditya  and my age is  19. standard output using print() function
print("My name is {} and I am {} years old.".format(name,age)) #output: My name is aditya and I am 19 years old.formatted output using format() method

#INPUT
a=input("Enter your name: ") #input() function is used to take input from the user. it takes input as a string by default.
print("Your name is ",a) #output: Your name is  aditya. standard output using print() function
b=int(input("Enter your age: ")) #type casting input to integer using int() function
print("Your age is ",b) #output: Your age is  19. standard output using print() function
print(f"Your name is {a} and your age is {b}.") #output: Your name is aditya and your age is 19. formatted output using f-string    
