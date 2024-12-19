import random
from games.module import hangmandata

chosen_fruit = random.choice(hangmandata.fruits).lower()

print(f"Selected fruit : {chosen_fruit.lower()}")

game_over = False
correct_selected_words = []
used_lives = 0

while not game_over:
    chosen_word = input('Select a letter : ').lower()
    print(f"You choose : {chosen_word}")

    display_word = ''
    correct_chose = 0
    for char in chosen_fruit :
        if char == chosen_word :
            correct_chose = 1
            display_word += char
            correct_selected_words.append(char)
        elif char in correct_selected_words :
            display_word += char
        else :
            display_word += '_'
    if correct_chose == 0 :
        used_lives +=1

    print(display_word)
    print(hangmandata.hangman_stage[used_lives])

    if used_lives == 6 :
        game_over = True
        print(hangmandata.game_over_text)





