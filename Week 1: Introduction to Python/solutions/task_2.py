# List of contact names
contacts = ["John Doe", "Alice Smith", "Bob Johnson"]

# Display welcome message for each contact
# Remember, special message for names starting with 'A'
for name in contacts:
    if name.startswith('A'):
        print(f"Welcome {name}! (Special message for names starting with 'A')")
    else:
        print(f"Welcome {name}!")