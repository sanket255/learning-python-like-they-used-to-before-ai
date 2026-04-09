
ask="0"
while ask!="quit":
    for i in range(5):
        with open ("file.txt", "a") as file:
            file.write(input("Enter five lines: ")+"\n")


    with open ("file.txt","r") as file:
        lines=file.readlines()
        for index, line in enumerate(lines):
            print(f"{index + 1}:{line}")


    with open ("file.txt") as file:
        keyword=input("search keyword: ")
        for line in file:
            if keyword in line:
                print(line)

    ask=input("another oparetion?: ")

