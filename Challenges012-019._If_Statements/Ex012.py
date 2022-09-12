# Ask for two numbers.
# If the first one is larger then the second
# Display the second number first and then the first number
# Otherwise show the first number first and then the second

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
