def get_string(m):
    my_string = input(m)
    return my_string

def get_integer(message):
    my_integer = int(input(message))
    return my_integer


def print_list(L):
    for i in range(0, len(L)):
        if len(L[i]) != 2:
            print("Sublist is not the correct length")
            return None
        output = "{:3} : {:<3}".format(L[i][0], L[i][1])
        print(output)


def main():
    my_fruit = [
        ["Apple", 5],
        ["Mangoes", 2],
        ["Kiwifruit", 9],
        ["Peaches", 3],
    ]

    my_menu = [
    ["R", "Review the list"],
    ["Q", "Quit"]
    ]

    run = True
    while run == True:
        print_list(my_menu)
        choice = get_string("Please select your option: ->").upper()
        print("." * 100)
        if choice == "R":
            print_list(my_fruit)
        elif choice == "Q":
            print("Thank you")
            run = False
        else:
            print("Input was not recognised, please try again")


main()

