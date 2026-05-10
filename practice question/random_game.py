import random
print("Welcome to the random number guessing game!")
num=random.randint(1,100)
tries=0
print("Try to guess the number between 1 and 100. You have 11 tries.")
while True:
    guess=int(input("Enter your guess between 1 and 100 :- "))
    tries+=1
    if(guess==num):
        print(F"Congratulations you guessed the number {num} in {tries} tries!")
        break
    elif tries>10:
        print(f"Sorry you have used all your tries. The number was {num}. Better luck next time!")
        break
    elif(guess>num):
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low.Try again.")
    