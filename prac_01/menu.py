MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU_STRING)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU_STRING)
    choice = input(">>> ").upper()
print("Finished")