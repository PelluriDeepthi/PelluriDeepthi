'''write a user defined function findname(name) where name is an argument in python to delete phone number from a dictionary phonebook on the basis of the name'''
def findname(name, phonebook):
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name}'s phone number from the phonebook.")
    else:
        print(f"{name} not found in the phonebook.")

# Example phonebook dictionary
phonebook = {
    "John": "123-456-7890",
    "Alice": "987-654-3210",
    "Bob": "555-555-5555"
}

# Call the function to delete a phone number by name
findname("Alice", phonebook)

# Print the updated phonebook
print(phonebook)
