class Library:
    def __init__(self):
        self.books = [] # Laver attributen books som en tom liste
        self.members = [] # Laber attributen members som en tom liste
    
    def add_book(self, book):
        self.books.append(book) # Tager listen over alle bøger og tilføjer den enkelte bog til den

    def remove_book(self, isbn):
        for book in self.books: # For hver bog i listen
            if book.isbn == isbn:
                self.books.remove(book)
                print("Bogen er fjernet fra listen")
            else:
                print("Bogen findes ikke i systemet")

    def update_book(self, isbn, title, author, copies):
        for book in self.books:
            if book.isbn == isbn:
                book.title = title
                book.author = author
                book.copies = copies
                print("Bogen er opdateret")
            else:
                print("Bogen kan ikke findes i systemet.")

    def display_books(self):
        if len(self.books) == 0:
            print("Der er ingen bøger i systemet")
        else:
            for book in self.books:
                book.display_info()

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print("Låneren er slettet fra systemet")
            else:
                print("Låneren findes ikke i systemet")

    def update_member(self, member_id, name, borrowed_books):
        for member in self.members:
            if member.member_id == member_id:
                member.name = name
                print("Låneren er opdateret")
            else:
                print("Låneren kan ikke findes i systemet")

    def display_members(self):
        if len(self.members) == 0:
            print("Der er ingen lånere i systemet")
        else:
            for member in self.members:
                member.display_info()