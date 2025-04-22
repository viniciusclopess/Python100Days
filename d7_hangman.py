import random
words_list = ['mouse', 'bamboo', 'paragraph']
selected_word = random.choice(words_list)
print(selected_word)

blank_word = []
i = 0
for i in range(0, len(selected_word)):
    blank_word.append('_')
    print(blank_word)
    i+=1

lives = 3
win = False

def won_the_game():
    print("Congrats! You won the game!")

def lost_the_game():
    print("Game Over. Try again next time!")

while lives != 0 or win == False:
    letter = input('Guess a letter: ').islower

    continue