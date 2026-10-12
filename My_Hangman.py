import random
from hangman_words import word_list
from hangman_art import stages, logo




lives = 6


print(logo)
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []


while not game_over:


    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    if guess in correct_letters and guess in guessed_letters:
        print(f"You have already guessed the letter {guess}!")
    elif guess in guessed_letters:
        print(f"You have already guessed the letter {guess}! Don't waste lives..")

    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            guessed_letters.append(guess)
        elif letter in correct_letters:
            display += letter
            guessed_letters.append(guess)
        else:
            display += "_"
            guessed_letters.append(guess)

    print("Word to guess: " + display)



    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True


            print(f"***********************YOU LOSE**********************")
            print(f"the correct word was {chosen_word}! Better luck next time!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        print(f"the correct word was {chosen_word}! Congratulations! :)")


    print(stages[lives])
