from app import Contact
from contacts import ContactsBook


def main():
    contacts_book = ContactsBook()

    while True:
        print("\nOptions:")
        print("1. Add a contact")
        print("2. Display contacts")
        print("3. Quit")

        option = int(input("Enter an option: "))

        if option == 1:
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            contact = Contact(name, phone, email)
            contacts_book.add_contact(contact)

        elif option == 2:
            contacts_book.display_contacts()

        elif option == 3:
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()