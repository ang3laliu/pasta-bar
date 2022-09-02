"""This allows the user to place an order with a pasta bar."""


def get_integer(m, min_, max_):
    """Get an integer input from the user.

    :param m: str
    :param min_: int
    :param max_: int
    :return: int
    """
    get_input = True
    while get_input is True:
        # validation - use try, except to process string inputs without a program crash
        try:
            user_input = int(input(m))
        except ValueError:
            print("You must enter a whole number.")
            continue
        if user_input < min_ or user_input > max_:
            print("Entry is out of range, please try again.")
        else:
            return user_input


def get_string(m, min_=1, max_=1):
    """Get a string input from the user.

    :param m: str
    :param min_: int
    :param max_: int
    :return: str
    """
    get_input = True
    while get_input is True:
        # simple validation, make all string entries upper-case
        user_input = input(m).upper()
        # checking if the length of the input is outside of set parameters
        if len(user_input) < min_ or len(user_input) > max_:
            print("Entry is too short or too long, please try again.")
        else:
            return user_input


def get_pd(m, min_=1, max_=1):
    """Get a string input, either 'P' or 'D', from the user.

    :param m: str
    :param min_: int
    :param max_: int
    :return: str
    """
    get_input = True
    while get_input is True:
        user_input = input(m).upper()
        # validation - only wants 'P' or 'D' for pick-up/delivery
        if user_input not in ["P", "D"]:
            print("You have not entered 'P' or 'D', please try again.")
        else:
            return user_input


def get_yn(m):
    """Get a string input, either 'Y' or 'N', from the user.

    :param m: str
    :return: str
    """
    get_input = True
    while get_input is True:
        user_input = input(m).upper()
        # validation - only wants 'Y' or 'N' for yes/no
        if user_input not in ["Y", "N"]:
            print("You have not entered 'Y' or 'N', please try again.")
        else:
            return user_input


def make_line():
    """Print a dashed line to seperate information on the screen.

    :return: None
    """
    print("-" * 45)
    return None


def view_menu(menu):
    """Print pasta menu.

    :param menu: list
    :return: None
    """
    print("PASTA MENU")
    make_line()
    i = 0
    for item in menu:
        # printed with corresponding numbers, used when adding pasta
        output = "{} : {:<31} ${}".format(i + 1, item[0], item[1])
        print(output)
        i += 1
    make_line()
    return None


def pasta_descriptions():
    """Print descriptions of each pasta.

    :return: None
    """
    descriptions = [["Linguine Gamberi", "Long, flat pasta: Tomato, garlic and chilli sauce, prawns anchovies, capers, olives, parmesan", 23],
                    ["Fusilli Pesto", "Short, spiral pasta: Kale and cashew pesto and cream sauce, olives, parmesan", 19],
                    ["Conchilglie alla Bolognese", "Small, shell pasta: Northern italian beef and pork sauce, parmesan", 22],
                    ["Rigatoni alla Caponata", "Short, tube pasta: Agrodolce tomato sauce, eggplant, ricotta salata, pine nut", 21],
                    ["Fettuccine Carbonara", "Long, flat pasta: Creamy egg and pepper sauce, bacon, parmesan", 20],
                    ["Spaghetti Pomodoro", "Long, thin pasta: Classic tomato and basil sauce, parmesan", 16],
                    ["Pappardelle Ricci D’Angello", "Short, frizzy pasta: Slow cooked lamb ragu, rosemary, olives, sweet garlic, parmesan", 26],
                    ["Raviolo di Salsiccia", "Filled pasta: Red wine vinegar and tomato sauce, sausage, green capsicum, three cheese (filled) parmesan", 22],
                    ["Ravioli di Ricotta", "Spinach and ricotta (filled) pasta: brown butter sauce, sage, hazelnuts, parmesan", 20]
                    ]
    i = 0
    for item in descriptions:
        output = "{} : {:<28} -> {} ${}".format(i+1, item[0], item[1], item[2])
        i += 1
        print(output)
    make_line()
    return None


def add_pasta(menu, c):
    """Add pasta to customer order.

    :param menu: list
    :param c: list
    :return: None
    """
    view_menu(menu)
    add_pasta_type = get_integer("Please select the item number of the pasta you would like to order: ", 1, 9)
    double_up = False
    # test if pasta is already there
    # if so add to a pasta already in the customer order list
    for i in range(len(c)):
        if menu[add_pasta_type-1][0] == c[i][0]:
            double_up = True
            if c[i][1] == 5:
                print("You currently have 5 {}.".format(c[i][0]))
                print("This is the maximum amount you can order.")
                print("Returning to main menu...")
                make_line()
            else:
                if c[i][1] < 5:
                    print("You currently have {} {}, you can order {} more.".format(c[i][1], c[i][0], 5 - c[i][1]))
                add_pasta_quantity = get_integer("How many {} would you like to order? Maximum of 5 dishes per pasta: ".format(menu[add_pasta_type - 1][0]), 1, 5 - c[i][1])
                confirm = get_yn("You are adding {} {} to your order, (Y/N): ".format(add_pasta_quantity, menu[add_pasta_type - 1][0]))
                if confirm == "Y":
                    c[i][1] += add_pasta_quantity
                    print("You have added {} {}.".format(add_pasta_quantity, menu[add_pasta_type - 1][0]))
                    print("You now have {} {}".format(c[i][1], menu[add_pasta_type - 1][0]))
                else:
                    print("Order has not been updated.")
                    print("Returning to main menu...")
                make_line()
    # adding a new pasta
    if double_up is False:
        # run regular order
        add_pasta_quantity = get_integer("How many {} would you like to order? Maximum of 5 dishes per pasta: ".format(menu[add_pasta_type - 1][0]), 1, 5)
        confirm = get_yn("You are adding {} {} to your order, (Y/N): ".format(add_pasta_quantity, menu[add_pasta_type - 1][0]))
        if confirm == "Y":
            # if customer confirms, the pasta is appended onto the order list
            c.append([menu[add_pasta_type - 1][0], add_pasta_quantity, menu[add_pasta_type - 1][1]])
            output = ("You have added {} {}.".format(add_pasta_quantity, menu[add_pasta_type - 1][0]))
            print(output)
        else:
            # if customer rejects...
            print("Order has not been updated.")
            print("Returning to main menu...")
        make_line()
    return None


def update_pasta(c):
    """Change quanitity of a pasta dish.

    :param c: list
    :return: None
    """
    # items in the order list are printed with corresponding numbers
    for i in range(0, len(c)):
        sub_total = c[i][2] * c[i][1]
        output = "{} : {} x {} @ ${} = ${} ".format(i+1, c[i][1], c[i][0], c[i][2], sub_total)
        print(output)
    # user chooses which pasta they would like to update view the corresponding number
    pasta_index = get_integer("Please select the item number of the pasta you would like update: ", 1, len(c))
    # user requests a new quantity for the pasta
    new_pasta_quantity = get_integer("Please select the new number of {} you would like: ".format(c[pasta_index-1][0]), 0, 5)
    # request confirmation from user
    confirm = get_yn("You will have {} {} in your order, Y/N: ".format(new_pasta_quantity, c[pasta_index-1][0]))
    if confirm == "Y":
        # if customer confirms, make the previous quantity equal to the new quantity
        c[pasta_index-1][1] = new_pasta_quantity
        # if the new quantity is 0...
        if new_pasta_quantity == 0:
            print("You now have 0 {} in your order.".format(c[pasta_index - 1][0]))
            # clear the list containing that pasta
            c[pasta_index-1].clear()
            # remove the empty nested list
            c = list(filter(None, c))
        else:
            print("You now have {} {} in your order.".format(new_pasta_quantity, c[pasta_index - 1][0]))
    else:
        print("Order has not been updated.")
        print("Returning to main menu...")
    make_line()
    # prints order to display changes
    review_order(c)
    return None


def review_order(c):
    """Print items in order list.

    :param c: list
    :return: None
    """
    print("CUSTOMER ORDER")
    make_line()
    grand_total = 0
    # if the list is empty, provide a statement...
    if len(c) == 0:
        print("Nothing to display, your order is empty.")
        print("Returning to main menu...")
        make_line()
    else:
        # print out the customer list, formatted with appropriate prices and a grand total
        for i in range(0, len(c)):
            sub_total = c[i][2]*c[i][1]
            grand_total += sub_total
            output = "{} x {} @ ${} = ${} ".format(c[i][1], c[i][0], c[i][2], sub_total)
            print(output)
    print("Total Price : ${}".format(grand_total))
    make_line()
    return None


def cancel_order(c, d):
    """Cancel an order and remove details.

    :param c: list
    :param d: list
    :return: None
    """
    # request confirmation from the user
    confirm = get_yn("You are cancelling your order, (Y/N): ")
    if confirm == "Y":
        print("Your order has been cancelled and any details have been removed.")
        print("Returning to main menu...")
        # provide statements and clear both the order list and details list
        make_line()
        c.clear()
        d.clear()
    else:
        # otherwise state no changes have been made
        print("Order has not been cancelled.")
        print("Returning to main menu...")
        make_line()
    return None


def delivery_option(d):
    """Get user to input personal details.

    :param d: list
    :return: None
    """
    # request customer name for the order, char limits between 1 and 30
    order_name = get_string("Please enter a name for your order: ", 1, 30)
    # request the customer's phone number, char limits between 8 and 13
    phone_number = get_string("Please enter your phone number: ", 8, 13)
    # append both values to the customer details list
    d.append(order_name)
    d.append(phone_number)
    # request pick-up or delivery option
    pd = get_pd("Pick up is free of charge, delivery is an extra $3 (P/D)?: ")
    if pd == "D":
        # if delivery, request address, char limits between 15 and 100
        address = get_string("Please enter your address (e.g. 12A Tadpole Lane Karori 6012): ", 15, 100)
        make_line()
        # append address to details list to store the value
        d.append(address)
        # display for user to view and check over
        print("NAME: {}\nPHONE: {}\nADDRESS: {}".format(d[0], d[1], d[2]))
        make_line()
    elif pd == "P":
        make_line()
        # display for user to view and check over
        print("NAME: {}\nPHONE: {}".format(d[0], d[1]))
        make_line()
    # request confirmation from the user
    confirm = get_yn("Confirm your details are correct (Y/N): ")
    make_line()
    if confirm == "Y":
        print("Thank you for confirming your details.")
        print("Returning to main menu...")
    else:
        d.clear()
        print("No details confirmed.")
        print("Returning to main menu...")
    make_line()
    return None


def finish_order(c, d, extras=3):
    """Finalise order and confirm completion.

    :param c: list
    :param d: list
    :param extras: int
    :return: None
    """
    # if either the order list or details list is empty, the user will be redirected to the main menu
    if len(c) == 0:
        print("Your order is empty, please add pasta before completing.")
        print("Returning to main menu...")
        make_line()
    if len(d) == 0:
        print("Please enter your details before continuing.")
        print("Returning to main menu...")
        make_line()
    else:
        # use lengths to test for pickup(2) or delivery(3), formatting is dependent on this
        if len(d) == 2:
            # print customer order for user to check over
            review_order(c)
        elif len(d) == 3:
            grand_total = 0
            # also printing customer order for user to check over
            # review_order() is not used here due to the extra $3 delivery charge
            for i in range(0, len(c)):
                sub_total = c[i][2] * c[i][1]
                grand_total += sub_total
                output = "{} x {} @ ${} = ${} ".format(c[i][1], c[i][0], c[i][2], sub_total)
                print(output)
            print("Total Price : ${} + $3 = ${}".format(grand_total, grand_total+extras))
            make_line()
        # again, use lengths to test for pickup(2) or delivery(3), for the user to check over their personal details
        if len(d) == 2:
            print("NAME: {}\nPHONE: {}".format(d[0], d[1]))
            make_line()
        elif len(d) == 3:
            print("NAME: {}\nPHONE: {}\nADDRESS: {}".format(d[0], d[1], d[2]))
            make_line()
        # request confirmation
        confirm = get_yn("Please confirm your order and details are correct, (Y/N): ")
        if confirm == "Y":
            print("Thank you for ordering with us, your food will be ready soon.")
            make_line()
            # clear both the order list and details list upon confirmation
            c.clear()
            d.clear()
        else:
            print("Order is not finalised.")
            print("Returning to main menu...")
            make_line()
    return None


def main():
    """Get user to place an order for pasta.

    :return: None
    """
    # list containing pasta names and prices
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
    # list containing user options
    menu_list = [
        ["V", "View pasta menu"],
        ["P", "Pasta descriptions"],
        ["A", "Add pasta to order"],
        ["U", "Update pasta quantity"],
        ["R", "Review customer order"],
        ["C", "Cancel order"],
        ["G", "Get customer details"],
        ["F", "Finish order"],
        ["Q", "Quit"]
    ]
    # declare order and details lists
    customer_order = []
    details = []
    make_line()
    print("PASTARIA")
    make_line()
    run_program = True
    while run_program is True:
        for i in menu_list:
            output = "{} : {}".format(i[0], i[1])
            print(output)
        user_choice = get_string("Please select an option: ")
        make_line()
        # several if statements for user options
        if user_choice == "V":
            view_menu(pasta_menu)
        elif user_choice == "P":
            pasta_descriptions()
        elif user_choice == "A":
            add_pasta(pasta_menu, customer_order)
        elif user_choice == "U":
            update_pasta(customer_order)
        elif user_choice == "R":
            review_order(customer_order)
        elif user_choice == "C":
            cancel_order(customer_order, details)
        elif user_choice == "G":
            delivery_option(details)
        elif user_choice == "F":
            finish_order(customer_order, details)
        elif user_choice == "Q":
            run_program = False
        else:
            # simple validation, when the user fails to select one of the options provided
            print("Please select one of the options provided.")
            make_line()
    print("Thank you, the program has ended.")
    return None


if __name__ == "__main__":
    main()
