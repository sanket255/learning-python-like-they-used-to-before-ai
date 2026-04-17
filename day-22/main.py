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



print(data)

