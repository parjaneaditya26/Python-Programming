#function is a block of reusable code that can be execute when it is called.
'''def function_name(parameters):          #parameters means input value that we use in function
      code to be executed
   function_name(arguments)         #arguments means input value that we use in function call
      '''

#types of arguments
#1. positional arguments 
'''def add(a,b):   #a and b are parameters
    return a + b     #return is used to return the value from the function
print(add(2,3))  #2 is assigned to a and 3 is assigned to b '''

#2.keyword arguments 
'''def intro(name,age):     
    print(f"my name is {name} and my age is {age}")
intro(age=20,name="Aditya parjane")'''

#3default arguments 
''' def greet(name="guest"):
     print(f"hello {name}")
greet()                        #uses default value guest 
greet("Aditya")        #uses the value you passed in the function call
'''