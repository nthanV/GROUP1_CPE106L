import argparse
import oxo_args_ui
import oxo_gui_complete

def console_game():
    oxo_args_ui.main()

def gui_game():
    oxo_gui_complete.gui_main()  # Call the GUI interface directly

def main():
    parser = argparse.ArgumentParser(description="Tic-Tac-Toe Game")
    parser.add_argument('--console', action='store_true', help="Play in console mode")
    parser.add_argument('--gui', action='store_true', help="Play in GUI mode")

    args = parser.parse_args()

    if args.console:
        console_game()
    elif args.gui:
        gui_game()
    else:
        choice = input("Do you want to play in console or GUI? (console/gui): ").lower()
        if choice == 'console':
            console_game()
        elif choice == 'gui':
            gui_game()
        else:
            print("Invalid choice. Please choose 'console' or 'gui'.")

if __name__ == "__main__":
    main()
