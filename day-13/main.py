# Day 13 Task: Code Organization
# Build a  (simple, but organized with functions):

print("Contact Manager App")
# Add contact (name, phone, email)
def add_contacts():
    name=input("Enter the name of the person: ")
    number=int(input("Enter the Phone Number of the person: "))
    email=input("Enter the E-Mail of the person (optional, leave blank if not know):")
    with open("contacts.txt", "a" ) as file:
        file.write(f"{name}: {number}, {email}"+ "\n")






