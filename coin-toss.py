import random

print("===== COIN TOSSING GAME =====")

while True:
    times = int(input("How many times do you want to toss? "))

    if times <= 0:
        print("Please enter a number greater than 0.")
        continue

    heads = 0
    tails = 0
    score = 0

    for i in range(times):
        print(f"\nToss {i + 1}")

        guess = input("Guess Heads or Tails: ").capitalize()

        if guess not in ["Heads", "Tails"]:
            print("Invalid guess! You lose this round.")
            guess = ""

        coin = random.choice(["Heads", "Tails"])

        print("Coin result:", coin)

        if coin == "Heads":
            heads += 1
        else:
            tails += 1

        if guess == coin:
            print("Correct guess! ")
            score += 1
        else:
            print("Wrong guess!")

    print("\n===== FINAL RESULTS =====")
    print("Total tosses:", times)
    print("Heads:", heads)
    print("Tails:", tails)
    print("Correct guesses:", score)
    print("Wrong guesses:", times - score)

    print(f"Heads percentage: {heads / times * 100:.2f}%")
    print(f"Tails percentage: {tails / times * 100:.2f}%")

    if score > times / 2:
        print("Great job! You guessed most tosses correctly!")
    elif score == times / 2:
        print("Good game! You got half your guesses correct.")
    else:
        print("Better luck next time!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! Goodbye! ")
        break