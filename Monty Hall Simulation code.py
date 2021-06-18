import random # importing random module for random number generation

""" 
Taking input from the user for number of simulations.
Printing the game name in BOLD
"""
sim_num = int(input('\033[1m' + "M O N T Y   H A L L   P R O B L E M  -  S I M U L A T I O N" + '\033[0m'
                    "\n\nThe number of times you want to simulate: "))

# Taking input for the number of doors
ndoors = int(input("\nThe total number of doors you want to use: "))

#initializing variables
switch_win = 0    # Number of times user switched and won
not_switch_win = 0    # Number of times user didn't switch and won
n_times_switch = 0     #  Number of times user switched 
n_times_not_switch = 0    # Number of times user didn't switch

# Running for loop for simulating sim_num number of times
for k in range(1,sim_num+1):
    
    chosen_door = random.randint(1, ndoors) # chooses a random door between 1 and ndoors 
    car_door = random.randint(1, ndoors) # assigns a random door as car door between 1 and ndoors

# Choosing whether to switch door or not

    switch_num = random.randint(0, 1) 
    switch_door =  True if switch_num==1 else False

    if switch_door:
        
        n_times_switch = n_times_switch + 1  # Keeping track of the no. of times switched
        
        # Revealing the door except the chosen door and car door
        reveal_set = [dnum for dnum in range(1,ndoors+1) if dnum not in (chosen_door, car_door)]
        revealed_door = random.choice(reveal_set)
        
        # Keeping the available doors and switching to a door out of the available doors
        available_doors = [dnum2 for dnum2 in range(1,ndoors+1) if dnum2 not in (chosen_door, revealed_door)]
        chosen_door = random.choice(available_doors) 
        
        # keeping track of the number of times won by switching
        if chosen_door == car_door:
            switch_win = switch_win+1

    else:
        
        # keeping track of the number of times won by noy switching
        n_times_not_switch = n_times_not_switch + 1
        if chosen_door == car_door:
            not_switch_win = not_switch_win+1

print('\nMonty Hall Problem with {} doors'.format(ndoors))
print('\nProportion of wins with switching: {:.4f}'.format(switch_win/n_times_switch))
print('\nProportion of wins without switching: {:.4f}'.format(not_switch_win/n_times_not_switch))