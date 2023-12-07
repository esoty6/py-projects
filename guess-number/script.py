import random


randomNumber = random.randint(0, 100)

def get_user_guess():
  global userGuess
  userGuess = int(input('Guess number: '))

get_user_guess()

while userGuess != randomNumber:
  if userGuess < randomNumber:
    print('Try again! You guessed too small')
  else:
    print('Try again! You guessed too big')
  get_user_guess()
  
print("Congrats you guessed the number!")

