import time
import colorama 
colorama.init(autoreset=True)
time = time.strftime("%H:%M")

timing = {
		  "7:00" : "Jaffar Express",
		  "9:00" : "Thal Express",
		  "12:00": "Thar RailWay",
		  "16:00" : "Kohistan Xpress"
		  }
if time in timing:
	print(f"Next Train at {time} is {timing[time]}")
else:
	print("No Train Is Available At current time. Please Wait for The Next Train. To Get Timings of Trains, Enter 't'")
	a = input()
	if a == 't':
		for time,train in timing.items():
			c = (f"{time} »»» {train}").center(60)
			d = (colorama.Fore.YELLOW + c)
			print(d)


