hangman_stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

fruits = [
    "Apple", "Banana", "Orange", "Mango", "Grapes",
    "Pineapple", "Strawberry", "Blueberry", "Peach", "Pear",
    "Watermelon", "Kiwi", "Papaya", "Plum", "Cherry",
    "Lemon", "Lime", "Coconut", "Avocado", "Pomegranate",
    "Dragonfruit", "Lychee", "Raspberry", "Blackberry", "Cantaloupe",
    "Tangerine", "Apricot", "Grapefruit", "Fig", "Passion Fruit",
    "Mulberry", "Nectarine"]

game_over_text = '''

  ,ad8888ba,                                                ,ad8888ba,                                      
 d8"'    `"8b                                              d8"'    `"8b                                     
d8'                                                       d8'        `8b                                    
88            ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba,    88          88 8b       d8  ,adPPYba, 8b,dPPYba,  
88      88888 ""     `Y8 88P'   "88"    "8a a8P_____88    88          88 `8b     d8' a8P_____88 88P'   "Y8  
Y8,        88 ,adPPPPP88 88      88      88 8PP"""""""    Y8,        ,8P  `8b   d8'  8PP""""""" 88          
 Y8a.    .a88 88,    ,88 88      88      88 "8b,   ,aa     Y8a.    .a8P    `8b,d8'   "8b,   ,aa 88          
  `"Y88888P"  `"8bbdP"Y8 88      88      88  `"Ybbd8"'      `"Y8888Y"'       "8"      `"Ybbd8"' 88       

        '''