def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m).upper()
    return user_input


def make_line():
    print("-" * 40)


def delete_pasta(C):
    for i in range(0, len(C)):
        sub_total = C[i][2] * C[i][1]
        output = "{} : {} x {} @ ${} = ${} ".format(i+1, C[i][1], C[i][0], C[i][2], sub_total)
        print(output)
    delete_pasta = get_integer("Please select the item number of the pasta you would like to remove: ")
    delete_pasta_quantity = get_integer("Please select the number of {} you would like to remove: ".format(C[(delete_pasta)-1][0]))
    confirm = get_string("You are removing {} {} from your order, Y/N: ".format(delete_pasta_quantity, C[(delete_pasta)-1][0]))
    if confirm == "Y":
        C[(delete_pasta)-1][1] = C[(delete_pasta)-1][delete_pasta_quantity] - delete_pasta_quantity
    else:
        print("Order has not been updated.")
        print("Returning to main menu...")
    make_line()
    for i in range(0, len(C)):
        sub_total = C[i][2] * C[i][1]
        output = "{} : {} x {} @ ${} = ${} ".format(i + 1, C[i][1], C[i][0], C[i][2], sub_total)
        print(output)


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

delete_pasta(customer_order)




