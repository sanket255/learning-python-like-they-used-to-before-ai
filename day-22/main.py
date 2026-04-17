data={}
while True:
    category=input("Enter the category of you note ( study / work / random ): ")
    if category=="quit":
        break
    else:
        note=input("Enter the note: ")

    if category in data:
        data[category].append (note)
    else:
        data[category] = [note]
    cat=input("Enter category to view: ")
    
    if cat in data:
                print(data[cat])
    else:print("not found!!")






print(data)

