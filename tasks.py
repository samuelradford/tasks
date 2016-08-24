# add to list
# delete from list
# show list
# help

import os
import sys

# clear screen function
def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

# quit app function
def quit():
	clear_screen()
	print("\n***** Tasks *****\n\nThank you for using Tasks, goodbye!\n\n")
	sys.exit()

# main menu
def menu():
	clear_screen()
	print("\n***** Tasks *****\n")
	print("Type 'new list' to create a new task list\nType 'quit' to exit (WARNING you will lose all entered data if you exit)\n")

	command = input("> ")
	if command == 'quit':
		quit()

# create the list


menu()