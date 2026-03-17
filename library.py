from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = [] # Laver attributen books som en tom liste
        self.members = [] # Laber attributen members som en tom liste
        self.next_member_id = 0 # tæller der starter på 0
    
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print("En bog med dette ISBN findes allerede i systemet")
                return
        self.books.append(book) # Tager listen over alle bøger og tilføjer den enkelte bog til den
        print("Bogen er tilføjet til systemet")

    def remove_book(self, isbn):
        for book in self.books: # Kigger på alle bøger på listen
            if book.isbn == isbn: # Hvis isbn matcher en bogs isbn i listen
                self.books.remove(book) # slet den bog
                print("Bogen er fjernet fra listen") # og print denne meddelelse
            else:
                print("Bogen findes ikke i systemet") # Hvis isbn ikke matcher noget i listen skrives denne i stedet. 

    def update_book(self, isbn, title, author, copies, file_format=None, voice_actor=None):
        for book in self.books: # Kigger på alle bøger på listen
            if book.isbn == isbn: # Hvis isnb matcher en bog på listen kan de tre nederste variabler blive ændret
                book.title = title
                book.author = author
                book.copies = copies
                book.file_format = file_format
                if voice_actor and isinstance(book, (Audiobook)):
                    book.voice_actor = voice_actor
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
        member.member_id = self.next_member_id # Tildel det næste ledige ID
        self.members.append(member) # Tilføjer et medlem til listen
        self.next_member_id += 1 # forøg tælleren til næste gang den bruges

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
        for member in self.members: # Kigger på lånere på låner-listen
            if member.member_id == member_id: # Hvis et låner ID matcher det indtastede ID
                for book in member.borrowed_books: # Kigges der på lånerens udlånet bøger
                    if book.isbn == isbn: # Hvis en bog matcher det indtastede isbn
                        member.return_book(book) # kaldes return_book funktionen af den specifikke bog
                        print(f"Bogen({isbn}) er nu returneret") # og denne besked printes
                    else:
                        print("Bogen er ikke udlånt til denne låner") # Kan bogen ikke findes hos låneren printes denne
            else:
                print("Låner ID eller ISBN ikke fundet, prøv igen.") # Kan låneren eller ISBN ikke findes printes denne