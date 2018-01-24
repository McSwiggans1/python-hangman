import random

#Uses text file with random words in it
secret_word = random.choice(open('words.txt').read().split()).strip()
x = ['-' for _ in secret_word]
lives = 15
def get_guess(secret_word):
    while True:
        print("==========")
        guess = input("Guess: ")
        if guess == "break":
            break
        elif not guess.islower():
            print("Your guess must be a lowercase letter")
        elif len(guess) != 1:
            print("Your guess must be one letter")
        else:
            return guess


def update_dashes(secret_word, x, letter):
    global lives
    if letter not in secret_word:
      lives -= 1
      print("Lives:", lives)
      print(''.join(x))
    else:
      for i in range(0, len(secret_word)):
        if letter == secret_word[i]:
            x[i] = letter
      print(''.join(x))
print("Welcome to Hangman v0.2 by Yuryi Mironchyk")
print("You have",lives,"lives and must guess",''.join(x))

while '-' in x:
    letter = get_guess(secret_word)
    update_dashes(secret_word, x, letter)
    if lives == 0:
      print("==========") 
      print("!!! Game Over !!!")
      print("The word was \'", secret_word, "\'")
      break
    elif '-' not in x:
      print("==========")
      print("Victory! With", lives, "lives left!")
      
  



    
