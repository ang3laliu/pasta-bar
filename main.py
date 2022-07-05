def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m).upper()
    return user_input


def make_line():
    print("-" * 40)


def print_menu(L):
    print("PASTA MENU")
    make_line()
    i = 0
    for item in L:
        output = "{} : {:<31} ${}".format(i + 1, item[0], item[1])
        print(output)
        i += 1
    make_line()


def add_pasta(L,C):
    add_pasta_type = get_integer("Please select the item number of the pasta you would like to order: ")
    add_pasta_quantity = get_integer("How many {} would you like to order? ".format(L[(add_pasta_type)-1][0]))
    confirm = get_string("You are adding {} {} to your order, Y/N: ".format(add_pasta_quantity, L[(add_pasta_type)-1][0]))
    if confirm == "Y":
        C.append([ L[(add_pasta_type)-1][0],add_pasta_quantity, L[(add_pasta_type)-1][1] ] )
        output = ("You have added {} {}.".format(add_pasta_quantity, L[(add_pasta_type)-1][0]))
        print(output)
    else:
        print("Order has not been updated.")
        print("Returning to main menu...")
    make_line()


def review_order(C):
    print("CUSTOMER ORDER")
    make_line()
    for i in range(0, len(C)):
        sub_total = C[i][2]*C[i][1]
        output = "{} x {} @ ${} = ${} ".format(C[i][1],C[i][0],C[i][2], sub_total)
        print(output)
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
        ["A", "Add pasta to order"],
        ["R", "Review customer order"],
        ["Q", "Quit"]
    ]
    customer_order= [['Fusilli Pesto', 1, 19],['Rigatoni alla Caponata', 2, 21]]
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
        elif user_choice == "A":
            add_pasta(pasta_menu, customer_order)
        elif user_choice == "R":
            review_order(customer_order)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry, please try again.")
    print("Thank you, the program has ended.")


if __name__ == "__main__":
    main()

