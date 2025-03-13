# Dictionary simulating a switch statement

day_messages = {
    "monday": "Today is Monday.",
    "tuesday": "Today is Tuesday.",
    "wednesday": "Today is Wednesday.",
    "thursday": "Today is Thursday.",
    "friday": "Today is Friday.",
    "saturday": "Today is Saturday.",
    "sunday": "Today is Sunday."
}

# Get user input and normalize it
day = input("Enter a day of the week: ").strip().lower()

# Retrieve message with default for invalid input
message = day_messages.get(day, "Invalid day entered.")

# Determine if it's a weekend or a weekday
day_type = "Weekend" if day in ("saturday", "sunday") else "Weekday"

# Display results
print(message)
print("It's a", day_type + "!")