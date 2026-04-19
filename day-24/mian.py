class Library:
    def __init__(self):
        print("Library")
        self.shelf = []
        self.borrow= []

    def add_book(self,title):
        if title in self.shelf:
            print(f"the book {title} already exist!!")
        elif title not in self.shelf:
            (self.shelf).append(title)
            print(self.shelf)
            
    def borrow_book(self,title):
        if title in self.borrow:
            print(f"{title} this book is already borrowed")
            print(f"{self.shelf} here are other options we have")            
        elif title in self.shelf:
            (self.shelf).remove(title) 
            (self.borrow).append(title)
            print(self.borrow)

    def return_book(self,title):
        if title not in self.shelf and title not in self.borrow:
            print("thanks for charity we will make sure to make it as accessible as possible!!")
            (self.shelf).append(title)
        # elif title not in self.shelf:
        #     (self.shelf).append(title)
        elif title in self.borrow:
            (self.borrow).remove(title)
            (self.shelf).append(title)
            
            
lib=Library()
while True:
    book = input("add book ( add book name / quit ):")
    if book=="quit":
        break
    lib.add_book(book)

while True:
    check=input("what operation you have to do (borrow book(b)/ return book(r) / quit ) : ")

    if check == "quit":
        break
    
    elif check == "b":
        lib.borrow_book(input("Enter the book name you want to borrow: "))
    
    elif check == "r":
        lib.return_book(input("enter the book name you want to return: "))
    

