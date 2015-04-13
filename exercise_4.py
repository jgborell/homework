
def choose():
    print " Menu \n What would you like to do? \n 1. Write input to file \n 2. Write input to screen \n 3. Quit"
    choice = raw_input("Which do you choose?: ")
    if choice == "1":
        with open('text.txt', 'a+') as f: #another way to manipulate the I/O
            f.write(raw_input("Type text here: "))
        return choose()
    elif choice == "2":
        text = raw_input("Type text here: ")
        print text
        return choose()
    elif choice == "3":
        return choice
    else:
        print "Please choose 1, 2, or 3"
        return choose()
choose()

