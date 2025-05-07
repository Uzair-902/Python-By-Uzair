#START
#IMPORTING COLORAMA TO COLOR STRINGS
###PLEASE INSTALL COLORAMA BY USING 'pip install colorama' BEFORE RUNNING THE PROGRAM###
from colorama import init, Fore, Back, Style
init(autoreset=True)
head = (Fore.YELLOW +  '================ \nCONVERSIONS LIST\n================ ')
convs = '''
Km ➜ Miles   [km]
Miles ➜ Km   [mk]
°C  ➜ ° F    [cf]
°F  ➜ °C     [fc]
Kg  ➜ P      [kp]
P   ➜ Kg     [pk]
L   ➜ Gallons [lg]
Gallons ➜ L  [gl]

'''

#DEFINING FUNCTIONS

def km(km):
	return f"\n{km} Km = {km*0.621371:.2f} Miles\n"

def mk(M):
	return f"\n{M} Miles = {M/0.621371:.2f} Kilometers\n"

def cf(c):
	return f"\n{c} °C = {(c*1.8)+32:.2f} °F\n"

def fc(f):
	return f"\n{f} °F ={(f-32)*0.555555556:.2f} °C\n"

def kp(kg):
	return f"\n{kg} Kg = {kg*0.621371:.2f} Pounds\n"

def pk(p):
	return f"\n{p} Pounds = {p/0.621371:.2f} Kg\n"

def lg(l):
	return f"\n{l} Liters = {l*0.264172:.2f} Gallons\n"

def gl(g):
	return f"\n{g} Gallons = {g/0.264172:.2f} Liters\n"
#MAIN
def main():
#CONDITIONAL STATEMENTS 
	print(head)
	print(convs)
	inp = input()
	if inp.lower() == 'km':
		M = float(input(Fore.CYAN + '\nEnter KM:'))
		print(km(M))
	elif inp.lower() == 'mk':
		k = float(input(Fore.CYAN+'\nEnter Miles:'))
		print(mk(k))
	elif inp.lower() == 'cf':
		c = float(input(Fore.CYAN+'\nEnter °C:'))
		print(cf(c))
	elif inp.lower() == 'fc':
		f = float(input(Fore.CYAN+'\nEnter °F:'))
		print(fc(f))
	elif inp.lower() == 'kp':
		kg = float(input(Fore.CYAN+'\nEnter Kilograms:'))
		print(kp(kg))
	elif inp.lower() == 'pk':
		p = float(input(Fore.CYAN+'\nEnter Pounds:'))
		print(pk(p))
	elif inp.lower() == 'lg':
		l = float(input(Fore.CYAN+'\nEnter Liters:'))
		print(lg(l))
	elif inp.lower() == 'gl':
		g = float(input(Fore.CYAN+'\nEnter Gallons:'))
		print(gl(g))
	else:
		print(Fore.LIGHTRED_EX + '\nPlease Enter Valid Prompt. Only Prompts listed above are supported.\n')
#MAIN PROCESS LOOP AND ERROR HANDLING
try:
	while True:
		main()
except Exception as e:
		print(f'\nAn Unknown Error({e}) Occured. Make Sure you have Entered Everything In Correct Format.\n')