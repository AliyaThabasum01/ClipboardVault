from vault import save_clipboard, view_history

while True:
    print("\n===== ClipboardVault =====")
    print("1. Save Text")
    print("2. View History")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        text = input("Enter text: ")
        save_clipboard(text)

    elif choice == "2":
        view_history()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
