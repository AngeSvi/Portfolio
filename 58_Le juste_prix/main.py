import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  while True:
    number = random.randint(1,100)
    guess = 101
    while guess != number :
        guess = int(input("Pick a number between 1 and 100: "))
        if guess > number:
          print("Too high")
          attempts+=1
        elif guess < number:
          print("Too low")
          attempts+=1
            
    print("Just right!")
    print(f"{attempts} attempts this round")  
    return attempts

while True:
  menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
  if menu == "1":
    totalAttempts+= game()
  elif menu == "2":
    print(f"You've had {totalAttempts} attempts")
  else:
    break