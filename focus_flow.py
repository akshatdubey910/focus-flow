import time
import random

# List of motivational quotes
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success doesn’t come from what you do occasionally. It comes from what you do consistently.",
    "Discipline is the bridge between goals and accomplishment.",
    "You’re doing better than you think. Keep going!"
]

print("📚 Welcome to Focus Flow!")
minutes = int(input("⏰ How many minutes do you want to study? "))

# Countdown timer
print(f"\nStarting your {minutes}-minute session. Stay focused! 🚀")
time.sleep(minutes * 60)

# After timer ends
print("\n✅ Time's up! Great job!")
print("💡 Here's a motivational quote for you:\n")
print("👉", random.choice(quotes))
print("\n🔁 Take a 5-minute break before the next session.")
