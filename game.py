score = 0

print("Welcome to the Arnav Quiz Game! 🎉")

# Question 1
answer1 = input("Q1: What is the capital of India? ").lower()
if answer1 == "delhi":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Nope, it's Delhi.")

# Question 2
answer2 = input("Q2: What does CPU stand for? ").lower()
if answer2 == "central processing unit":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Central Processing Unit.")

# Question 3
answer3 = input("Q3: Who founded Microsoft? ").lower()
if "bill" in answer3 and "gates" in answer3:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! It's Bill Gates.")

# Final Score
print("\n🎯 You got", score, "out of 3 correct!")

if score == 3:
    print("🔥 You’re a genius!")
elif score == 2:
    print("💪 Not bad!")
else:
    print("👀 You can do better next time!")
