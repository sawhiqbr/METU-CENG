import math
import random
from evaluator import *    # get_data() will come from this import

universal_state = get_data()[6]
initial_data = get_data()

def new_move(): # calculates all the new moves and returns new universal state
	global initial_data
	global universal_state
	
	rows = initial_data[0]
	columns = initial_data[1]
	threshold = initial_data[2]
	contamination_constant = initial_data[3]
	mask_constant = initial_data[4]
	probability_constant = initial_data[5]
	
	ind_number = len(universal_state)

	occupied_positions = []
	for individiual in universal_state:
		occupied_positions += [list(individiual[0])]

	for individiual in universal_state: # calculates all individuals' new coordinates
		last_move = individiual[1]
		next_move = prob_move(last_move, probability_constant) # returns next move's direction as an integer
		
		individiual[1] = next_move

		current_pos = list(individiual[0])
		next_position = apply_move(next_move, current_pos) # returns next position of an individual as a list
		
		if (next_position[0] < 0) or (next_position[1] < 0) or (next_position[0] >= columns) or (next_position[1] >= rows) or (next_position in occupied_positions): # if an individual is not able to move, makes its status the same as before
			individiual[1] = last_move
			next_position = current_pos
		
		individiual[0] = tuple(next_position)
		
		index_of_ind = universal_state.index(individiual)
		
		occupied_positions[index_of_ind] = next_position

	universal_state = contamination(universal_state, ind_number, threshold, contamination_constant, mask_constant)

	return universal_state

def prob_move(last_move, mu): # determine the next move of an individiual
	#mu: move probability constant
	G = mu/2 #green
	Y = mu/8 #yellow
	B = (1 - mu - mu**2)/2 #blue
	P = (2*(mu**2))/5 #purple
	Gy= (mu**2)/5 #gray
	prob_list = [G, Y, B, P, Gy, P, B, Y]
	
	direction = random.choices(["F", "FR", "R", "BR", "B", "BL", "L", "FL"], prob_list, k = 1)
	
	directions = ["F", "FR", "R", "BR", "B", "BL", "L", "FL"]
	index_of_direction = directions.index(direction[0])

	next_move_direction = (index_of_direction+last_move)%8
	
	return next_move_direction

def apply_move(next_move, current_pos): # takes integer version of next_move and current position as arguments, calculates the next position; obeying specifications

	if next_move == 0:
		next_pos = [current_pos[0]] + [current_pos[1] + 1]
	if next_move == 2:
		next_pos = [current_pos[0] - 1] + [current_pos[1]]	
	if next_move == 4:
		next_pos = [current_pos[0]] + [current_pos[1] -1]
	if next_move == 6:
		next_pos = [current_pos[0] + 1] + [current_pos[1]]

	if next_move == 1:
		next_pos = [current_pos[0] - 1] + [current_pos[1] + 1]
	if next_move == 3:
		next_pos = [current_pos[0] - 1] + [current_pos[1] - 1]
	if next_move == 5:
		next_pos = [current_pos[0] + 1] + [current_pos[1] - 1]
	if next_move == 7:
		next_pos = [current_pos[0] + 1] + [current_pos[1] + 1]

	return next_pos

def contamination(current_uni_state, inds, thres_const, cont_const, mask_const): # applies rules of contamination
	# current_uni_state: current universal state
	# inds: number of individuals
	# thres_const: the threshold constant (D)
	# cont_const: the contamination constant (K)
	# mask_const: the constant used for masked individuals (lambda)
	infected_list = [] # holds the list of infected individuals

	for i in range(0, inds):                     # calculates if contamination occured between two individuals
		first_ind_mask = current_uni_state[i][2] # mask condition of first ind.
		first_ind_inf = current_uni_state[i][3]  # infection condition of first ind.
		for j in range(i+1, inds):
			second_ind_mask = current_uni_state[j][2] # mask condition of second ind.
			second_ind_inf = current_uni_state[j][3] # infection condition of second ind.

			distance = math.sqrt((current_uni_state[i][0][0] - current_uni_state[j][0][0])**2 + (current_uni_state[i][0][1] - current_uni_state[j][0][1])**2) 

			if distance > thres_const: # check if distance is more than threshold distance
				continue
			if first_ind_inf == second_ind_inf: # check if both individiuals' infection status are the same
				continue
			
			infect_prob = min(1, cont_const/(distance**2))

			if first_ind_mask == "masked" and second_ind_mask == "masked":
				infect_prob = infect_prob/(mask_const**2)
				
			if (first_ind_mask == "notmasked" and second_ind_mask == "masked") or (first_ind_mask == "masked" and second_ind_mask == "notmasked"):
				infect_prob = infect_prob/(mask_const)
				
			is_infectious = random.choices(["Infected", "Not infected"], [infect_prob, 1-infect_prob], k=1)

			if is_infectious[0] == "Infected":
				infected_list.append(i)
				infected_list.append(j)
				
	for x in infected_list: # to be able to apply contamination rules after all of the calculations
		current_uni_state[x][3] = "infected"

	return current_uni_state
