# Ask the user to enter their first name
# And then ask them to enter their surname
# Join them together with a space between
# And display the name and the length of whole name

firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
fullname = firstname + " " + surname
print(fullname)
print(len(fullname))