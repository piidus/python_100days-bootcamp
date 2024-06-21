import random
from game_data import data
from art import logo, vs


FINAL_SCORE = 0
game_is = True
def data_number():
    return random.randint(1,50)
# game_is = False

QUESTION = data_number()
# ANSWER = data_number()

def check_answer(ques, ans, score):
    # print(ques,ans)
    if ques>ans and score==1:
        global FINAL_SCORE
        FINAL_SCORE+=1
        print(f"You are Right. Score : {FINAL_SCORE}") 
        return True
    elif ques<ans and score==2:
        FINAL_SCORE+=1
        print(f"You are Right. Score : {FINAL_SCORE}")
        return True
    else :
        FINAL_SCORE-=1
        print(f"You are Wrong. Score : {FINAL_SCORE}")
        False
while game_is :
   
    inp = input("Do you want to Play(type y or n) :").lower()
    if  inp == "y" :
        pass
    elif inp == "n":
        game_is = False
    

    
    print(logo)
    # global QUESTION
    # QUESTION = data_number()
    print(f'Who is highest follower\n{data[QUESTION]["name"]}')
    # print(f'{data[QUESTION]["follower_count"]}')
    print(vs)
    ANSWER = data_number()
    print(f'{data[ANSWER]["name"]}')
    # print(\n{data[ANSWER]["follower_count"]})
    choosen_option = int(input(f"Choose 1 or 2  :  " ))
    if choosen_option == 1 or choosen_option == 2:
        # print(choosen_option)
    
        final_answer = check_answer(data[QUESTION]["follower_count"], data[ANSWER]["follower_count"],choosen_option)
        # print(final_answer)
        if final_answer == True and choosen_option == 2:
            QUESTION = ANSWER
            # global game_is
            # game_is = True
            # print(QUESTION)
               
    
        
    
# gs_game()
    


    # game_mode()
    # gs_game()