# MODIFY get_data() AS YOU LIKE.
# DO NOT SEND THIS FILE TO US

import random
random.seed(111)  #remove hash-sign to get randomization seed we will be using at evaluation
#                    (if you fix the seed you get always the same probabilty choice sequence)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	       #[M, N,   D,   K, LAMBDA, MU,    universal_state]
	return [50, 100, 5,  80,  30,  0.55,  [[(34, 21), 4, 'notmasked', 'notinfected'] , [(27, 28), 2, 'notmasked', 'notinfected'] , [(40, 28), 6, 'notmasked', 'infected'] , [(34, 33), 2, 'masked', 'notinfected']]]


#2) [50, 100, 5,  80,  30,  0.55,  [[(34, 21), 4, 'notmasked', 'notinfected'] , [(27, 28), 2, 'notmasked', 'notinfected'] , [(40, 28), 6, 'notmasked', 'infected'] , [(34, 33), 2, 'masked', 'notinfected']]]

#First call of new_data() returns :[[(33, 22), 1, 'notmasked', 'notinfected'], [(26, 28), 2, 'notmasked', 'notinfected'], [(41, 27), 5, 'notmasked', 'infected'], [(35, 32), 5, 'masked', 'notinfected']]
#Second call of new_data() returns [[(32, 22), 2, 'notmasked', 'notinfected'], [(27, 27), 5, 'notmasked', 'notinfected'], [(42, 26), 5, 'notmasked', 'infected'], [(36, 31), 5, 'masked', 'notinfected']]
#Third call of new_data() returns :[[(32, 21), 4, 'notmasked', 'notinfected'], [(28, 26), 5, 'notmasked', 'notinfected'], [(41, 27), 1, 'notmasked', 'infected'], [(37, 32), 7, 'masked', 'notinfected']]
#Forth call of new_data() returns :[[(33, 20), 5, 'notmasked', 'notinfected'], [(29, 25), 5, 'notmasked', 'notinfected'], [(40, 28), 1, 'notmasked', 'infected'], [(37, 31), 4, 'masked', 'notinfected']]
#Fifth call of new_data() returns :[[(34, 20), 6, 'notmasked', 'notinfected'], [(28, 25), 2, 'notmasked', 'notinfected'], [(39, 29), 1, 'notmasked', 'infected'], [(36, 32), 1, 'masked', 'notinfected']]

#                                  [[(33, 22), 1, 'notmasked', 'notinfected'], [(26, 28), 2, 'notmasked', 'notinfected'], [(41, 27), 5, 'notmasked', 'infected'], [(35, 32), 5, 'masked', 'notinfected']]
#                                  [[(32, 22), 2, 'notmasked', 'notinfected'], [(27, 27), 5, 'notmasked', 'notinfected'], [(42, 26), 5, 'notmasked', 'infected'], [(36, 31), 5, 'masked', 'notinfected']]
#                                  [[(32, 21), 4, 'notmasked', 'notinfected'], [(28, 26), 5, 'notmasked', 'notinfected'], [(41, 27), 1, 'notmasked', 'infected'], [(37, 32), 7, 'masked', 'notinfected']]
#                                  [[(33, 20), 5, 'notmasked', 'notinfected'], [(29, 25), 5, 'notmasked', 'notinfected'], [(40, 28), 1, 'notmasked', 'infected'], [(37, 31), 4, 'masked', 'notinfected']]
#                                  [[(34, 20), 6, 'notmasked', 'notinfected'], [(28, 25), 2, 'notmasked', 'notinfected'], [(39, 29), 1, 'notmasked', 'infected'], [(36, 32), 1, 'masked', 'notinfected']]

#
#3) [100, 100, 5,  70,  30,  0.50,  [[(12, 18), 5, 'masked', 'infected'] , [(25, 30), 3, 'notmasked', 'infected'] , [(50, 40), 1, 'notmasked', 'notinfected'] , [(66, 10), 7, 'masked', 'notinfected']]]

#First call of new_data() returns : [[(11, 17), 3, 'masked', 'infected'], [(24, 29), 3, 'notmasked', 'infected'], [(50, 41), 0, 'notmasked', 'notinfected'], [(65, 11), 1, 'masked', 'notinfected']]
#Second call of new_data() return : [[(12, 16), 5, 'masked', 'infected'], [(25, 30), 7, 'notmasked', 'infected'], [(50, 42), 0, 'notmasked', 'notinfected'], [(64, 12), 1, 'masked', 'notinfected']]
#Third call of new_data() returns : [[(13, 17), 7, 'masked', 'infected'], [(26, 31), 7, 'notmasked', 'infected'], [(50, 41), 4, 'notmasked', 'notinfected'], [(63, 11), 3, 'masked', 'notinfected']]
#Forth call of new_data() returns : [[(12, 18), 1, 'masked', 'infected'], [(27, 32), 7, 'notmasked', 'infected'], [(50, 40), 4, 'notmasked', 'notinfected'], [(63, 12), 0, 'masked', 'notinfected']]
#Fifth call of new_data() returns : [[(13, 19), 7, 'masked', 'infected'], [(27, 33), 0, 'notmasked', 'infected'], [(49, 40), 2, 'notmasked', 'notinfected'], [(62, 13), 1, 'masked', 'notinfected']]

#                                   [[(11, 17), 3, 'masked', 'infected'], [(24, 29), 3, 'notmasked', 'infected'], [(50, 41), 0, 'notmasked', 'notinfected'], [(65, 11), 1, 'masked', 'notinfected']]
#                                   [[(12, 16), 5, 'masked', 'infected'], [(25, 30), 7, 'notmasked', 'infected'], [(50, 42), 0, 'notmasked', 'notinfected'], [(64, 12), 1, 'masked', 'notinfected']]
#                                   [[(13, 17), 7, 'masked', 'infected'], [(26, 31), 7, 'notmasked', 'infected'], [(50, 41), 4, 'notmasked', 'notinfected'], [(63, 11), 3, 'masked', 'notinfected']]
#                                   [[(12, 18), 1, 'masked', 'infected'], [(27, 32), 7, 'notmasked', 'infected'], [(50, 40), 4, 'notmasked', 'notinfected'], [(63, 12), 0, 'masked', 'notinfected']]
#                                   [[(13, 19), 7, 'masked', 'infected'], [(27, 33), 0, 'notmasked', 'infected'], [(49, 40), 2, 'notmasked', 'notinfected'], [(62, 13), 1, 'masked', 'notinfected']]

#            [50, 100, 5, 80, 30, 0.55, [[(22, 14), 0, 'notmasked', 'notinfected'], [(19, 15), 7, 'notmasked', 'notinfected'], [(17, 16), 7, 'notmasked', 'notinfected'], [(26, 20), 3, 'notmasked', 'infected'], [(22, 21), 5, 'masked', 'infected'], [(25, 21), 3, 'notmasked', 'infected']]]

#First call of new_move() returns :     [[(23, 13), 5, 'notmasked', 'notinfected'], [(20, 16), 7, 'notmasked', 'notinfected'], [(18, 16), 6, 'notmasked', 'notinfected'], [(27, 20), 6, 'notmasked', 'infected'], [(23, 21), 6, 'masked', 'infected'], [(26, 21), 6, 'notmasked', 'infected']]
#Second call of new_move() returns :    [[(24, 12), 5, 'notmasked', 'notinfected'], [(21, 17), 7, 'notmasked', 'notinfected'], [(18, 17), 0, 'notmasked', 'notinfected'], [(28, 20), 6, 'notmasked', 'infected'], [(22, 21), 2, 'masked', 'infected'], [(26, 22), 0, 'notmasked', 'infected']]
#Third call of new_move() returns :     [[(25, 11), 5, 'notmasked', 'notinfected'], [(22, 18), 7, 'notmasked', 'notinfected'], [(19, 16), 5, 'notmasked', 'notinfected'], [(28, 19), 4, 'notmasked', 'infected'], [(21, 20), 3, 'masked', 'infected'], [(27, 21), 5, 'notmasked', 'infected']]
#Forth call of new_move() returns :     [[(26, 10), 5, 'notmasked', 'notinfected'], [(21, 18), 2, 'notmasked', 'notinfected'], [(20, 17), 7, 'notmasked', 'notinfected'], [(27, 19), 2, 'notmasked', 'infected'], [(21, 21), 0, 'masked', 'infected'], [(28, 20), 5, 'notmasked', 'infected']]
#Fifth call of new_move() returns :     [[(27,  9), 5, 'notmasked', 'notinfected'], [(20, 18), 2, 'notmasked', 'notinfected'], [(21, 17), 6, 'notmasked', 'notinfected'], [(26, 20), 1, 'notmasked', 'infected'], [(21, 22), 0, 'masked', 'infected'], [(29, 19), 5, 'notmasked', 'infected']]
#Sixth call of new_move() returns :     [[(26,  8), 3, 'notmasked', 'notinfected'], [(21, 18), 6, 'notmasked',    'infected'], [(20, 16), 3, 'notmasked', 'notinfected'], [(25, 19), 3, 'notmasked', 'infected'], [(20, 21), 3, 'masked', 'infected'], [(28, 18), 3, 'notmasked', 'infected']]
#Seventh call of new_move() returns :   [[(25,  7), 3, 'notmasked', 'notinfected'], [(20, 17), 3, 'notmasked',    'infected'], [(19, 15), 3, 'notmasked',    'infected'], [(24, 19), 2, 'notmasked', 'infected'], [(20, 22), 0, 'masked', 'infected'], [(29, 17), 5, 'notmasked', 'infected']]
#Eighth call of new_move() returns :    [[(24,  7), 2, 'notmasked', 'notinfected'], [(20, 16), 4, 'notmasked',    'infected'], [(18, 14), 3, 'notmasked',    'infected'], [(25, 19), 6, 'notmasked', 'infected'], [(21, 22), 6, 'masked', 'infected'], [(30, 16), 5, 'notmasked', 'infected']]
#Ninth call of new_move() returns :     [[(25,  8), 7, 'notmasked', 'notinfected'], [(21, 15), 5, 'notmasked',    'infected'], [(19, 15), 7, 'notmasked',    'infected'], [(25, 20), 0, 'notmasked', 'infected'], [(22, 21), 5, 'masked', 'infected'], [(30, 17), 0, 'notmasked', 'infected']]
#Tenth call of new_move() returns :     [[(26,  8), 6, 'notmasked', 'notinfected'], [(21, 14), 4, 'notmasked',    'infected'], [(20, 16), 7, 'notmasked',    'infected'], [(26, 21), 7, 'notmasked', 'infected'], [(21, 21), 2, 'masked', 'infected'], [(30, 18), 0, 'notmasked', 'infected']]
#Eleventh call of new_move() returns :  [[(25,  9), 1, 'notmasked', 'notinfected'], [(21, 13), 4, 'notmasked',    'infected'], [(21, 17), 7, 'notmasked',    'infected'], [(27, 22), 7, 'notmasked', 'infected'], [(20, 20), 3, 'masked', 'infected'], [(31, 18), 6, 'notmasked', 'infected']]
#Twelfth call of new_move() returns :   [[(24, 10), 1, 'notmasked',    'infected'], [(22, 14), 7, 'notmasked',    'infected'], [(22, 16), 5, 'notmasked',    'infected'], [(27, 23), 0, 'notmasked', 'infected'], [(20, 21), 0, 'masked', 'infected'], [(30, 19), 1, 'notmasked', 'infected']]
#Thirteenth call of new_move() returns  [[(23,  9), 3, 'notmasked',    'infected'], [(23, 14), 6, 'notmasked',    'infected'], [(23, 17), 7, 'notmasked',    'infected'], [(27, 24), 0, 'notmasked', 'infected'], [(20, 22), 0, 'masked', 'infected'], [(29, 20), 1, 'notmasked', 'infected']]
#Fourteenth call of new_move() returns  [[(22,  8), 3, 'notmasked',    'infected'], [(24, 13), 5, 'notmasked',    'infected'], [(24, 18), 7, 'notmasked',    'infected'], [(28, 24), 6, 'notmasked', 'infected'], [(21, 21), 5, 'masked', 'infected'], [(28, 19), 3, 'notmasked', 'infected']]
#Fifteenth call of new_move() returns : [[(21,  7), 3, 'notmasked',    'infected'], [(25, 12), 5, 'notmasked',    'infected'], [(25, 18), 6, 'notmasked',    'infected'], [(28, 25), 0, 'notmasked', 'infected'], [(20, 21), 2, 'masked', 'infected'], [(27, 18), 3, 'notmasked', 'infected']]

#                                       [[(23, 13), 5, 'notmasked', 'notinfected'], [(20, 16), 7, 'notmasked', 'notinfected'], [(18, 16), 6, 'notmasked', 'notinfected'], [(27, 20), 6, 'notmasked', 'infected'], [(23, 21), 6, 'masked', 'infected'], [(26, 21), 6, 'notmasked', 'infected']]
#                                       [[(24, 12), 5, 'notmasked', 'notinfected'], [(21, 17), 7, 'notmasked', 'notinfected'], [(18, 17), 0, 'notmasked', 'notinfected'], [(28, 20), 6, 'notmasked', 'infected'], [(22, 21), 2, 'masked', 'infected'], [(26, 22), 0, 'notmasked', 'infected']]
#                                       [[(25, 11), 5, 'notmasked', 'notinfected'], [(22, 18), 7, 'notmasked', 'notinfected'], [(19, 16), 5, 'notmasked', 'notinfected'], [(28, 19), 4, 'notmasked', 'infected'], [(21, 20), 3, 'masked', 'infected'], [(27, 21), 5, 'notmasked', 'infected']]
#                                       [[(26, 10), 5, 'notmasked', 'notinfected'], [(21, 18), 2, 'notmasked', 'notinfected'], [(20, 17), 7, 'notmasked', 'notinfected'], [(27, 19), 2, 'notmasked', 'infected'], [(21, 21), 0, 'masked', 'infected'], [(28, 20), 5, 'notmasked', 'infected']]
#                                       [[(27,  9), 5, 'notmasked', 'notinfected'], [(20, 18), 2, 'notmasked', 'notinfected'], [(21, 17), 6, 'notmasked', 'notinfected'], [(26, 20), 1, 'notmasked', 'infected'], [(21, 22), 0, 'masked', 'infected'], [(29, 19), 5, 'notmasked', 'infected']]
#                                 	    [[(26,  8), 3, 'notmasked', 'notinfected'], [(21, 18), 6, 'notmasked',    'infected'], [(20, 16), 3, 'notmasked', 'notinfected'], [(25, 19), 3, 'notmasked', 'infected'], [(20, 21), 3, 'masked', 'infected'], [(28, 18), 3, 'notmasked', 'infected']]
#                                       [[(25,  7), 3, 'notmasked', 'notinfected'], [(20, 17), 3, 'notmasked',    'infected'], [(19, 15), 3, 'notmasked',    'infected'], [(24, 19), 2, 'notmasked', 'infected'], [(20, 22), 0, 'masked', 'infected'], [(29, 17), 5, 'notmasked', 'infected']]
#                                       [[(24,  7), 2, 'notmasked', 'notinfected'], [(20, 16), 4, 'notmasked',    'infected'], [(18, 14), 3, 'notmasked',    'infected'], [(25, 19), 6, 'notmasked', 'infected'], [(21, 22), 6, 'masked', 'infected'], [(30, 16), 5, 'notmasked', 'infected']]
#                                       [[(25,  8), 7, 'notmasked', 'notinfected'], [(21, 15), 5, 'notmasked',    'infected'], [(19, 15), 7, 'notmasked',    'infected'], [(25, 20), 0, 'notmasked', 'infected'], [(22, 21), 5, 'masked', 'infected'], [(30, 17), 0, 'notmasked', 'infected']]
#                                       [[(26,  8), 6, 'notmasked', 'notinfected'], [(21, 14), 4, 'notmasked',    'infected'], [(20, 16), 7, 'notmasked',    'infected'], [(26, 21), 7, 'notmasked', 'infected'], [(21, 21), 2, 'masked', 'infected'], [(30, 18), 0, 'notmasked', 'infected']]
#                                       [[(25,  9), 1, 'notmasked', 'notinfected'], [(21, 13), 4, 'notmasked',    'infected'], [(21, 17), 7, 'notmasked',    'infected'], [(27, 22), 7, 'notmasked', 'infected'], [(20, 20), 3, 'masked', 'infected'], [(31, 18), 6, 'notmasked', 'infected']]
#                                       [[(24, 10), 1, 'notmasked',    'infected'], [(22, 14), 7, 'notmasked',    'infected'], [(22, 16), 5, 'notmasked',    'infected'], [(27, 23), 0, 'notmasked', 'infected'], [(20, 21), 0, 'masked', 'infected'], [(30, 19), 1, 'notmasked', 'infected']]
#                                       [[(23,  9), 3, 'notmasked',    'infected'], [(23, 14), 6, 'notmasked',    'infected'], [(23, 17), 7, 'notmasked',    'infected'], [(27, 24), 0, 'notmasked', 'infected'], [(20, 22), 0, 'masked', 'infected'], [(29, 20), 1, 'notmasked', 'infected']]
#                                       [[(22,  8), 3, 'notmasked',    'infected'], [(24, 13), 5, 'notmasked',    'infected'], [(24, 18), 7, 'notmasked',    'infected'], [(28, 24), 6, 'notmasked', 'infected'], [(21, 21), 5, 'masked', 'infected'], [(28, 19), 3, 'notmasked', 'infected']]
#                                       [[(21,  7), 3, 'notmasked',    'infected'], [(25, 12), 5, 'notmasked',    'infected'], [(25, 18), 6, 'notmasked',    'infected'], [(28, 25), 0, 'notmasked', 'infected'], [(20, 21), 2, 'masked', 'infected'], [(27, 18), 3, 'notmasked', 'infected']]
