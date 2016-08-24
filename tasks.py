# create the list
# welcome message to user
# add to list
# delete from list
# show list
# help

import os

def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def welcome():
	clear_screen()
	print("***** Tasks *****\n")
	


tasks = []

welcome()