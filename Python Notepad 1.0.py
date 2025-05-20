from colorama import init, Back, Fore, Style

def save_file():
	with open(f'/storage/emulated/0/Documents/{name}.txt', 'w') as f:
		f.write(data)
		print('Saved')

init(autoreset=True)
print(Fore.YELLOW + Back.LIGHTRED_EX + Style.BRIGHT+ 'Python Notepad 1.0'.center(50))
name = input(Fore.CYAN+ 'Please Provide a Name for your File: ' + Fore.GREEN + Style.BRIGHT)
print(Fore.WHITE + "Write your notes (type '-exit' to save):")
data = ""
while True:
    line = input(Style.BRIGHT)
    if line.lower() == '-exit':
        break
    data += line + '\n'

save_file()

