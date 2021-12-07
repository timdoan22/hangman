import random
from hangman_art import *
from hangman_words import word_list

chosen_word = random.choice(word_list)

# print(chosen_word)

display = []

lives = 6
hangman_counter = -1

print(logo)

for letter in chosen_word:
    display += '_'

end_of_game = False
guess_letters = ''

while not end_of_game:
    guess = input("Enter a letter. ").lower()
    if guess in guess_letters:
        print("You have already guessed this letter, please enter a different letter!")
        guess
    else:
        for n in range(len(chosen_word)):
            char_position = chosen_word[n]
            if guess == char_position:
                display[n] = char_position
            # display.pop(n)
            # display.insert(n, guess)
    print(" ".join(display))

    if guess not in chosen_word and guess not in guess_letters:
        print(
            f"You guessed {guess}, that's not in the word.  You lose a life.")
        lives -= 1
        hangman_counter -= 1
    else:
        lives = lives
        hangman_counter = hangman_counter

    guess_letters += guess

    if "_" not in display and ''.join(display) == chosen_word:
        end_of_game = True
        print('You Win. You spared the hangman from his death!')
    elif lives == 0:
        end_of_game = True
        print(f"You Lose. The word was {chosen_word}. Better luck next time!")

    print(stages[hangman_counter])
