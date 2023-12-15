from Grammar import ContextFreeGrammar


def main():
    grammar = ContextFreeGrammar()
    file_path = input("Enter the path of the grammar file: ")
    try:
        grammar.load_grammar(file_path)
    except ValueError as e:
        print(e)
        return

    while True:
        print("\nContext-Free Grammar Menu")
        print("1. Display Non-Terminals")
        print("2. Display Terminals")
        print("3. Display Start Symbol")
        print("4. Display Production Rules")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Non-Terminals:", grammar.display_non_terminals())
        elif choice == '2':
            print("Terminals:", grammar.display_terminals())
        elif choice == '3':
            print("Start Symbol:", grammar.display_start_symbol())
        elif choice == '4':
            print("Production Rules:", grammar.display_productions())
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
