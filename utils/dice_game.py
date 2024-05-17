import random
from utils.score import Score

class DiceGame:
    def __init__(self):
        self.score_manager = Score()

    def load_scores(self):
        self.score_manager.load_scores()

    def save_scores(self):
        self.score_manager.save_scores()

    def play_game(self, username):
        while True:
            if self.roll_dice(username):
                choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                try:
                    choice = int(choice)
                    if choice == 1:
                        continue
                    elif choice == 0:
                        break
                    else:
                        print("Invalid choice, returning to menu.")
                        break
                except ValueError:
                    print("Invalid input, returning to menu.")
                    break
            else:
                break
        self.menu(username)  # Return to the user's menu after playing the game

    def show_top_scores(self):
        self.score_manager.print_high_scores()

    def logout(self):
        print("Logging out...")

    def menu(self, username):
        self.load_scores()
        print(f"Welcome, {username}!")
        while True:
            print("Menu:")
            print("1. Start Game")
            print("2. Show Top Scores")
            print("3. Log Out")
            try:
                choice = int(input("Enter your choice, or leave blank to cancel: "))
                if choice == 1:
                    print(f"Starting game as {username}...\n")
                    self.play_game(username)
                elif choice == 2:
                    self.show_top_scores()
                elif choice == 3:
                    self.logout()
                    return
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input, please enter a number.")

    def roll_dice(self, username):
        points = 0
        wins = 0
        round_win = 0
        round_lose = 0
        while round_win < 2 and round_lose < 2:
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)
            print(f"{username} rolled: {user_roll}\n")
            print(f"CPU rolled: {cpu_roll}\n")
            if user_roll > cpu_roll:
                print(f"You win this round, {username}!")
                round_win += 1
                points += 1
            elif cpu_roll > user_roll:
                print("CPU wins this round!")
                round_lose += 1
            else:
                print("It's a tie!")

        if round_win == 2:
            print(f"You won this stage, {username}!\n")
            points += 3
            wins += 1
            print(f"{username} - Total points: {points}, Stages Won: {wins}")
            self.score_manager.add_score(username, points)
            return True
        elif round_lose == 2:
            print(f"You lost this stage, {username}.\n")
            print("Game over. You didn't win any stages.")
            return False
