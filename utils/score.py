class Score:
    def __init__(self):
        self.scores = {}

    def load_scores(self):
        try:
            with open('scores.txt', 'r') as f:
                for line in f:
                    username, score = line.strip().split(',')
                    self.scores[username] = int(score)
        except FileNotFoundError:
            print("Scores file not found. Starting fresh.")
        except Exception as e:
            print(f"Error loading scores: {e}")

    def save_scores(self):
        with open('scores.txt', 'w') as f:
            for username, score in self.scores.items():
                f.write(f"{username},{score}\n")

    def add_score(self, username, points):
        if username in self.scores:
            self.scores[username] += points
        else:
            self.scores[username] = points
        self.save_scores()

    def print_high_scores(self):
        print("Top Scores:")
        for username, score in sorted(self.scores.items(), key=lambda item: item[1], reverse=True):
            print(f"{username}: {score}")
