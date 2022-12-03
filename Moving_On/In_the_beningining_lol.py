#Reading particular a line of txt from MenuData.txt using islice
from itertools import islice
with open('Menu Data') as lines:
    for line in islice(lines,1):
        print(line, end="")

#loop to recieve Yes/No input
while True:
    qr = input('\nshall we begin?\n ') #qr stands for query jsky. \n supposed to receive input in nextline
    if qr == '' or not qr[0].lower() in ['y','n']: #Will not accept answers not starting with 'y' or 'n'
        print('HaHa Dont do that! Yes or No?')
    else:
        break #Break loop

#Dictionary of menu
menu = {
    1 : 'Mathematicals',
    2 : 'Banking',
    3 : 'About',
    4 : 'Exit'
}

class main_menu():#Class so this damn thing can be imported tfffff
    def show_menu(self): #Function to show menu
        for options in menu.keys():
            print(options,'', menu[options])
draw = main_menu

#Processing Yes/No statements
if qr[0].lower() == 'y':
    try:
        print("Here's the menu")
        draw.show_menu(main_menu)
        #Main menu block. Here menu features are given
        while True:
            select = int(input('Pick a vibe\n'))
            #Option 1
            if select == 1:
               from MathsModules import *
               calc1.show_maths_menu()

            #Option 2
            elif select == 2:
                #Basically OOPs concept mashup.  Tried to put in as many OOPs concepts as I could
                import OOPs_literally

            #Option 3
            elif select == 3: #About option
                #This shit suppose to print some files
                def about_option():
                    if True: #Unnecessary code but I dunno. works
                        from time import sleep
                        #print particular nth line
                        with open('Menu Data') as lines:
                            for line in islice(lines, 1, 5): #Using import islice; start:24 _ stop:25
                                print(line, end="")
                            sleep(2)
                        #Continue/Exit code after printing 'About'
                        wr_input_about_option = input("\nWe done? continue or exit?\n")  # weird section
                        if wr_input_about_option[0].lower() == 'c':
                            print("Ok, from menu", end=" ")
                        elif wr_input_about_option[0].lower() == 'e':
                            closing_gimmick()
                        else:
                            print("You picked the wrong thing. I'm out!")
                            Gimmick_obj.closing_method()
                    else:
                        pass

                about_option() #Done/Works

            #Option 4
            elif select == 4: #Exit option
                print("Aight, later then")
                break
            else:
                #Handles inputs out of range with options given in menu
                def wrong_input():
                    from time import sleep
                    print("wtf yu typing? Input is wrong"), sleep(0.5)
                    wr_input = input("Do yu wish to continue or exit?\n")
                    if wr_input[0].lower() == 'c':
                        print("Then", end=" ")
                    elif wr_input[0].lower() == 'e':
                        Gimmick_obj.closing_method()
                    else:
                        print("You picked the wrong thing again. Bye!")
                        Gimmick_obj.closing_method()
                wrong_input() #Done/Works
    except:
        pass

    finally:
        #closing_gimmick to mimic an exit module closing a module
        class closing_gimmick():
            def closing_method(self):
                print("Closing session. Do hold on")
                from time import sleep
                sleep(1.5)
                for i in range(3):
                    for j in range(i + 1):
                        print('.', end=""), sleep(0.5)
                    print(end=" ")
                print("\nClosed successfully")
        Gimmick_obj = closing_gimmick()
        Gimmick_obj.closing_method() #Done/works

if qr[0].lower() == 'n':
    print("Well fok off then") #End of code if it was never run
