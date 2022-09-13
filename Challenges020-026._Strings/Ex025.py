# Ask the user to enter their first name.
# If the length of their first name is under five characters,
# Ask them to enter their surname and join them together (without a space)
# And display the name in upper case
# If the length of the first name is five or more characters
# display their first name in lower case

firstname = input("Enter your first name: ")
if len(firstname) < 5:
    surname = input("Enter your surname: ")
    fullname = firstname + surname
    print(fullname.upper())
else:
    print(firstname.lower())
