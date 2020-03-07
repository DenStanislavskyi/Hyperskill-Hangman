import random
import string
# List of words


list_of_words = ['python', 'java', 'kotlin', 'javascript', 'c', 'r']
# Pseudorandom choice of a word
correct_word = random.choice(list_of_words)

# Hint to the player
hint_word = '-' * (len(correct_word))
# The player guesses a word
print("H A N G M A N")

letters = set(correct_word)
guessed_letters = set()

trying = 3
while True:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == "play":
        while trying > 0:
            user_word = input(f"\n{hint_word}\nInput a letter: ")

            if user_word in letters:
                count_letters = str.count(correct_word, user_word)
                index = 0
                for letter in range(count_letters):
                    index = str.find(correct_word, user_word, index)
                    hint_word = hint_word[:index] + user_word + hint_word[index + 1:]
                    index += 1
                letters.discard(user_word)
                print(hint_word)
                guessed_letters.add(user_word)
                if len(letters) == 0:
                    print("You guessed the word!\nYou survived!\n")
                    break

            else:
                if user_word in guessed_letters:
                    print("You already typed this letter")
                    guessed_letters.add(user_word)
                elif len(user_word) != 1:
                    print("You should print a single letter")
                elif user_word not in string.ascii_lowercase:
                    guessed_letters.add(user_word)
                    print("It is not an ASCII lowercase letter")
                else:
                    print("No such letter in the word")
                    guessed_letters.add(user_word)
                    trying -= 1
        else:
            print("You are hanged!\n")
    elif play == "exit":
        break
