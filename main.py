def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m).upper()
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


def add_pasta(L,C):
    add_pasta_type = get_integer("Please select the item number of the pasta you would like to order: ")
    add_pasta_quantity = get_integer("How many {} would you like to order? ".format(L[(add_pasta_type)-1][0]))
    confirm = get_string("You are adding {} {} to your order, (Y/N): ".format(add_pasta_quantity, C[add_pasta_type-1][0]))
    if confirm == "Y":
        C.append([ L[(add_pasta_type)-1][0],add_pasta_quantity, L[(add_pasta_type)-1][1] ] )
        output = ("You have added {} {}.".format(add_pasta_quantity, L[(add_pasta_type)-1][0]))
        print(output)
    else:
        print("Order has not been updated.")
        print("Returning to main menu...")
    make_line()


def update_pasta(C):
    for i in range(0, len(C)):
        sub_total = C[i][2] * C[i][1]
        output = "{} : {} x {} @ ${} = ${} ".format(i+1, C[i][1], C[i][0], C[i][2], sub_total)
        print(output)
    pasta_index = get_integer("Please select the item number of the pasta you would like update: ")
    new_pasta_quantity = get_integer("Please select the new number of {} you would like: ".format(C[(pasta_index)-1][0]))
    confirm = get_string("You will have {} {} in order, Y/N: ".format(new_pasta_quantity, C[(pasta_index)-1][0]))
    if confirm == "Y":
        C[(pasta_index)-1][1] = new_pasta_quantity
    else:
        print("Order has not been updated.")
        print("Returning to main menu...")
    make_line()
    for i in range(0, len(C)):
        sub_total = C[i][2] * C[i][1]
        output = "{} : {} x {} @ ${} = ${} ".format(i + 1, C[i][1], C[i][0], C[i][2], sub_total)
        print(output)
    make_line()


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


def cancel_order(C,d):
    confirm = get_string("You are cancelling your order, (Y/N): ")
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
    order_name = get_string("Please enter a name for your order: ")
    d.append(order_name)
    phone_number = get_string("Please enter your phone number: ")
    d.append(phone_number)
    pd = get_string("Pick up is free of charge, delivery is an extra $3 (P/D)?: ")
    if pd == "D":
        address = get_string("Please enter your address (e.g. 12A Tadpole Lane Karori 6012): ")
        d.append(address)
        print("NAME: {}\nPHONE: {}\nADDRESS: {}".format(d[0], d[1], d[2]))
        make_line()
    elif pd == "P":
        print("NAME: {}\nPHONE: {}".format(d[0], d[1]))
        make_line()
    else:
        print("Unrecognised entry.")
        print("Returning to main menu...")
        print("how to jump to the end of the function")
    confirm = get_string("Confirm your details are correct (Y/N): ")
    make_line()
    if confirm == "Y":
        print("Thank you for confirming your details.")
        print("Returning to main menu...")
    else:
        d.clear()
        print("No details confirmed.")
        print("Returning to main menu...")
    make_line()


def finish_order(C,d):
    if len(C)==0:
        print("Your order is empty, please add pasta before completing.")
        print("Returning to main menu...")
        make_line()
    else:
        grand_total = 0
        for i in range(0, len(C)):
            sub_total = C[i][2] * C[i][1]
            grand_total += sub_total
            output = "{} x {} @ ${} = ${} ".format(C[i][1], C[i][0], C[i][2], sub_total)
            print(output)
        if len(d)==2:
            print("Total Price : ${}".format(grand_total))
        elif len(d)==3:
            print("Total Price : ${} + $3 = ${}".format(grand_total, grand_total+3))
        make_line()
    if len(d)==0:
        print("Please enter your details before continuing.")
        print("Returning to main menu...")
        make_line()
    else:
        if len(d)==2:
            print("NAME: {}\nPHONE: {}".format(d[0], d[1]))
            make_line()
        elif len(d)==3:
            print("NAME: {}\nPHONE: {}\nADDRESS: {}".format(d[0], d[1], d[2]))
            make_line()
    confirm = get_string("Please confirm your order and details are correct, (Y/N): ")
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
    customer_order= [['Fusilli Pesto', 1, 19],['Rigatoni alla Caponata', 2, 21],["Fettuccine Carbonara", 2, 20]]
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
            print("Unrecognised entry, please try again.")
    print("Thank you, the program has ended.")


if __name__ == "__main__":
    main()

