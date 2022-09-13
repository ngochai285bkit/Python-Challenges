# Ask the user to enter a number between 10 and 20 (inclusive)
# If they enter a number within this range,
# Display the message "Thank you"
# Otherwise display the message "Incorrect answer".

num = int(input("Please enter a number between 10 and 20: "))

if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")
