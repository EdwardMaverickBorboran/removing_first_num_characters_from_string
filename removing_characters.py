# Create a program that will --

# Remove characters from a string starting from zero up to n and return a new string.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Expected results
# remove_chars("pynative", 4) so output must be tive. 
# Here, we need to remove the first four characters from a string.

# remove_chars("pynative", 2) so output must be native. 
# Here, we need to remove the first two characters from a string.

# Adding an input function
word_given = input("Enter your word: ")
print(word_given)

# Removing the number of the characters from given word
remove_character = int(input("Please enter number of letters to remove: "))
print("Removing characters from a string")
print(word_given [remove_character:])