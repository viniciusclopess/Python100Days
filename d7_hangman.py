import random

words_list = ['mouse', 'bamboo', 'paragraph']
selected_word = random.choice(words_list)

blank_word = []
for i in range(len(selected_word)):
    blank_word.append('_')
    print(blank_word)

lives = 3
win = False

def won_the_game():
    print("Congrats! You won the game!")
    print(f"The word was {selected_word}")

def lost_the_game():
    print("Game Over. Try again next time!")

while win == False:
    if lives <= 0:
        lost_the_game()
        break
    elif '_' not in blank_word:
        won_the_game()
        win = True
    else:
        letter = input('Guess a letter: ').lower()
        i = 0
        found = False
        while i < len(selected_word):
            if letter == selected_word[i] and blank_word[i] == '_':
                blank_word[i] = letter
                found = True
            i += 1
        print(blank_word)
        if found:
            continue
        else:
            lives -= 1
            print(f"You lost a life! Lives remaining {lives}.")
