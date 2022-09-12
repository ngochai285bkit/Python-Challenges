# Ask how many slices of pizza the user started with
# And ask how many slices they have eaten.
# Work out how many slices they have left
# And display the answer in a user-friendly format

startNum = int(input("Enter the number of slices of pizza you started with: "))
endNum = int(input("How many slices have you eaten? "))
slicesLeft = startNum - endNum
print("You have", slicesLeft, "slices remaining")
