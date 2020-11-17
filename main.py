"""
File Name: main.py
Function List:
  main_menu()       Provides display and functionality for main menu.
  sales_menu()      Provides display and functionality for sales menu.
  inv_menu()        Provides display and functionality for inventory menu.
  settings_menu()   Provides display and functionality for settings menu.
  new_sale()        Takes in sales info, writes transaction to log, and
                    adjusts inventory.
  view_inv()        Provides in-program view of inventory.
  add_inv()         Allows user to add/modify inventory items/quantities.
  change_msg()      Allows user to customize the Message of the Day! *neat*
  read_inventory()  Helper function, reads inventory from file to dictionary
                    on program launch.
  write_inventory() Helper function, writes inventory to file during user
                    requested export or at program exit.
  clear()           Helper function, clears terminal based on operating system.
  run_exit()        Houses clean-up functions necessary for clean exit
                    of the program.
"""


# Imports necessary for clear() and sleep() calls
import os
import time


"""
Function: main_menu     Provides display and functionality for main menu.
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def main_menu(msg, d):
    clear()
    print("Welcome to Point of Sale/Inventory Management System\n" + msg)
    print("\nPlease select from the following menu items...\n")
    print("1.) Sales Menu")
    print("2.) Inventory Menu")
    print("3.) Settings")
    print("4.) Exit")
    user_choice = input("#> ")
    if user_choice == "1":
        sales_menu(msg, d)
    elif user_choice == "2":
        inv_menu(msg, d)
    elif user_choice == "3":
        settings_menu(msg, d)
    elif user_choice == "4":
        run_exit()
    else:
        print("Invalid selection, please enter a valid selection.")
        time.sleep(2)
        main_menu(msg, d)


"""
Function: sales_menu    Provides display and functionality for sales menu.
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def sales_menu(msg, d):
    clear()
    print("Sales Menu\n")
    print("Please select from the following menu items...\n")
    print("1.) New Sale")
    print("2.) Return to Main Menu")
    user_choice = input("#> ")
    if user_choice == "1":
        new_sale(msg, d)
    elif user_choice == "2":
        main_menu(msg, d)
    else:
        print("Invalid selection, please enter a valid selection.")
        time.sleep(2)
        sales_menu(msg, d)


"""
Function: inv_menu      Provides display and functionality for inventory menu.
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def inv_menu(msg, d):
    clear()
    print("Inventory Menu\n")
    print("Please select from the following menu items...\n")
    print("1.) View Inventory")
    print("2.) Add Item to Inventory")
    print("3.) Export Inventory")
    print("4.) Return to Main Menu")
    user_choice = input("#> ")
    if user_choice == "1":
        view_inv(msg, d)
    elif user_choice == "2":
        add_inv(msg, d)
    elif user_choice == "3":
        filename = input("Please enter a filename: ")
        write_inventory(d, filename)
    elif user_choice == "4":
        main_menu(msg, d)
    else:
        print("Invalid selection, please enter a valid selection.")
        time.sleep(2)
        inv_menu(msg, d)


"""
Function: settings_menu Provides display and functionality for settings menu.
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def settings_menu(msg, d):
    print("Settings Menu\n")
    print("Please select from the following menu items...\n")
    print("1.) Change Message of the Day")
    print("2.) Return to Main Menu")
    user_choice = input("#> ")
    if user_choice == "1":
        change_msg(msg, d)
    elif user_choice == "2":
        main_menu(msg, d)
    else:
        print("Invalid selection, please enter a valid selection.")
        time.sleep(2)
        settings_menu(msg, d)


"""
Function: new_sale      Takes in sales info, writes transaction to log, and
                        adjusts inventory.
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def new_sale(msg, d):
    try:
        name = input("Enter customer name: ")
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        ppi = float(input("Enter price per item: "))

        if item in d:
            old_q = int(d.get(item))
            new_q = old_q - quantity
            d.update({item: new_q})
        else:
            d[item] = -quantity

        with open("transactions.txt", mode='a') as f:
            f.write(name + " - " + str(item) + ": " + str(quantity) + " $" + str(round(quantity * ppi, 2)) + "\n")
    except ValueError:
        print("Invalid selection, please enter a valid selection.")
        time.sleep(2)
        new_sale(msg, d)
    finally:
        sales_menu(msg, d)


"""
Function: view_inv      Provides in-program view of inventory.
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def view_inv(msg, d):
    for key, val in d.items():
        print(str(key) + " >> " + str(val))
    input("\nPress Enter to Continue...")

    inv_menu(msg, d)


"""
Function: add_inv       Allows user to add/modify inventory items/quantities.
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def add_inv(msg, d):
    try:
        new_item = input("Enter new item name: ")
        new_quantity = int(input("Enter new quantity: "))
        d.update({new_item: new_quantity})
    except ValueError:
        print("Invalid input, ensure an whole number was entered for quantity.")
        time.sleep(2)
        add_inv(msg, d)
    finally:
        inv_menu(msg, d)


"""
Function: change_msg    Allows user to customize the Message of the Day! *neat*
Input variables:        msg - string storing message of the day
                        d - dictionary storing inventory
Output variables:       none
Global variables:       none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def change_msg(msg, d):
    print("Please enter a new message: ")
    new_msg = input("#> ")
    print("New message will be: " + new_msg)
    confirm = str(input("Confirm? (Y)es/(N)o")).lower()
    if confirm == "y" or "yes":
        msg = new_msg
        settings_menu(msg, d)
    else:
        change_msg(msg, d)


"""
Function: read_inventory Helper function, reads inventory from file to dictionary
                         on program launch.
Input variables:         none
Output variables:        none
Global variables:        none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def read_inventory():
    d = {}
    with open("inventory.txt", mode='r') as f:
        for line in f:
            (key, val) = line.strip("\n").split(sep=",")
            d[key] = int(val)

    return d


"""
Function: write_inventory   Helper function, writes inventory to file during user
                            requested export or at program exit.
Input variables:            d - dictionary storing inventory
                            filename - user designated filename, or "inventory.txt" if none provided
Output variables:           none
Global variables:           none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def write_inventory(d, filename="inventory.txt"):
    if filename != "inventory.txt":
        filename = time.strftime("%Y-%m-%d-%H%M%S - " + filename + ".txt", time.localtime())
    with open(filename, mode="w") as f:
        for key, val in d.items():
            f.write(str(key) + "," + str(val) + "\n")


"""
Function: clear     Helper function, clears terminal based on operating system.
Input variables:    none
Output variables:   none
Global variables:   none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def clear():
    # if windows
    if os.name == 'nt':
        _ = os.system('cls')
    # if unix
    else:
        _ = os.system('clear')


"""
Function: run_exit  Houses clean-up functions necessary for clean exit
                    of the program.
Input variables:    none
Output variables:   none
Global variables:   none
Version History:
  11/15/20  J. Setliff
  Initial implementation.
"""


def run_exit():
    write_inventory(d_inv)
    quit(0)


if __name__ == '__main__':
    user_defined_msg = "Remember to SMILE :)"
    d_inv = read_inventory()

    while True:
        main_menu(user_defined_msg, d_inv)
