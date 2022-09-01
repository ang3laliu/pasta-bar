def get_integer(m, min_, max_):
    get_input = True
    while get_input == True:
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
    get_input = True
    while get_input == True:
        user_input = input(m).upper()
        if len(user_input) < min_ or len(user_input) > max_:
            print("Entry is too short or too long, please try again.")
        else:
            return user_input


def get_pd(m, min_=1, max_=1):
    get_input = True
    while get_input == True:
        user_input = input(m).upper()
        if user_input not in ["P", "D"]:
            print("You have not entered 'P' or 'D', please try again.")
        else:
            return user_input


def get_yn(m):
    get_input = True
    while get_input == True:
        user_input = input(m).upper()
        if user_input not in ["Y", "N"]:
            print("You have not entered 'Y' or 'N', please try again.")
        else:
            return user_input


def make_line():
    print("-" * 40)


def view_menu(L):
    print("PASTA MENU")
    make_line()
    i = 0
    for item in L:
        output = "{} : {:<31} ${}".format(i + 1, item[0], item[1])
        print(output)
        i += 1
    make_line()


def pasta_descriptions():
    descriptions = [["Linguine Gamberi",
                     "Long, flat pasta: Tomato, garlic and chilli sauce, prawns anchovies, capers, olives, parmesan",
                     23],
                    ["Fusilli Pesto", "Short, spiral pasta: Kale and cashew pesto and cream sauce, olives, parmesan",
                     19],
                    ["Conchilglie alla Bolognese", "Small, shell pasta: Northern italian beef and pork sauce, parmesan",
                     22],
                    ["Rigatoni alla Caponata",
                     "Short, tube pasta: Agrodolce tomato sauce, eggplant, ricotta salata, pine nut", 21],
                    ["Fettuccine Carbonara", "Long, flat pasta: Creamy egg and pepper sauce, bacon, parmesan", 20],
                    ["Spaghetti Pomodoro", "Long, thin pasta: Classic tomato and basil sauce, parmesan", 16],
                    ["Pappardelle Ricci D’Angello",
                     "Short, frizzy pasta: Slow cooked lamb ragu, rosemary, olives, sweet garlic, parmesan", 26],
                    ["Raviolo di Salsiccia",
                     "Filled pasta: Red wine vinegar and tomato sauce, sausage, green capsicum, three cheese (filled) parmesan",
                     22],
                    ["Ravioli di Ricotta",
                     "Spinach and ricotta (filled) pasta: brown butter sauce, sage, hazelnuts, parmesan", 20]
                    ]
    i = 0
    for item in descriptions:
        output = "{} : {:<28} -> {} ${}".format(i + 1, item[0], item[1], item[2])
        i += 1
        print(output)
    make_line()



def add_pasta(L,C):
    view_menu(L)
    add_pasta_type = get_integer("Please select the item number of the pasta you would like to order: ", 1, 9)
    run_program = True
    while run_program == True:
        for i in range(len(C)):
            if L[(add_pasta_type) - 1][0] == C[i][0]:
                if C[i][1] == 5:
                    print("You currently have 5 {}.".format(C[i][0]))
                    print("This is the maximum amount you can order.")
                    print("Returning to main menu...")
                    make_line()
                    run_program = False
            else:
                rem = 0
                for i in range(len(C)):
                    if L[add_pasta_type- 1][0] in C[i][0]:
                        rem = 5 - C[i][1]
                        print("You already have {} {} in your order.".format(C[i][1], C[i][0]))
                        print("You may order {} more.".format(rem))
                    else:
                        continue


def update_pasta(C):
    for i in range(0, len(C)):
        sub_total = C[i][2] * C[i][1]
        output = "{} : {} x {} @ ${} = ${} ".format(i + 1, C[i][1], C[i][0], C[i][2], sub_total)
        print(output)
    pasta_index = get_integer("Please select the item number of the pasta you would like update: ", 1, len(C))
    if C[pasta_index - 1][1] == 5:
        print("You currently have 5 {}.".format(C[pasta_index - 1][0]))
        print("This is the maximum amount you can order.")
        print("Returning to main menu...")
        make_line()
    else:
        new_pasta_quantity = get_integer(
            "Please select the new number of {} you would like: ".format(C[(pasta_index) - 1][0]), 0, 5)
        confirm = get_yn("You will have {} {} in your order, Y/N: ".format(new_pasta_quantity, C[(pasta_index) - 1][0]))
        if confirm == "Y":
            C[(pasta_index) - 1][1] = new_pasta_quantity
            if new_pasta_quantity == 0:
                C[pasta_index - 1].clear()
                C = list(filter(None, C))
            print("You now have {} {} in your order.".format(new_pasta_quantity, C[pasta_index - 1][0]))
        else:
            print("Order has not been updated.")
            print("Returning to main menu...")
        make_line()
        review_order(C)


def review_order(C):
    print("CUSTOMER ORDER")
    make_line()
    grand_total = 0
    for i in range(0, len(C)):
        sub_total = C[i][2] * C[i][1]
        grand_total += sub_total
        output = "{} x {} @ ${} = ${} ".format(C[i][1], C[i][0], C[i][2], sub_total)
        print(output)
    print("Total Price : ${}".format(grand_total))
    make_line()


def cancel_order(C, d):
    confirm = get_yn("You are cancelling your order, (Y/N): ")
    if confirm == "Y":
        print("Your order has been cancelled and any details have been removed.")
        print("Returning to main menu...")
        make_line()
        C.clear()
        d.clear()
    elif confirm == "N":
        print("Order has not been cancelled.")
        print("Returning to main menu...")
        make_line()
    else:
        print("Unrecognised entry, no changes made.")
        print("Returning to main menu...")
        make_line()


def delivery_option(d):
    order_name = get_string("Please enter a name for your order: ", 1, 30)
    d.append(order_name)
    phone_number = get_string("Please enter your phone number: ", 8, 13)
    d.append(phone_number)
    pd = get_pd("Pick up is free of charge, delivery is an extra $3 (P/D)?: ")
    if pd == "D":
        address = get_string("Please enter your address (e.g. 12A Tadpole Lane Karori 6012): ", 15, 50)
        make_line()
        d.append(address)
        print("NAME: {}\nPHONE: {}\nADDRESS: {}".format(d[0], d[1], d[2]))
        make_line()
    elif pd == "P":
        make_line()
        print("NAME: {}\nPHONE: {}".format(d[0], d[1]))
        make_line()
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


def finish_order(C, d, extras=3):
    if len(C) == 0:
        print("Your order is empty, please add pasta before completing.")
        print("Returning to main menu...")
        make_line()
    else:
        # use lengths to test for pickup(2) or delivery(3)
        if len(d) == 2:
            review_order(C)
        elif len(d) == 3:
            grand_total = 0
            for i in range(0, len(C)):
                sub_total = C[i][2] * C[i][1]
                grand_total += sub_total
                output = "{} x {} @ ${} = ${} ".format(C[i][1], C[i][0], C[i][2], sub_total)
                print(output)
            print("Total Price : ${} + $3 = ${}".format(grand_total, grand_total + extras))
            make_line()

    if len(d) == 0:
        print("Please enter your details before continuing.")
        print("Returning to main menu...")
        make_line()
    else:
        if len(d) == 2:
            print("NAME: {}\nPHONE: {}".format(d[0], d[1]))
            make_line()
        elif len(d) == 3:
            print("NAME: {}\nPHONE: {}\nADDRESS: {}".format(d[0], d[1], d[2]))
            make_line()
        confirm = get_yn("Please confirm your order and details are correct, (Y/N): ")
        if confirm == "Y":
            print("Thank you for ordering with us, your food will be ready soon.")
            make_line()
            C.clear()
            d.clear()
        elif confirm == "N":
            print("Order is not finalised.")
            print("Returning to main menu...")
        else:
            print("Unrecognised entry.")
            print("Returning to main menu...")


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
        ["P", "Pasta descriptions"],
        ["A", "Add pasta to order"],
        ["U", "Update pasta quantity"],
        ["R", "Review customer order"],
        ["C", "Cancel order"],
        ["G", "Get customer details"],
        ["F", "Finish order"],
        ["Q", "Quit"]
    ]
    customer_order = [['Fusilli Pesto', 1, 19], ['Rigatoni alla Caponata', 2, 21], ["Fettuccine Carbonara", 5, 20]]
    details = []
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
            print("Select one of the options provided, please try again.")
            make_line()
    print("Thank you, the program has ended.")


if __name__ == "__main__":
    main()