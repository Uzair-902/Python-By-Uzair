import colorama
from colorama import init, Fore, Back
init(autoreset=True)
print(Fore.YELLOW+Back.RED+'TaskManager1.0'.center(50))
def show_menu():
    print("\n1. Add Task")
    print(Fore.GREEN+"2. View Tasks")
    print(Fore.LIGHTRED_EX+"3. Delete Task")
    print(Fore.CYAN+"4. Exit")
    print(Fore.YELLOW+'5. Save Tasks')

tasks = [ ]


def add():
	task = input(Fore.CYAN+'Enter task Description:\n')
	tasks.append(task)
	print(f'Task "{task}" Added Successfully !\n')


def view():
	print('\n=========\nTASKS:')
	if len(tasks) == 0:
		print('\nNo Tasks.')
	else:
		for i, task in enumerate(tasks, start=1):
			print(f"{i}.{task}\n=========")



def delete():
	try:
		if len(tasks) == 0:
			print('\nNo Tasks.')
		for i, task in enumerate(tasks, start=1):
			print(f"{i}. {task}")
		index = int(input('\nEnter Task Number to Delete\n'))-1
		if 0 <= index < len(tasks):
			deleted = tasks.pop(index)
			print(f'\nTask "{deleted}" Deleted Successfully !')
		else:
			print('Invalid Task Number!')
	except ValueError:
		print('Please Enter a Valid Number.')

def save():
	if len(tasks) == 0:
		print('\nNo Tasks Available.')
	else:
		with open("/storage/emulated/0/Documents/tasks.txt", "w") as file:
		    for task in tasks:
		        file.write(task + "\n")
		    print('\nFile Saved to: /storage/emulated/0/Documents/tasks.txt')


def main():
	show_menu()
	global prompt
	prompt = int(input('\nEnter Operation Number to Perform:\n'))

	if prompt == 1:
		add()
	elif prompt == 2:
		view()
	elif prompt == 3:
		delete()
	elif prompt == 4:
		pass
	elif prompt == 5:
		save()
	else:
		print('Invalid Operation!')


while True:
	try:
		main()
		if prompt == 4:
			break

	except Exception as e:
			print(Fore.LIGHTRED_EX+'An Error Occured.\nAdvanced Info About Error:', e, '\n')

		