import random

# Step 1: Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

# Step 2: Ask user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Step 3: Check if guess is correct
if guess == secret_number:
    print("🎉 You got it!")
else:
    print("❌ Nope! The number was", secret_number)
