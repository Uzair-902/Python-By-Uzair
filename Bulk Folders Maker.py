#main infinite loop
while True:
    # Importing the os module
    import os

    #adding a try-except block for error handling.
    try:
        #getting path for operation
        path = input('Enter path for operation, "q" to exit. :')
        #exit logic
        if path.lower() == 'q':
            print('Programmed By Uzair_902. Thanks For Using. Also Support me at https://www.youtube.com/@FixDroid-Pro')
            break
        #getting prompt
        prompt = input('What do you want to do? Delete/Create?')

        #conditional statements
        if prompt.lower() == 'delete':
            os.rmdir(path)
            print('Folder deleted successfully!')
        elif prompt.lower() == 'create':
            os.chdir(path)

            #getting name for folders
            name = input('Enter Name for folders:')

            #getting quantity of folders
            qty = int(input('Enter qty:'))

            #main loop to create bulk folders
            for i in range(qty+1):
                os.mkdir(f"{name}, {i}")
            print('Done!')  # moved outside the loop
        else:
            print('Error, Please Input Valid Prompt!')

    #handling exceptions and errors
    except Exception as e:
        print(f"\nAn Unknown Error ({e}) occured. Please Make Sure The Input Is Correct and Try Again.\n")