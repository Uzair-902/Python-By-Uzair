#START
contacts = {}

try:
 def sr(name):
 	if name in contacts:
 		print(f"\nName: {name} \nNumber: {contacts[name]}\n")
 	else:
 		print('\nNo Contact Found.\n')


 def vc():
     i = 1 
     if contacts:
         for name in contacts:
             print(f"\n{i}. {name}")
             i = i + 1 
     else:
         print('\nNo Contact Exists.\n')


 def ac(NewName, number):
 	contacts[NewName] = number
 
 def dc(name):
 	if name in contacts:
 		del contacts[name]
 		print(f'\nContact: {name} Deleted Successfully!\n')
 	else:
 		print(f"{name} Doesn't Exists.")
 
 while True:
  a = input('\nWelcome! What do you want to do? \n • Search a Contact (sr) \n • View all contacts (vc) \n • Add New contact (ac)\n • Delete a Contact (dc) \n \n')

  if a.lower() == 'sr':
  	name = input("\nEnter Name to Search a Contact.\n").lower()
  	sr(name)
  
  elif a.lower() == 'vc':
  	print('\nAll Contacts:')
  	vc()
  
  elif a.lower() == 'ac':
  	NewName = input("\nEnter New Contact Name:\n").lower()
  	Number = int(input("\nEnter Number for New Contact:\n"))
  	ac(NewName, Number)
  	print('\nContact Saved Successfully!')
  
  elif a.lower() == 'dc':
  	name = input("\nEnter Name to Delete a Contact.\n").lower()
  	dc(name)

  elif a.lower() == 'q':
  	print('\nProgrammed By Uzair_902. Thanks For Using. Also Support me at https://www.youtube.com/@FixDroid-Pro')
  	break
  
  else:
  	print('\nError, Make sure you have entered everything correct.\n')

except Exception as e:
	error_input = input('\nAn Unexpected Error Occured, Please make sure you have entered everything correct. For Advanced Info About the error, Enter "adv".')

	if error_input.lower() == 'adv':
		print(e)