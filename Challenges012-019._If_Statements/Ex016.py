# Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. 
# If they answer “yes”, ask if it is windy. 
# If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, 
# Otherwise display the message “Take an umbrella”. 
# If they did not answer yes to the first question, display the answer “Enjoy your day”.

raining = str.lower(input("Is it raining? "))
if raining == "yes":
    windy = str.lower(input("Is it windy? "))
    if windy == "yes":
        print("It is too windy for and umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")
