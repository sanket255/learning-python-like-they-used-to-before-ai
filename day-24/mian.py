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
            (self.shelf).remove(title) and (self.borrow).append(title)
            print(self.borrow)
    

