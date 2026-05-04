name=input("Enter your name :- ")
age=int(input("Enter your age :- "))
if age>=18:
    print(f"Hello {name} ! you are eligible to vote.")
else:
    years_left=18-age
    print(f"Hello {name} ! you are not eligible to vote. You will be eligible after {years_left} years.")