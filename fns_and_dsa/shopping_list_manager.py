def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(item)
    else:
        print("Shopping list is empty.")

def main():
    shopping_list = []

    while True:
        print("\nShopping List Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
