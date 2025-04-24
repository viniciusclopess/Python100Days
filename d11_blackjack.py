import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def user():
    user_cards = []
    score_user = 0
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        score_user += user_cards[i]
    print(user_cards)
    print(score_user)
    
def computer():
    dealer_cards = []
    score_dealer = 0
    for i in range(0, 2):
        dealer_cards.append(random.choice(cards))
        score_dealer += dealer_cards[i]
    print(dealer_cards)
    print(score_dealer)


user()
computer()