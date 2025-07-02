import random

# List of predefined words
words = ['apple', 'tiger', 'house', 'train', 'plane']

# Randomly select a word
word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print(f"The word has {len(word)} letters.")

# Game loop
while wrong_guesses < max_guesses:
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(display_word.strip())

    if '_' not in display_word:
        print("🎉 Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        print("❌ Incorrect guess!")
        wrong_guesses += 1
        print(f"Wrong guesses: {wrong_guesses}/{max_guesses}")

else:
    print(f"💀 Game over! The word was '{word}'.")
