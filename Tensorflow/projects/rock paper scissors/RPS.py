#This bot is a combination of all the bots. It will play 35 games to know the player and then it will play the best stratigy to win the game.

import random

def player(prev_play, counter=[0], opponent_history=[], win=[0], bot=[0], char_sequence = []):
    opponent_history.append(prev_play)
    
    # The 35 test games
    if counter[0] < 34:
        
        win[0] = 0    

        if counter[0] >= 0 and counter[0] < 10: #mrugesh checker (10 games)
            
            if counter[0] == 0:
                print("\nmurgesh check")
            
            if counter[0] == 9: 
                j = 0
                theo_hist = ['', 'R', 'R', 'S', 'S', 'S', 'S', 'S', 'S']   # what must murgesh played 
                for oopPlayer in opponent_history[0:9]:
                    if oopPlayer == theo_hist[j]:
                        win[0]+= 1
                        
                    j+=1
                
                        
                if win[0] == 9:
                    bot[0] = 1
                    
                print("abbey check")

                    
                    
            counter[0]+= 1
            return "P"
        
        
            
        elif counter[0] >= 10 and counter[0] < 19: # abbey checker (9 games)            
            
            plays = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]
            
            
            if counter[0] == 18:
               
                j = 0
                theo_hist = ['S', 'S', 'S', 'P', 'R', 'S', 'S', 'S']  # what must abbey played
                   
                for oopPlayer in opponent_history[10:18]:
                    if oopPlayer == theo_hist[j]:
                        win[0]+= 1
                        
                    j += 1
                        
                if win[0] == 8:
                    bot[0] = 2
                    
                print("quincy check")

                    
            counter[0]+= 1
            return plays[counter[0]-11]
            
        
        
        elif counter[0] >= 19 and counter[0] < 25: #quincy checker (6 games)
                        
            plays = ["P", "P", "S", "S", "R"]
            
            if counter[0]== 19:
                counter[0] +=1
                return "R"
            
            
            if counter[0] == 24:
                j = 0
                theo_hist = ['S', 'R', 'R', 'P', 'P'] # what must quincy played
                   
                for oopPlayer in opponent_history[19:24]:
                    if oopPlayer == theo_hist[j]:
                        win[0]+= 1
                    j += 1
                        
                if win[0] == 5:
                    bot[0] = 3
                print("kirs check")

            counter[0]+= 1 
        
            return plays[(counter[0]-21)%5]
            
        
        
        elif counter[0] >= 25 and counter[0] < 34:  #kris checker   (9 games)        
            
            plays = ["P", "S", "R"]
            
            
            if counter[0] == 32:
                
                j = 0       
                theo_hist = ['R', 'P', 'R', 'P', 'S', 'R', 'P', 'S'] # what must kris played
                
                for oopPlayer in opponent_history[25:32]:
                    if j > 3:
                        j = j % 3
                    if oopPlayer == theo_hist[j]:
                        win[0]+= 1
                    j += 1
                        
                if win[0] == 6:
                    bot[0] = 4
                    
            counter[0]+= 1  
            return plays[(counter[0]-25) % 3]
                
            
    #Here it decides the stratigy to play         
    if counter[0] == 34:       
        
        if bot[0] == 1:
            print("Bingo I founded you Murgesh!")
            
        elif bot[0] == 2:
            print("Bingo I founded you Abbey!")
            
        elif bot[0] == 3:
            print("Bingo I founded you Quincy!")
            
        elif bot[0] == 4:
            print("Bingo I founded you kirs!")  
        else:
            print("WOW HUMAN YOU PALYED 35 GAMES TO SEE THIS MESSAGE :)")
            
            
            
    if counter[0] >= 34 and counter[0] < 999:

        if bot[0] == 1:             # Murgesh statigy: play in this sequence: P, S, S, R, P, P, R, R, S          
            choices = ["P", "S", "R", "P", "S", "R", "S", "R"]
            counter[0] += 1
            return choices[(counter[0]-35) % len(choices)]  
        
            
        elif bot[0] == 2:                  #abbey stratigy: it neeeds to makes abbey sequences equal, then play in equavekent sequence   
            if counter[0] >= 34 and counter[0] < 188:
                     #len is 138  
                if counter[0] == 34:
                    pair_frequencies = {
                        'PS': 8,  # all added +1
                        'PR': 12,
                        'RR': 11,
                        'RP': 8,
                        'RS': 10,
                        'SS': 10,
                        'SR': 6,
                        'SP': 12
                    }

                    for pair, count in pair_frequencies.items():
                        char_sequence.extend(list(pair) * count) 

                counter[0] += 1 
                return char_sequence[(counter[0] - 35) % len(char_sequence)]

                            
            else:
                if counter[0] == 188: 
                    print(opponent_history[188])
                choices = ["R", "P", "P", "R", "R", "S", "P", "S", "S"]       # All sequnses equals
                counter[0]+= 1                                                                                       

                return choices[(counter[0] - 188) % len(choices)] 
            
        elif bot[0] == 3:   #quincy statigy: just play oppestie
            counter[0] += 1
            choices = ["P", "P", "S", "S", "R"] 
            return choices[(counter[0]-35) % len(choices)]
            

            
        elif bot[0] == 4:    #kris statigy: near to murgesh but not same
            counter[0] += 1
            choices = ["R", "P", "S", "R", "P", "S", "R", "P"] 
            return choices[(counter[0]-35) % len(choices)]
        
        else:
            choices = ["S","R", "P"]
            counter[0] += 1
            return random.choice(choices)
            

    else:    # Every 1000 games it will reset the every thing so PLEASE play in 1000 factors <3          
        print(f"{counter[0] + 1} games done!\n")
        prev_play = ""
        counter[0] = 0
        bot[0] = 0
        opponent_history.clear()
        char_sequence.clear()
        
     
            
                
    