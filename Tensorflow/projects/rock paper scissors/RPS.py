# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.


# def player(prev_play, opponent_history=[]): # stratigy 1, init guss = P and 4 got 2/4
#     opponent_history.append(prev_play)

#     guess = "P"
#     if len(opponent_history) > 4:   
#         guess = opponent_history[-4]
#     return guess


# def player(prev_play, counter=[0]): 

#     counter[0] += 1
#     choices = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]  #["P", "S", "S", "R", "P", "P", "R", "R", "S"]  got 100% against abbey
#     return choices[counter[0] % len(choices)]


def player(prev_play, counter=[0], opponent_history=[], win=[0], bot=[0]): # stratigy3: try 40 games to know the player
    
    opponent_history.append(prev_play)
    
        
    if counter[0] < 35:
        
        print(counter[0])

        
        if counter[0] >= 0 and counter[0] < 10: #mrugesh checker
            
            win[0] = 0    
            
            if counter[0] == 9:         
                for i in opponent_history[0:9]:
                    if i == "S":
                        win[0]+= 1
                        
                if win[0] == 9:
                    # counter[0] = 40
                    bot[0] = 1
                    
            counter[0]+= 1
            
            return "P"
        
        
            
        elif counter[0] >= 10 and counter[0] < 19: # abbey checker
            
            win[0] = 0    
            
            
            plays = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]
            
            
            if counter[0] == 18:
               
                j = 0
                for i in opponent_history[10:18]:      
                    oppPlayer = i
                    
                    if plays[j]=="R" and oppPlayer=="S":
                        win[0]+= 1
                        
                    elif plays[j]=="P" and oppPlayer=="R":
                        win[0]+= 1
                        
                    elif plays[j]=="S" and oppPlayer=="P":
                        win[0]+= 1
                    j += 1
                        
                if win[0] >= 5:
                    # counter[0] = 40
                    bot[0] = 2
                    
            counter[0]+= 1    
            return plays[counter[0]-8]
            
        
        
        elif counter[0] >= 19 and counter[0] < 25: #quincy checker
            win[0] = 0    
            
            plays = ["P", "P", "S", "S", "R"]
            
            
            if counter[0] == 24:
                
                j = 0
                for i in opponent_history[19:24]:      
                    oppPlayer = opponent_history[i]
                    
                    if plays[j]=="R" and oppPlayer=="S":
                        win[0]+= 1
                        
                    elif plays[j]=="P" and oppPlayer=="R":
                        win[0]+= 1
                        
                    elif plays[j]=="S" and oppPlayer=="P":
                        win[0]+= 1
                    j += 1
                        
                if win[0] == 5:
                    # counter[0] = 40
                    bot[0] = 3
            counter[0]+= 1    
            return plays[counter[0]-17]
            
        
        
        elif counter[0] >= 25 and counter[0] < 35:  #kris checker
            win[0] = 0    
            
            
            plays = ["P", "S", "R"]
            
            
            if counter[0] == 33:
                
                j = 0
                for i in opponent_history[25:33]:      
                    oppPlayer = opponent_history[i]
                    
                    if j > 2:
                        j = j % 3
                    
                    if plays[j]=="R" and oppPlayer=="S":
                        win[0]+= 1
                        
                    elif plays[j]=="P" and oppPlayer=="R":
                        win[0]+= 1
                        
                    elif plays[j]=="S" and oppPlayer=="P":
                        win[0]+= 1
                    j += 1
                        
                if win[0] == 8:
                    # counter[0] = 40
                    bot[0] = 4
            counter[0]+= 1   
            return plays[counter[0]-24]
                
            
            
    if counter[0] == 35:
        
        print(counter[0])

        
        if bot[0] == 1:
            print("Bingo I founded you Murgesh!")
            
        elif bot[0] == 2:
            print("Bingo I founded you Abbey!")
            
        elif bot[0] == 3:
            print("Bingo I founded you Quincy!")
            
        elif bot[0] == 4:
            print("Bingo I founded you kirs!")
            
        else:
            print("Sorry I am stupid and nothing worked ):")
            
    if counter[0] >= 35:
        
        return "P"
        if bot[0] == 1:
            pass
            
        elif bot[0] == 2:
            pass
            
        elif bot[0] == 3:
            pass
            
        elif bot[0] == 4:
            pass
            
                
        
            
            
        
    # else:
    #     opponent_history.append(prev_play)
    #     choices = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]
    #     choice =  choices[counter[0] % len(choices)]
        
    #     my_history.append(choice[counter[0]])
    # return winrazz
    