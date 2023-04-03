"""
    My TODO APPLICATION Project. Code written by Philip Favour Boluwatife in collaboration with Paul John
 """
from prettytable import PrettyTable
print("\nMy TO-DO List Terminal Application.")
manual = "\n1: Enter A or a to add new TO-DO.\n2: Enter D or d to delete TO-DO.\n3: Enter U or u to update TO-DO.\n4: Enter E or e to exit the program.\n5: Enter L or l to checheck your TO-DO List."
print(manual)

my_todo_list = []
x = PrettyTable()

def my_list():
    x.field_names = ["Item Names"]
    for i in my_todo_list:
        x.add_row([i])
    print(x.get_string(title="TO DO LIST"))
    x.clear_rows()

runing = True
while runing:
    user_input = input("\nWhat do you want to do? (A, D, U, E, L): ").lower()
    if user_input == "a":
        new_todo = input("\nPlease enter your new TODO: ").lower()
        print(f"\nYour current TODO is {new_todo}. ")
        my_todo_list.append(new_todo)
    elif user_input == "d":
        while True:
            item_name = input("\nPlease enter a name of an item you want to delete. ").lower()
            try:
                if item_name in my_todo_list:
                    choice = input(f"Are you sure to delete {item_name} from your TODO List? (Y/N) ").lower()
                    if choice == "y":
                        my_todo_list.remove(item_name)
                        print("Your Updated To_Do List")
                        my_list()
                        break
                    else:
                        print("Item not found.")
            except Exception:
                print("Something went wrong.")
    elif user_input == "u":
        while True:
            item_name = input("\nPlease enter the name of the item you want to update. ").lower()
            try:
                if item_name in my_todo_list:
                    choice = input(f"Are you sure to update {item_name} from your Todo List? (Y/N) ").lower()
                    if choice == "y":
                        update_item = input(f"Please enter a name you want to update {item_name} with. ").lower()
                        index = my_todo_list.index(item_name)
                        my_todo_list[index] = update_item
                        print("Your updated TO-DO List: ")
                        my_list()
                        break
                    else:
                        print("Item not found.")
            except Exception:
                print("Something went wrong.")
    elif user_input == "e":
        ask_user = input("\nAre you sure to exit? (Y/N): ").lower()
        if ask_user == "y":
            runing = False
    elif user_input == "l":
        my_list()
    elif user_input == "" or user_input == " ":
        print("Please enter Something.")
    else:
        print("Please enter a valid value.")
