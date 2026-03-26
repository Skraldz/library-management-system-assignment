class Member:
    def __init__(self, name):
        self.member_id = None # tilføjes af library.add_member
        self.name = name
        self.borrowed_books = []

    def display_info(self):
        borrowed_titles = [str(book) for book in self.borrowed_books]
        print(f"Navn: {self.name}, medlems ID: {self.member_id}, lånte bøger: {borrowed_titles}")

    def borrow_book(self, book):
        if book.copies > 0: # Hvis der er flere bøger tilbage
            self.borrowed_books.append(book) # Tilføj bog til listen over udlån
            book.copies -= 1 # Træk en kopi fra mængden af bøger
        else:
            print("Bogen er allerede udlånt") # Er der ikke flere bøger kommer denne meddelelse

    def return_book(self, book):
        if book in self.borrowed_books: # Hvis bogen er udlånt
            self.borrowed_books.remove(book) # Fjerner bogen fra borrowed_books listen
            book.copies += 1 # Tilføjer en kopi til mængden af bøger
        else:
            print("Bogen er ikke udlånt til brugeren") # Ellers udskriver den denne fejlmeddelelse
