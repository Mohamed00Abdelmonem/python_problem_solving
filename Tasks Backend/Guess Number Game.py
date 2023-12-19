#This  is a Guess Number Game !!
# Final project day 12


logo=""""

 $$$$$$\                                                $$\   $$\                         $$\                           
$$  __$$\                                               $$$\  $$ |                        $$ |                          
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\        $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\       $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |      $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______|\_______/ \_______/       \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
                                                                                                                        
                                                                                                                        
                                                                                                              
                                                                                                              """


import random

def random_num():
    ''' this is function random hey MOhamed '''
    random_guess=random.randint(1,100) 
    return random_guess
counst=random_num()    







def easy_level():
    ''' this is a bulid in fumction easy level in game''' 
    count=10
    for _ in range(10):
    
        count=count-1
        result_easy=int(input("Enter Your Guess Number: "))
        print(f"You have {count} more tries left.")

        if result_easy > counst:
            print ("too high")
        elif result_easy==counst:
            print (f"** You Win ** is right number guess {result_easy}")
            break
       
        elif result_easy < counst:
            print ("too low")
# easy_level()         

       

def hard_level(): 
    ''' this is a bulid in fumction hard level in game''' 

    
    count=5
    for _ in range(5):
    
        count-=1
        result_easy=int(input("Enter Your Guess Number: "))
        print(f"You have {count} more tries left.")
        if result_easy==counst:
            print(result_easy)
            print(f"** you win ** is right number guess {result_easy}")
            break
        elif result_easy > counst:
            print("too high")
        elif result_easy < counst:
            print("too low")



def game():
    """ this is a function body project"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("i'm thinking of a number between 1 to 100.")
    level_game=input("Do YOU Want game is 'easy' level or 'hard' level :  "  )
    
    print(f"The Correct Answer is {counst}")
    
    if level_game=="easy":
        easy_level()
    else:
        hard_level()
game()        




