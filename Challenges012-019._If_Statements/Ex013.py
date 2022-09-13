# Ask the user to enter a number that is under 20
# If they enter a number that is 20 or more
# Display the message "Too high"
# Otherwise display "Thank you"

num = int(input("Please enter a number less than 20: "))
if num>=20:
    print("To high")
else:
    print("Thank you")