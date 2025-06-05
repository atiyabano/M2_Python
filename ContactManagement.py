import json
import os
# function loading contact data to a file______
CONTACTS_FILE = 'contact_data.json'
def load_contacts (CONTACTS_FILE):

    if not os.path.exists(CONTACTS_FILE):
        return{}
    try:
        with open (CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except Exception  as e:
        print({e})
        return{}

# function to save contacts to a file________
def save_contacts(contacts):
    try:
        with open (CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file)
    except Exception as e:
        print({e})


# Function to add a contact_______
def add_contact(contacts, name, phone, email):
    if name in contacts:
        print("contact already exists. Use update option to modify.")
    else:
        contacts[name] = {'phone':phone, 'email': email}
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully!")

#  Function to view all contacts______
def view_contact(contacts):
    if  not  contacts:
        print(f"Contact not found.")
        return
    for name, detail in contacts.items():
        print(f"Name: {name}, phone: {detail['phone']}, Email: {detail['email']}")

# Function to update a contact______
def update_contact(contacts, name, phone=None, Email=None):
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return
    if phone:
        contacts[name]['phone']  = phone
    if Email:
        contacts[name]['email'] = Email
    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")

# FUnction to delete a contact______
def delete_contact(contacts, name):
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name} deleted successfully!")

# Main function to run the contact management system________
def main():
    contacts = load_contacts(CONTACTS_FILE)
    while True:
        print("\nContact management system")
        print("1. Add contact")
        print("2. view contact")
        print("3. Upodate contact")
        print("4.Delete contact")
        print("5. Exit")
        choice = input("Enter your chioce")    
        if choice == '1':
            name = input("Enter the contact name:")
            phone = input("Enter the contact phone number:")
            email= input("Enter the contact email:")
            add_contact(contacts, name, phone, email)
        elif choice == '2':
            view_contact(contacts)
        elif choice == '3':
            name = input("Enter the contact name to update:")
            phone = input("Enter the new phone number(leave blank to keep current):")
            email= input("Enter the new email (leave blank to keep current):")
            update_contact(contacts, name, phone if phone else None, email if email else None)
        elif choice == '4':
            name = input("Enter the contact name to delete:")
            delete_contact(contacts, name)
        elif choice == '5':
            print ("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 5.")


if __name__ == "__main__":
    main()