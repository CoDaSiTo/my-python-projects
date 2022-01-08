'''Pyhton hangman game 2021/01/08 '''

import random
import time
import os

def false_loading(loadtime=random.randint(1,5)):
  '''Waits for loadtime seconds then prints a line of 20 dots.
  If loadtime not specified, it will be a random duration between 1 and 5s.
  '''
  
  time.sleep(loadtime)
  print("."*20, "100%")
    



''' Set-up / Présentation before game starts:'''

os.system("clear -x")

welcome_message = "\nHello and welcome to this very simple hangman game by CoDaSiTo\n"
print(welcome_message)
player_name = input("Enter player name: ")
print(f"Player {player_name} started a game")

#time.sleep(2)

print("\nArranging prisonners to be hanged in a queue:")
#false_loading(3)
print("\nChecking solidity of the ropes:")
#false_loading()
profane = input("\nDo you want to include profane/offensive words in the game?\n(yes: y, no: n)")
while profane not in ("y", "n"):
  profane = input("\nIncorrect entry\nDo you want to include profane/offensive words in the game?\n(yes: y, no: n)")
profane = profane == 'y'
print("\nIncluding offensive words: ", profane) 
print("\nLoading words:")
#false_loading()

''' Loading words according to choice of the player:'''

file_english="wordbank/english-words.10"
file_profane="wordbank/profane.1"

with open(file_english, 'r', encoding="ISO-8859-1") as f:
	WORDS = f.readlines()
WORDS=[word.replace('\n', '') for word in WORDS if "'" not in word] #remove words with apostrophes 
if profane:
	with open(file_profane, 'r', encoding="ISO-8859-1") as f:
	  profane_words=f.readlines()
	WORDS+=[word.replace("\n", "") for word in profane_words if "'" not in word]

print("\nRandom sample of words:")
print( " ; ".join([random.choice(WORDS) for i in range(10)]))

	
print('\n\nGame ready')

word=random.choice(WORDS)

def play_loop(WORDS):
  '''Replay or end game'''
  PLAY=input("Play once more?\n(yes: y ; no: n) ")
  while PLAY not in ("y", "n"):
    PLAY=input("\nIncorrect entry\nPlay once more?\n(yes: y ; no: n) ")
  PLAY=PLAY=="y"
  if PLAY:
    hangman(random.choice(WORDS), GUESSED=[], COUNT=0)
  else:
    print("\nGame shutting off...")
    exit()

def hangman(WORD, GUESSED=[], COUNT=0):
  limit=8

  print("Word:\n", "".join([letter if letter in GUESSED else '_' for letter in WORD]))
  guess = input("\nEnter your letter: ")
  guess = guess.replace(" ","") #remove eventual spaces
  guess=guess.lower()
  guess=guess.strip()

  while len(guess)==0 or len(guess)>1 or guess in '0123456789':
    guess = input("\nIncorrect entry\nEnter a single letter please: ")
    
  if guess in GUESSED:
    print("This letter was already guessed")
    hangman(WORD, GUESSED, COUNT)
  else:
    GUESSED.append(guess)
  
  if guess not in WORD:
    COUNT+=1
    if COUNT<limit:
      print(f"WRONG\n{limit-COUNT} guesses remaining\n")
    if COUNT>=limit:
      print("WRONG\nThe prisonner has been hanged")
      print("The word was: ",WORD)
      play_loop(WORDS)
  if "".join([letter if letter in GUESSED else "_" for letter in WORD])==WORD:
    print("Congratulation, you found: ", WORD)
    play_loop(WORDS)
  elif COUNT<limit:
    hangman(WORD, GUESSED, COUNT)


hangman(random.choice(WORDS)) 
