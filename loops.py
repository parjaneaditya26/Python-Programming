#Loops in the python allow us to execute a block of code multiple times.

# ---------------------for loop------------------------------------------ 
# in that use range() function , range(start,stop,step)
# range is always start with 0 upto n-1 and step is 1 . bur its changable
sen="My name is Aditya"

'''for i in range(1, 21, 2):
    print(i)

sen="My name is Aditya"
for char in range(len(sen)): #len(0,7) and len(7) is same as len(sen)
    print(sen[char])

for i in sen:
    print(i)'''

#for j in range(len(sen)-1,-1,-1):
#    print(sen[j])

#-----------------Break ,continue and else statement------------------
"""for i in range(0,20):
    if i==15:
        print("Break statement is executed ")
        break
    if i==10:
        print("Continue statement is executed")
        continue 

    print(i)
else:                                   
    print("Else statement is executed ") #if for loop will not execute then else block will be executed """

#-----------------While loop------------------------------------------
#while condition:
    #code to be executed 
#in that condition is true then code will be executed otherwise it will not be executed
#while loop is used when we dont know the number of iterations