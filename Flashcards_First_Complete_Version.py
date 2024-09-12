import random


# Initialize the exit condition
exit = False

# Escaping backslashes

# Using a raw string

import csv

# Use the correct file path and 'with' statement
with open(r"C:\Users\simon\OneDrive\Desktop\TM112_Glossary.txt", "r") as file:
    reader = csv.reader(file)
    table = []
    for row in reader:
        table.append(row)

# Now 'table' contains the rows from the CSV file
print(table)

# Glossary (dictionary)
glossary = {
    "toy1": "car",
    "toy2": "bear",
    "toy3": "barbie doll"
}

# Get the initial user input
import random

# Sample glossary dictionary
glossary = {
    "toy1": "car",
    "toy2": "bear",
    "toy3": "barbie doll"
}

def flashcard_game(glossary):
    exit = False
    user_input = input("Press 's' to show a flash card, or 'quit' to exit: ")

    while not exit:
        if user_input.lower() in ["quit", "stop", "q"]:
            exit = True
        elif user_input.lower() == "s":
            toy = random.choice(list(glossary.items()))  # Choose a random key-value pair from the glossary
            print(f"Flashcard: {toy[0]} - {toy[1]}")  # Print the key and its corresponding value
        else:
            print("Invalid input, please try again.")

        if not exit:
            user_input = input("Press 's' to show another flash card, or 'quit' to exit: ")

# Call the function to start the flashcard game
flashcard_game(glossary)
