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
    

