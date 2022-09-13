# Pig Latin takes the first consonant of a word,
# Move it to the end of the word and adds on an "ay"
# If a word begins with a vowel you just add "way" to the end.
# For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway.
# Create a program that will ask the user to enter a word and change it into Pig Latin.
# Make sure the new word is displayed in lower case.

word = str.lower(input("Please enter a word: "))
first = word[0]
rest = word[1:len(word)]
vowel = "aeiou"
if first in vowel:
    newword = word + "way"
else:
    newword = rest + first + "ay"
print(newword)