from time import sleep
maths_menu = {
        1: 'Basic calc.',
        2: 'Blank2',
        3: 'exit'
}

class mathematics():
    #Maths  selection menu
    def show_maths_menu(self):
        from time import sleep
        print("Here's our selection.")
        for options in maths_menu.keys():
            print(options, '', maths_menu[options])
        sleep(1)
        calc1.maths_space()

    #Select method
    def maths_space(self):
        while True:
            select = int(input("Pick a category\n"))
            if select == 1:
                import sys
                class error(): #Fuck!!!!! I forgot why this is here
                    def exception(self):
                        print("I dont accept strings mfer! ", end="Whatever tho, i'm ")
                        print("closing session. Hold")
                        from time import sleep
                        sleep(1.5)
                        for i in range(3):
                            for j in range(i + 1):
                                print('.', end=""), sleep(0.5)
                            print(end=" ")
                        print("\nClosed successfully")

                error = error()

                calc_menu = {
                    1: '+ Addition',
                    2: '- Subtraction',
                    3: '* Multiplication',
                    4: '/ division',
                    5: 'expressions?'
                }

                def calc():
                    from time import sleep
                    try:
                        n_1 = int(input('1st number?'))
                        n_2 = int(input('2nd number?'))
                    except:
                        print("Puhlease, yu kno waht yu did wrong!")
                        wr_input = input("Do yu wish to continue or exit?\n")
                        if wr_input[0].lower() == 'c':
                            try:  # Using try as a go-to function
                                n_1 = int(input('1st number?'))
                                n_2 = int(input('2nd number?'))
                            except:
                                print("You're unserious mtcheww")
                                error.exception(), sleep(1)
                                sys.exit("Closed successfully")

                        elif wr_input[0].lower() == 'e':
                            print("Well buh byee")
                            sys.exit()

                    from time import sleep
                    print("Here's our list of operations.")
                    for options in calc_menu.keys():
                        print(options, '', calc_menu[options])
                    sleep(1)
                    try:
                        while True:
                            select = int(input("What's your choice\n"))
                            sleep(.5)
                            # Addition
                            if select == 1:
                                print('{} + {} = '.format(n_1, n_2), end="")
                                print(n_1 + n_2)

                            elif select == 2:
                                print('{} - {} = '.format(n_1, n_2), end="")
                                print(n_1 - n_2)

                            elif select == 3:
                                print('{} * {} = '.format(n_1, n_2), end="")
                                print(n_1 * n_2)

                            elif select == 4:
                                print('{} / {} = '.format(n_1, n_2), end="")
                                print(n_1 / n_2)

                            elif select == 5:
                                def expressions():
                                    rarr = eval(input("Enter expression\n"))
                                    print(rarr)

                                expressions()
                            else:
                                # Handles inputs out of range with options given in menu
                                def wrong_input():
                                    print("Unrecognized input"), sleep(0.3)
                                    wr_input = input("Do yu wish to continue or exit?\n")
                                    if wr_input[0].lower() == 'c' or not wr_input[0] != int:
                                        print("Then", end=" ")
                                    elif wr_input[0].lower() == 'e' or not wr_input[0] != int:
                                        # closing function runs if a user wishes to exit
                                        def closing_method():
                                            print("Closing session. Do hold on")
                                            sleep(1.5)
                                            for i in range(3):
                                                for j in range(i + 1):
                                                    print('.', end=""), sleep(0.5)
                                                print(end=" ")
                                            print("\nClosed successfully")

                                        closing_method()
                                    else:
                                        print("You picked the wrong thing again. Bye!")

                                wrong_input()  # Done/Works

                            def rerun():
                                calc_again = input("Wanna try again?\n")
                                if calc_again.lower() == 'y':
                                    dict(calc_menu)
                                    calc()
                                if calc_again.lower() == 'n':
                                    def closing_method():
                                        print("Closing session. Do hold on")
                                        sleep(1.5)
                                        for i in range(3):
                                            for j in range(i + 1):
                                                print('.', end=""), sleep(0.5)
                                            print(end=" ")
                                        print("\nClosed successfully")

                                    closing_method()
                                    #sys.exit()
                                    from In_the_beningining_lol import main_menu
                                    main_menu()


                            rerun()

                    except Exception as e:
                        error.exception()
                        sys.exit()
                calc()

            elif select == 2:
                print("lol got an absolute mental block here. return")

                def rerun():
                    calc_again = input("Wanna try again?\n")
                    if calc_again.lower() == 'y':
                        dict(calc_menu)
                        calc()
                    if calc_again.lower() == 'n':
                        def closing_method():
                            print("Closing session. Do hold on")
                            sleep(1.5)
                            for i in range(3):
                                for j in range(i + 1):
                                    print('.', end=""), sleep(0.5)
                                print(end=" ")
                            print("\nClosed successfully")

                        closing_method()
                        # sys.exit()
                        from In_the_beningining_lol import main_menu
                        main_menu()

                rerun()

            elif select == 3:
                print("Buh bye..."), sleep(1)
                from In_the_beningining_lol import main_menu
                main_menu()

            else:
                print("Wrong input, thats it we done here"), sleep(.5)
                for i in range(3):
                    for j in range(i + 1):
                        print('.', end=""), sleep(0.5)
                    print(end=" ")
                print("\nClosed 'mathematicals' successfully "), sleep(0.5)
                from In_the_beningining_lol import main_menu
                main_menu()

calc1 = mathematics()
calc1.show_maths_menu()
