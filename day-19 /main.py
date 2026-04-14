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

    # pair=dict(zip(user_m,user_r))
    # print(pair)







# Loop until quit
# 
# Uses: File I/O, dictionaries, loops, try/except.