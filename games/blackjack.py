import random


user_score = -1
comp_score = -1
def deal_card() :
    card_stack = [11,2,3,4,5,6,7,8,9,10,10,10]
    return  random.choice(card_stack)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    if sum(cards) > 21  and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score) :
    if u_score == c_score :
        return "Draw"
    elif u_score == 0 :
        return "User Win"
    elif c_score == 0 :
        return "Computer Win"
    elif u_score > 21 :
        return 'Computer Win'
    elif c_score > 21 :
        return 'User Win'
    elif u_score > c_score :
        return 'User Win'
    else :
        return 'Computer Win'
def play_game() :
    user_card = []
    comp_card = []
    is_game_over = False
    for _ in range(2) :
        user_card.append(deal_card())
        comp_card.append(deal_card())


    while not is_game_over :
        user_score =  calculate_score(user_card)
        comp_score =  calculate_score(comp_card)
        print(f"User cards : {user_card}, current score : {user_score}")
        print(f"Computer's cards : {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21 :
            is_game_over = True
        else :
            user_want_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_want_deal == 'y':
                user_card.append(deal_card())
            else :
                is_game_over = True

    while comp_score != 0 and comp_score < 17 :
        comp_card.append(deal_card())
        comp_score = calculate_score(comp_card)


    print(f"Your final hand : {user_card}, final score : {user_score}")
    print(f"Computer final hand : {comp_card}, final score : {comp_score}")
    print(compare(user_score, comp_score))


while input('Do you want to play game y/n : ') == 'y' :
    play_game()




