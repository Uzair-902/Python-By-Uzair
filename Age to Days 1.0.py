import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)
print(Fore.YELLOW + Back.LIGHTRED_EX + 'Age to Days 1.0'.center(50))

def ageday(age, months):
	days1 = age*365
	days2 = months*30
	days = days1+days2
	days = str(Fore.YELLOW + f'{days}')
	if age < 0 or age > 105:
		print(Fore.LIGHTRED_EX + '\nPlease Enter a Valid Age!\n')
	else:
		print(Fore.GREEN + Style.BRIGHT + f'\nYOU HAVE LIVED ~{days}' + Fore.GREEN +  ' DAYS OF YOUR LIFE!\n')

while True:
	try:
		age = int(input('\nEnter Age in Years:\n'))
		months = int(input('Enter Months In Addition to years:\n'))
		ageday(age, months)
	except Exception as e :
		print(f'ERROR: ({e}) OCCURED. PLEASE ENTER A VALID VALUE.')