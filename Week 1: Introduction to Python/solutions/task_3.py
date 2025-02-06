contacts = []

def add_contact(name: str, phone_number: str, email: str) -> int:
    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email
    }
    contacts.append(contact)
    contact_id = len(contacts) - 1
    return contact_id  # Return the index (ID) of the new contact

def update_contact(id: int, name: str, phone_number: str, email: str) -> None:
    if 0 <= id < len(contacts):
        contacts[id] = {
            'name': name,
            'phone_number': phone_number,
            'email': email
        }

def display_contacts():
    for i, contact in enumerate(contacts):
        print(f"\nContact Information (ID: {i}):")
        print(f"Name: {contact['name']}")
        print(f"Phone Number: {contact['phone_number']}")
        print(f"Email: {contact['email']}")

# Test the functions
contact_id = add_contact("John Doe", "123-456-7890", "john@example.com")
_ = add_contact("Alice Smith", "123-456-7777", "alice@example.com")
update_contact(
    id=contact_id,
    name="John Doe",
    phone_number="555-555-5555",
    email="john@example.com"
)
display_contacts()