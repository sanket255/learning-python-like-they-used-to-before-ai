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

# View all contacts
def view_contacts():
    with open ("contacts.txt", "r" )as file:
        print(file.read())


# Search contact
def search_contacts():
    keyword=input("search by name: ")
    with open ("contacts.txt","r") as file:
        for line in file:
            if keyword in line:
                print(line)

# Delete contact
def del_con():
    keyword1=input("search the contact by name: ")
    with open ("contacts.txt","r") as file:
        lines=file.readlines()

        
        
    with open("contacts.txt","w") as file:   
        for line in lines:
            if keyword1 not in line:
                file.write(line)
                



