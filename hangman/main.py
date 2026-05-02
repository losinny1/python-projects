import random 
from hangman_art import stages, logo
from hangman_words import word_list
lives = 6 
chosen_word = random.choice(word_list)
print(logo)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
  placeholder += "_"
print("Guess a letter: " + placeholder)
game_over = False
correct_letters = []
already_guessed = []
while not game_over:
  print("*****YOU HAVE " + str(lives) = " LIVES LEFT*****")
  guess = input("Guess a letter: ").lower()
  display = ""
  if guess in already_guessed:
    print("You already guessed this letter!")
  else: 
    already_guessed.append(guess)

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else: 
      display += "_"
  print("Word to guess: " + display)

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word!. You lose a life!")
    if lives == 0:
      game_over = True
      print(f"You lose! The word was {chosen_word}.")
  if "_" not in display:
    game_over = True 
  print(stages[lives])
