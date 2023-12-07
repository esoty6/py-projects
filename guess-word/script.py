import random


words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

turns = 10

guesses = ''

while turns > 0:
  guess = input('Guess the character: ')[0]
  answer = ''

  while guess in guesses:
    guess = input(f"You already guessed '{guess}'. Try another one: ")[0]
    
  guesses += guess
  
  if guess not in word:
    print('Wrong')
    turns -= 1
    print('You have', turns, 'more guesses')
    continue
  
  print('Your guess: ', end="")
  for char in word:
    if char in guesses:
      print(char, end='')
      answer += char
    else:
      print('_', end="")
      
  print()
      
  if answer == word:
    print('\nYou win!')
    break
 
 
if turns <= 0:
  print('\nYou loose')
print('The word was:', word)

  