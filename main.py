def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def make_line():
    print("-"*40)


def print_menu(L):
    print("PASTA MENU")
    make_line()
    i = 0
    for item in L:
        output = "{} : {:<31} ${}".format(i + 1, item[0], item[1])
        print(output)
        i += 1
    make_line()


def main():
    pasta_menu = [
        ["Linguine Gamberi", 23],
        ["Fusilli Pesto", 19],
        ["Conchilglie alla Bolognese", 22],
        ["Rigatoni alla Caponata", 21],
        ["Fettuccine Carbonara", 20],
        ["Spaghetti Pomodoro", 16],
        ["Pappardelle Ricci D’Angello", 26],
        ["Raviolo di Salsiccia", 22],
        ["Ravioli di Ricotta", 20]
    ]
    menu_list = [
        ["V", "View pasta menu"],
        ["Q", "Quit"]
    ]
    make_line()
    print("PASTARIA")
    make_line()
    run_program = True
    while run_program == True:
        for i in menu_list:
            output = "{} : {}".format(i[0], i[1])
            print(output)
        user_choice = get_string("Please select an option: ")
        make_line()
        if user_choice == "V":
            print_menu(pasta_menu)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry, please try again.")
    print("Thank you, the program has ended.")


if __name__ == "__main__":
    main()
