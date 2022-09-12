# Write a program that will ask for a number of days
# And then will show how many hours, minutes and seconds are in that number of days

days = int(input("Enter the number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In", days, "days there are ", end="")
print(hours, "hours, ", end="")
print(minutes, "minutes, ", end="")
print(seconds, "seconds.")
