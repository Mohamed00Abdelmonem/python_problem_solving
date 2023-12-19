import random
logo='''
                                                                                   
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                          


'''

# random card 
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

# calclate score sum card and if in card 11 be card 1 
def calclate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and cards>21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# who lose and who winer  
def compare(user_score,computer_score):
  if user_score>21 and computer_score>21:
        return "You went over. You lose 😤"
   
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
# contants play game add card him user or computer anything this is function is a body project
def play_game():
    print(logo)

    user_card=[]
    computer_card=[]
    is_game_over=False

    for _ in range(2):
        user_card.append(deal_cards())    
        computer_card.append(deal_cards())
# while loop for countinuo game and loop ask user
    while not is_game_over:
        user_score=calclate_score(user_card)        
        computer_score=calclate_score(computer_card)  

        print(f"   Your cards: {user_card}, current score: {user_score}")
        print(f"   Computer's first card: {computer_card[0]}")

        if user_card==0 or  computer_card==0 or user_score>21:
          is_game_over=True

        else: 

            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal=='y':
                user_card.append(deal_cards())
            else:
                is_game_over=True
# uf user choese 'n' that computer playing game 
    while computer_score !=0 and computer_score<17:
        computer_card.append(deal_cards())
        computer_score=calclate_score(computer_card)

    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))
# while loop to ask Q try agin game or n 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()

    





            
        
