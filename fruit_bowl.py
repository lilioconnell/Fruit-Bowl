def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(message):
    while True:
        try:
            my_integer = int(input(message))
            return my_integer
        except:
            print("Invalid entry")


def print_list(L):
    for i in range(0, len(L)):
        if len(L[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:3} : {:<3}".format(L[i][0], L[i][1])
        print(output)


def print_list_with_indexes(L):
    for i in range(0, len(L)):
        if len(L[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:3} : {:3} : {:<3}".format(i, L[i][0], L[i][1])
        print(output)


def add_fruit(L):
    print_list_with_indexes(L)
    my_index = get_integer("Choose index number to update the fruit quantity")
    number = get_integer("Enter how many you would like to add:")
    old_amount = L[my_index][1]
    new_amount = old_amount + number
    print("{} + {} = {}".format(old_amount, number, new_amount))
    output_message = "The number of {} {} has been updated to {}.".format(old_amount, L[my_index][0], new_amount)
    print(output_message)


def remove_fruit(L):
    print_list_with_indexes(L)
    my_index = get_integer("Choose index number to update the fruit quantity")
    number = get_integer("Enter how many you would like to add:")
    old_amount = L[my_index][1]
    new_amount = old_amount - number
    print("{} - {} = {}".format(old_amount, number, new_amount))
    output_message = "The number of {} {} has been updated to {}.".format(old_amount, L[my_index][0], new_amount)
    print(output_message)


def add_new_fruit(L):
    print_list(L)
    my_fruit = get_string("What new fruit would you like to add?").title()
    for x in L:
        if my_fruit == x[0]:
            get_string("{} are already in the list. Press any key to return to main menu".format(my_fruit))
            main()
    number = get_integer("How many of this fruit do you have?")
    new_list = [my_fruit, number]
    L.append(new_list)
    print_list(L)
    return None


def main():
    my_fruit_list = [
        ["Apples", 5],
        ["Mangoes", 2],
        ["Kiwifruit", 9],
        ["Peaches", 3],
    ]

    my_menu = [
        ["A", "Add some fruit"],
        ["B", "Remove some fruit"],
        ["C", "Review the list"],
        ["D", "Add a new fruit"],
        ["Q", "Quit"]
    ]

    run = True
    while run == True:
        print_list(my_menu)
        choice = get_string("Please select your option: ->").upper()
        print("." * 100)
        if choice == "A":
            add_fruit(my_fruit_list)
        elif choice == "B":
            remove_fruit(my_fruit_list)
        elif choice == "C":
            print_list_with_indexes(my_fruit_list)
        elif choice == "D":
            add_new_fruit(my_fruit_list)
        elif choice == "Q":
            print("Thank you")
            run = False
        else:
            print("Input was not recognised, please try again")


main()
