import colorama
from colorama import init, Fore
colorama.init(autoreset=True)

def evenodd(n):
	if int(n) % 2 == 0:
		print(Fore.GREEN + f'\nThe Number {n} is an Even Number.\n')
	elif int(n) % 2 != 0:
		print(Fore.YELLOW + f'\nThe Number {n} is an Odd Number.\n')
	else:
		print(Fore.LIGHTRED_EX + '\nERROR: Please Enter a Valid Number.\n')
		
while True:
	try:
		n = input(Fore.CYAN + "Enter a Number to Check whether it's even or odd\nEnter 'e' to quit:\n")
		if n.lower()=='e':
			print(Fore.YELLOW + 'Exiting.....')
			print(Fore.LIGHTBLUE_EX + 'Good Bye!')
			break
		else:
			evenodd(n)
	except Exception as e:
		print(Fore.LIGHTRED_EX + f'An Unknown Error ({e}) occured. Please Enter a Valid Number.')