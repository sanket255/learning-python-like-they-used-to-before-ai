# Day 13 Task: Code Organization
# Build a  (simple, but organized with functions):

print("Contact Manager App")
# Add contact (name, phone, email)
def add_contacts():
    name=input("Enter the name of the person: ")
    while True:
        try:
            number=int(input("Enter the Phone Number of the person: "))
            break
        except ValueError:
            print ("Enter a number please")
            continue
    
    email=input("Enter the E-Mail of the person (optional, leave blank if not know):")
        
    with open("contacts.txt", "a" ) as file:
        file.write(f"{name}: {number}, {email}"+ "\n")
    print("Contact added successfully!!!")

# View all contacts

def view_contacts():
    try:
        with open ("contacts.txt", "r" )as file:
            print(file.read())
    except FileNotFoundError:
        print("file not found")

# Search contact
def search_contacts():
    while True:
        try:
            keyword=input("search by name: ")
            with open ("contacts.txt","r") as file:
                for line in file:
                    if keyword in line:
                        print(line)
                    elif keyword not in line:
                        print("keyword not found try again")
            break
        except FileNotFoundError:
            print("file not found")
            continue
# Delete contact
def del_con():
    keyword1=input("search the contact by name: ")
    with open ("contacts.txt","r") as file:
        lines=file.readlines()
    with open("contacts.txt","w") as file:   
        for line in lines:
            if keyword1 in line:
                print(f"deleted line: {line}")
            if keyword1 not in line:
                file.write(line)

def main():
    ask=0
    while ask!="quit":
        ask=input("Add contact(a)/ search contact(b)/ read contact list(r)/ delete contact(d) or quit?: ")
        if ask=="a":
            add_contacts()
        if ask=="r":
            view_contacts()
        if ask == "b":
            search_contacts()
        if ask == "d":
            del_con()
        if ask == "quit":
            break

main()



        
        



