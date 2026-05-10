string=input("Enter a string that check its palindrome or not :- ").lower()
text=string.replace(" ","").replace(",","").replace(".","")
print(text)
rev=text[::-1]
if rev==text:
    print(f"{string} is a palindrome string.")
else:
    print(f"{string} is not a palindrome string.")