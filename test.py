def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m).upper()
    return user_input


def make_line():
    print("-" * 40)


def review_order(C):
    print("CUSTOMER ORDER")
    make_line()
    grand_total = 0
    for i in range(0, len(C)):
        sub_total = C[i][2]*C[i][1]
        grand_total += sub_total
        output = "{} x {} @ ${} = ${} ".format(C[i][1],C[i][0],C[i][2], sub_total)
        print(output)
    print("Total Price : ${}".format(grand_total))
    make_line()


def delivery_option():
    order_name = get_string("Please enter a name for your order: ")
    phone_number = get_integer("Please enter your phone number: ")
    pd = get_string("Pick up or delivery (P/D)?: ")
    if pd == "D":
        address = get_string("Please enter your address: ")
        deliver_output = "NAME: {}\nPHONE: {}\nADDRESS: {}".format(order_name, phone_number, address)
        make_line()
        print(deliver_output)
    else:
        pickup_output = "NAME: {}\nPHONE: {}".format(order_name, phone_number)
        make_line()
        print(pickup_output)
    confirm = get_string("Confirm your details are correct (Y/N): ")
    if confirm == "Y":
        print("Thank you?????")
    else:
        print("No details confirmed, returning to main menu...")
    make_line()


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

customer_order= [['Fusilli Pesto', 3, 19],['Rigatoni alla Caponata', 1, 21]]

def main():
    menu_list = [
        ["V", "View pasta menu"],
        ["A", "Add pasta to order"],
        ["D", "Delete pasta from order"],
        ["R", "Review customer order"],
        ["G", "Get customer details"],
        ["C", "Complete order"],
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
        if user_choice == "G":
            delivery_option()
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry, please try again.")
    print("Thank you, the program has ended.")


if __name__ == "__main__":
    main()


