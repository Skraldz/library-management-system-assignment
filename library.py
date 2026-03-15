from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = [] # Laver attributen books som en tom liste
        self.members = [] # Laber attributen members som en tom liste
    
    def add_book(self, book):
        self.books.append(book) # Tager listen over alle bøger og tilføjer den enkelte bog til den

    def remove_book(self, isbn):
        for book in self.books: # Kigger på alle bøger på listen
            if book.isbn == isbn: # Hvis isbn matcher en bogs isbn i listen
                self.books.remove(book) # slet den bog
                print("Bogen er fjernet fra listen") # og print denne meddelelse
            else:
                print("Bogen findes ikke i systemet") # Hvis isbn ikke matcher noget i listen skrives denne i stedet. 

    def update_book(self, isbn, title, author, copies):
        for book in self.books: # Kigger på alle bøger på listen
            if book.isbn == isbn: # Hvis isnb matcher en bog på listen kan de tre nederste variabler blive ændret
                book.title = title
                book.author = author
                book.copies = copies
                print("Bogen er opdateret") # Og denne besked printes
            else:
                print("Bogen kan ikke findes i systemet.") # Matcher isbn ikke en bog på listen, skrives denne besked

    def display_books(self):
        if len(self.books) == 0: # Hvis der ikke er nogen bøger i systemet
            print("Der er ingen bøger i systemet") # printes denne besked
        else: # ellers
            for book in self.books: # finder den en bog
                book.display_info() # og viser information om bogen

    def add_member(self, member):
        self.members.append(member) # Tilføjer et medlem til listen

    def remove_member(self, member_id): 
        for member in self.members: # Kigger på listen af lånere
            if member.member_id == member_id: # Hvis låner ID matcher 
                self.members.remove(member) # sletter den låneren
                print("Låneren er slettet fra systemet") # skrives denne besked
            else:
                print("Låneren findes ikke i systemet") # ellers skrives denne

    def update_member(self, member_id, name, borrowed_books): 
        for member in self.members: # kigger på lånere på listen
            if member.member_id == member_id: # Hvis låner id matcher det indtastede id
                member.name = name # kan navnet ændres
                print("Låneren er opdateret") # og denne besked skrives
            else:
                print("Låneren kan ikke findes i systemet") # ellers skrives denne

    def display_members(self):
        if len(self.members) == 0: # hvis der ikke er nogle lånere på listen
            print("Der er ingen lånere i systemet") # skrives denne besked
        else:
            for member in self.members: # ellers kigger den på listen af lånere
                member.display_info() # og viser låner info

    def issue_book(self, member_id, isbn):
        for member in self.members: # Kigger på lånere på låner-listen
            if member.member_id == member_id: # hvis et låner ID matcher det indtastede
                for book in self.books: # kigges der på listen af bøger på bog-listen
                    if book.isbn == isbn: # hvis en bogs isbn matcher det indtastede
                        member.borrow_book(book) # bliver bogen udlånt til låneren
                    else:
                        print("Bogen er allerede udlånt") # ellers printes denne besked
            else:
                print("Låner ID eller ISBN ikke fundet, prøv igen.") 

    def return_issued_book(self, member_id, isbn):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.isbn == isbn:
                        member.return_book(book)
                        print(f"Bogen({isbn}) er nu returneret")
                    else:
                        print("Bogen er ikke udlånt til denne låner")
            else:
                print("Låner ID eller ISBN ikke fundet, prøv igen.")