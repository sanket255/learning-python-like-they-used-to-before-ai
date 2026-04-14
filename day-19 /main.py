# Build a
print("Movie Rating Tracker")
ask="0"
# Ask user for movie name + rating (1-10)
def inputt():
    movie=[]
    rating=[]

    user_m=input("Enter the movie name: ")
    while True:
        try:
            user_r=int(input(f"rate the movie {user_m}: "))
            break
        except ValueError:
            print("make sure the rating is a NUMBER!!")
            continue

    movie.append(user_m)
    rating.append(user_r)

    # print(pair)

# Store in file (movie: rating format)
    with open("movie.txt", "a") as file:
        file.write((f"{user_m}: {user_r}")+"\n")

    with open ("movie.txt","r") as file:
        print(file.read())
        

# Show average rating of all movies
# def rate():
    # pair=dict(user_m,user_r)
    # valv=int(pair.values())
    # addi=sum(valv)
    # # print(addi)
    # count=len(pair)
    # avg=addi/count
    # print(avg)

# Search for a specific movie's rating
def search():
    keyword=input("Enter the movie name: ")
    with open ("movie.txt", "r") as file:
        for line in file:
            if keyword in line:
                print (line)



while ask!="quit":
    ask=input("( rate a movie (y) / search a movie you rated (a)/ avarage rating of all movies(b) / quit): ")
    if ask == "y":
        inputt()
    elif ask== "a":
        search()
    # elif ask == "b":
    #     rate()
    elif ask == "quit":
        break






# Loop until quit
# 
# Uses: File I/O, dictionaries, loops, try/except.