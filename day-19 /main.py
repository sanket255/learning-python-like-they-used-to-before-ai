# Build a
print("Movie Rating Tracker")
ask="0"
# Ask user for movie name + rating (1-10)
while ask!="quit":
    movie=[]
    rating=[]
    user_m=input("Enter the movie name: ")
    while True:
        try:
            user_r=(input(f"rate the movie {user_m}: "))
            break
        except ValueError:
            print("make sure the rating is a NUMBER!!")
            continue

    movie.append(user_m)
    rating.append(user_r)

    pair=dict(zip(user_m,user_r))
    # print(pair)

# Store in file (movie: rating format)
    
    with open("movie.txt", "a") as file:
        file.write((f"{movie}: {rating}")+"\n")

    with open ("movie.txt","r") as file:
        print(f"{movie}: {rating}")

# Show average rating of all movies
    # valv=int(pair.values())
    # addi=sum(valv)
    # # print(addi)
    # count=len(pair)
    # avg=addi/count
    # print(avg)

# Search for a specific movie's rating
    keyword=input("Enter the movie name: ")
    with open ("movie.txt", "r") as file:
        for line in file:
            if keyword in line:
                print (line)



    ask=input("do you want another movie to rate (y/quit): ")




# Loop until quit
# 
# Uses: File I/O, dictionaries, loops, try/except.