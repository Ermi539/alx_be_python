shopping_list = []

def display_menu():
    """Displays the menu options for the shopping list."""
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    """Main function to handle shopping list operations."""
    print(f"Shopping List Manager")  # Added the requested print statement
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")  # Modified input prompt
            shopping_list.append(item)
            print(f"{item} added to the list.")
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == '3':
            if shopping_list:
                print("\nShopping List:")
                for item in shopping_list:
                    print(item)
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
