while True:
 try:
  n = input("\nEnter 'q' to quit. Enter Number for table: \n")
  if n.lower() == "q":
    break
  i = 0
  n = int(n)
  while i < 10:
  	i = i+1
  	print(f"{n} × {i} = {n*i}")
 except Exception:
 	print("An Unexpected Error Occured.")