import random

print("🪨📄✂️ Welcome to Stone Paper Scissors!")

choices = ["stone", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user_input = input("Choose stone, paper, or scissors (or type exit to quit): ").lower()
    
    if user_input == "exit":
        print("👋 Final Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break

    if user_input not in choices:
        print("❌ Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print("🤖 Computer chose:", computer_choice)

    if user_input == computer_choice:
        print("😐 It's a tie!")
    elif (user_input == "stone" and computer_choice == "scissors") or \
         (user_input == "scissors" and computer_choice == "paper") or \
         (user_input == "paper" and computer_choice == "stone"):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1
