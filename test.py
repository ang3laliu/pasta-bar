def get_integer(m):
    user_input = int(input(m))
    return user_input

def get_string(m):
    user_input = input(m)
    return user_input

def add_pasta(L):
    customer_order = []
    add_pasta_type = get_integer("Please select the item number of the pasta you would like to order: ")
    add_pasta_quantity = get_integer("How many {} would you like to order? ".format(L[(add_pasta_type)-1][0]))
    confirm = get_string("You are adding {} {} to your order, Y/N: ".format(add_pasta_quantity, L[(add_pasta_type)-1][0]))
    if confirm == "Y":
        customer_order.append([L[(add_pasta_type)-1][0],add_pasta_quantity])
        output = ("You have added {} {}.".format(add_pasta_quantity, L[(add_pasta_type)-1][0]))
        print(output)
        print(customer_order)
    else:
        print("Order has not been updated.")
        print("Returning to main menu...\n")

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
add_pasta(pasta_menu)




