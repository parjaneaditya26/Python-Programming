text=input("Enter a text to identify how many chars,number and special chars are there in given in string :- ")
char,num,spec=0,0,0
for i in text:
    if i.isalpha():
        char+=1
    elif i.isdigit():
        num+=1
    else:
        spec+=1
print(f"Characters: {char}\nNumbers: {num}\nSpecial Characters: {spec}")