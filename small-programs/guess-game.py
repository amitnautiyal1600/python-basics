question = "What goes up and down but can't move ? "
answer = "stair"
guess = ""
guess_count = 1
guess_limit = 3
out_of_guess = False

print("WELCOME!!")
print('Guess the answer to win. Toatal guess Count : ' + str(guess_limit) + "\n")

while guess != answer and not (out_of_guess):
    if guess_count <= guess_limit:
        guess = input(question + " ( Guess " + str(guess_count) + " ) : ")
        guess = guess.lower()
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print(' You Loose !! 👎🏻')
else:
    print("You Won !! 👍")
