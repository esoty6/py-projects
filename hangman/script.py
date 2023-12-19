import random

  
someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
  
someWords = someWords.split(' ') 

word = random.choice(someWords) 

chances = 5

letters = []

guessedWord = "";

for _ in word:
  print("_ ", end="")
  
print()

while chances > 0:
  guess = input('Guess the letter: ')[0]
  
  while guess in letters or not guess.isalpha():
    guess = input("Enter different character: ")[0]
    
  letters.append(guess)

  if guess not in word:
    chances -= 1
    if chances == 0:
      print(f"\nYou've lost! Try again...")
      break
    else:
      print(f'\nTry again! Chances: {chances}\n')
      continue
  
  guessedWord = ""
  
  print()
  
  for w in word:
    if w in letters:
      guessedWord += w;
      print(f"{w} ", end="")
    else:
      print("_ ", end="")
        
  print()
  print()
  
  if guessedWord == word:
    print("You've won! Congratulations")
    break