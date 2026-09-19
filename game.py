import random


def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy   - 10 attempts, numbers 1-50")
    print("2. Medium - 7 attempts, numbers 1-100")
    print("3. Hard   - 5 attempts, numbers 1-200")

    while True:
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            return "Easy", 50, 10
        elif choice == "2":
            return "Medium", 100, 7
        elif choice == "3":
            return "Hard", 200, 5
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


def calculate_score(max_attempts, attempts, difficulty):
    base_score = {
        "Easy": 100,
        "Medium": 200,
        "Hard": 300
    }

    score = base_score[difficulty]
    score -= (attempts - 1) * 10

    # Bonus for guessing with fewer attempts
    if attempts <= max_attempts // 2:
        score += 50

    return max(score, 10)

def update_high_score(high_score, current_score):
    if current_score > high_score:
        print(f"\n🏅 New High Score: {current_score}!")
        return current_score
    return high_score


def play_game():
    difficulty, max_number, max_attempts = choose_difficulty()

    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\n🎯 Difficulty: {difficulty}")
    print(f"Guess a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess < 1 or guess > max_number:
            print(f"⚠️ Please enter a number between 1 and {max_number}.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        if guess == secret_number:
            score = calculate_score(
                max_attempts,
                attempts,
                difficulty
            )

            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempt(s).")
            print(f"🏆 Your Score: {score}")

            return score

        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        if remaining > 0:
            print(f"Attempts remaining: {remaining}")

    print("\n💀 Game Over!")
    print(f"The correct number was: {secret_number}")
    print("Better luck next time!")

    return 0


def main():
    print("=" * 40)
    print("       🎯 NUMBER GUESSING GAME")
    print("=" * 40)

    total_score = 0
    games_played = 0
    high_score = 0
    wins = 0

    while True:
        score = play_game()

        total_score += score
        games_played += 1

        if score > 0:
            wins += 1
    
        high_score = update_high_score(high_score, score)

        print("\n" + "-" * 40)
        print(f"Games Played: {games_played}")
        print(f"Games Won: {wins}")
        print(f"Total Score: {total_score}")
        print(f"High Score: {high_score}")
        print("-" * 40)

        while True:
            replay = input("\nDo you want to play again? (y/n): ").lower()

            if replay in ("y", "yes"):
                break
            elif replay in ("n", "no"):
                print("\nThanks for playing! 👋")
                print(f"Final Score: {total_score}")
                print(f"Games Played: {games_played}")
                print(f"Games Won: {wins}")
                print(f"High Score: {high_score}")
                return
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()