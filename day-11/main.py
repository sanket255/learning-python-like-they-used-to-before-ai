import requests
ask=0
while ask!="quit":
    ask=input("are you ready to witness something godlike (y/quit)?: ")
    try:
        url="https://api.kanye.rest"
        responce = requests.get(url)
        if responce.status_code ==200:
            clean = responce.json()
            data = clean['quote']

            print(f"Kanye says: {data}")
        else:
            print(f"server sent an error code: {responce.status_code}")

    except requests.exceptions.ConnectTimeout:
        print("Internet is gone")

    except Exception as e:
        print(f"Something went wrong: {e}")
    ask=input("do you want to save this in your collection? (y/quit): ")
    if ask =="y":
        with open ("kanye.txt", "a") as file:
            file.write(data + "\n")
# 
# # https://api.kanye.rest


# import requests
# url = "https://api.kanye.rest"
# ask=0
# while ask!="quit":
#     ask =input("yk whats kanye thinking?(y/quit): ")
#     if ask != "y" and ask != "quit":
#         print("it only works with either y/quit")
#         continue
#         # break
#     responce =requests.get(url)
#     data = responce.json()
#     try:
#         if responce.status_code ==200:
#             print(f"Kanye says: {data['quote']}")

#     except requests.exceptions.ConnectTimeout:
#         print("internet is not working")
#     except Exception as e:
#         print(f"something went wrong: {e}")


#     save=input("do you wan to save what kanye said forvever in a file? (y/quit):")
#     if save == "y":
#         with open ("yesays.txt", "a") as file:
#             file.write(data['quote'] + "\n")

    
























