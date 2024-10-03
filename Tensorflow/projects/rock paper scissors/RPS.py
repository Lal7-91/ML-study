# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.


# def player(prev_play, opponent_history=[]): # stratigy 1, init guss = P and 4 got 2/4
#     opponent_history.append(prev_play)

#     guess = "P"
#     if len(opponent_history) > 4:   
#         guess = opponent_history[-4]
#     return guess


def player(prev_play, counter=[0]): # stratigy2, patern: ["P", "P", "R", "R", "S","R", "P", "P", "S", "R"] won murgesh and qunciy

    counter[0] += 1
    choices = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]  #["P", "S", "S", "R", "P", "P", "R", "R", "S"]  got 100% against abbey
    return choices[counter[0] % len(choices)]


# from RPS_game import play

# def player(prev_play, counter=[0], opponent_history=[], my_history=[]): # stratigy3: try 40 games to know the player 
    
#     counter[0] += 1
    
#     if counter[0] <= 40:
    
#         if counter[0] <= 10: # abbey checker
                        
#             # opponent_history.append(prev_play)
#             # choices = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]
#             # choice =  choices[counter[0] % len(choices)]
            
#             # my_history.append(choice[counter[0]])
            
#             opponent_history.append(prev_play)
#             choices = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]
#             choice =  choices[counter[0] % len(choices)]
#             my_history.append(choice) # problem is here
#             print(counter[0], choice)
#             return choice
        
#         elif counter[0] > 10 and counter[0] <= 20:  #kris checker
#             pass
            
            
#         elif counter[0] > 20 and counter[0] <= 30: #mrugesh checker
#             pass
        
#         elif counter[0] > 30 and counter[0] <= 40: #quincy checker
#             pass
            
#         print(my_history)
            
#     elif counter[0] == 40: #choose the best
        
#         pass
            
            
        
#     else:
#         opponent_history.append(prev_play)
#         choices = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]
#         choice =  choices[counter[0] % len(choices)]
        
#         my_history.append(choice[counter[0]])
#         return choice
    