#!/usr/bin/env python3

'''
This file is run the main Secret Santa program.
'''
#################################################
######### Editor's Name & Date  #################
#################################################
# YYYY/MM/DD ---------------------------- NAME  #
#################################################
#
# 2022/10/24 - MANZALEZ.I.98@
#
#################################################
#IMPORTS
from random import choice, randint

#FUNCTIONS NEEDED
def init_santas_and_receivers(N):
	names_list = []
	names_dict = {}
	if (N < 3):
		print("Not enough friends for Secret Santa this year. Sorry")

	else:
		for i in range(N):
			if (i >= 0 and i < 3):
				fname = str(input(f"Please enter the first name of the {ux_dict[i]} Secret Santa ... "))
				lname = str(input(f"Please enter the last name of the {ux_dict[i]} Secret Santa ... "))
			else:
				fname = str(input(f"Please enter the first name of the {i+1}th Secret Santa ... "))
				lname = str(input(f"Please enter the last name of the {i+1}th Secret Santa ... "))
			
			full_name = fname +' '+ lname
			names_list.append(full_name) 
			names_dict[i+1] = full_name 
	return names_dict,names_list


#INITIALIZE DATA STRUCTURES USED
names_list = []

contact_dict = {}
santa_dict = {}
ux_dict = { ## come up with better name
	0 : '1st',
	1 : '2nd',
	2 : '3rd'
} 

#ADD N SANTAS TO NAMES_DICT
#N = int(input("How many persons will be included in this year's Secret Santa?\n"))
#names_list = init_santas_and_receivers(N)
#print(names_dict, '\n',names_list)
#SELECT SANTA AND RECEIVER 
# santa_dict = get_santa(N, names_dict, names_list)

# print(santa_dict)


def secret_santas(names):
	
	def random_rearrange(names):
		cycle_santas = []
		for i in range(len(names)):
			x = names[randint(0,len(names)-1)]
			cycle_santas.append(x)
			names.remove(x)
		return cycle_santas

	def cycle(santas, start, end, matches):
		if start + 1 > end:
			matches[santas[end]] = santas[0]
			return matches
		else:
			santa = santas[start]
			receiver = santas[start + 1]
			matches[santa] = receiver
			start += 1
			cycle(santas, start, end, matches)


	matches = {}
	santas = random_rearrange(names)
	print(santas)

	cycle(santas, 0, len(santas)-1, matches)	
	print(matches)

	return matches


names = ['A', 'B', 'C', 'D', 'E', 'F']

secret_santas(names)


#################################################

