import random

word_list = ["apple", "banana", "cherry"]
word = random.choice(word_list)
guesses = 6

while guesses > 0:
    guess = input("Guess a letter or the word: ")
    if guess == word:
        print("You won!")
        break
    elif guess in word:
        print("Good guess!")
    else:
        guesses -= 1
        print(f"Incorrect! {guesses} guesses left.")
    if guesses == 0:
        print(f"Game over! The word was {word}.")