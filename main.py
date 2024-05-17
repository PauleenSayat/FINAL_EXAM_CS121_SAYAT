from utils.dice_game import DiceGame
from utils.user_manager import UserManager

dice_game = DiceGame()
user_manager = UserManager()

def main():
    while True:
        print("\n*** WELCOME TO DICE GAME ***\n")
        print("1. Register")
        print("2. Login")
        print("3. Exit\n")
        choice = input("What would you like to do?(1-3) ")
        try:
            choice = int(choice)
            if choice == 1:
                user_manager.register_user()
            elif choice == 2:
                user = user_manager.login_user()
                if user:
                    dice_game.menu(user.username)
            elif choice == 3:
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main()
