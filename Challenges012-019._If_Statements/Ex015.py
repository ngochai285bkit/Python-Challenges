# Ask the user to enter their favourite colour.
# If they enter “red”, “RED” or “Red” display the message “I like red too”,
# Otherwise display the message “I don’t like [colour], I prefer red”.

colour = input("Type in your favourite colour: ")
if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too")
else:
    print(f"I don't like {colour}, I prefer red")
