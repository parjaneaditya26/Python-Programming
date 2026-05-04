temp=float(input("Enter the temperature in celsius :- "))
if temp<0:
    print(f"{temp} is freezing cold temerature.")
elif temp>=0 and temp<=10:
    print(f"{temp} is very cold temperature.")
elif temp>10 and temp<=20:
    print(f"{temp} is cold temoerature.")
elif temp>20 and temp<=30:
    print(f"{temp} is pleasant temperature.")
elif temp>30 and temp<=40:
    print(f"{temp} is hot temperature.")
elif temp>40:
    print(f"{temp} is very hot temperature.")