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
	print("\n##########\nTasks\n##########\n\nThank you for using Tasks, goodbye!\n")
	sys.exit()

# main menu
def menu():
	clear_screen()
	print("\n##########\nTasks\n##########\n")
	print("Type 'new' to create a new task list\nType 'quit' to exit\n\n** WARNING: you will lose all entered data if you exit\n")
	command = input("> ").lower()
	if command == 'quit':
		quit()
	elif command == 'new':
		clear_screen()
		list_name = input("\n----- Enter a list name -----\n\n>")
		new_task_list(list_name)
	else:
		menu()

# Show current list
def show_current_list(_list, list_name):
	clear_screen()
	num = 0
	print("\n\n--- Currently in {} ---\n\n".format(list_name))
	for i in _list:
		num += 1
		print("	{}: ".format(num) + i)
	command = input("\n\nType 'c' to continue adding or 'quit' to exit\n\n>")
	if command == 'c':
		return True
	elif command == 'quit':
		quit()


# create the list / enter items
def new_task_list(list_name):
	_list = []
	clear_screen()
	print("\nCommands:\n'show' - Show current list items\n'quit' - Exit app\n")
	print("\n----- {} -----\n".format(list_name))
	print("Enter items..")
	while True:
		task = input("> ")
		if task == 'show':
			show_current_list(_list, list_name)
		elif task == 'quit':
			quit()
		_list.append(task)
		if 'show' in _list:
			_list.remove('show')

menu()