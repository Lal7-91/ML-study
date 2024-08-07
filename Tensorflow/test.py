
counter = [0]

my_history = []  # Move the initialization outside the loop
for i in range(10):
    
    choices = ["P", "S", "S", "R", "P", "P", "R", "R", "S"]
    choice =  choices[counter[0] % len(choices)]
                
    my_history.append(choice)
    
    counter[0] += 1


print(my_history)

# countrt = [1, 10, 100]

# x = countrt[0]   # 1

# print(x)