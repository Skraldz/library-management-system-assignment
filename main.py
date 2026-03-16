from library import Library
from book import Book
from member import Member

library = Library()
admin_password = 1234

while True:
    print("Velkommen til Zealands bibliotekssystem")
    print("Tryk 1 for låner menu")
    print("Tryk 2 for administrator menu ")

    choice = input("Vælg:")

    if choice == "1":
        input_id = input("Indtast låner ID:")
        found_member = None
        for member in library.members:
            if member.member_id == input_id:
                found_member = member
            
        if found_member:
            print(f"Velkommen {found_member.name}, foretag en handling:")
            print("Tryk 1 for at låne en bog")
            print("Tryk 2 for at aflevere en lånt bog")
            print("Tryk 3 for at komme tilbage til hovedmenuen")

            choice = input("Vælg:")
            if choice == "1": 
                title = input("Indtast titel eller isbn: ")
                found_book = None

                for book in library.books:
                    if book.title == title or book.isbn == title:
                        found_book = book
                if found_book:
                    found_member.borrow_book(found_book)
                else:
                    print("Ingen bog i systemet matcher denne titel/isbn, prøv igen.")
            
            if choice == "2":
                title = input("Indtast titlen på bogen du vil aflevere:")
                found_book = None

                for book in library.books:
                    if book.title == title or book.isbn == title:
                        found_book = book
                if found_book:
                    found_member.return_book(found_book)
                else:
                    print("Ingen bog på lånerens liste matcher det indtastede, prøv igen.")

            if choice == "3":
                continue
    
    if choice == "2":
        password = input("Indtast administrator password")
        if password == admin_password:
            print("Velkommen administrator, foretag en handling:")
            print("Tryk 1 for at tilføje en bog til systemet")
            print("Tryk 2 for at fjerne en bog fra systemet")
            print("Tryk 3 for at opdatere en bog i systemet")
            print("Tryk 4 for at tilføje en ny låner til systemet")
            print("Tryk 5 for at fjerne en låner fra systemet")
            print("Tryk 6 for at opdatere et medlem i systemet")
            print("Tryk 7 for at vise alle bøger i systemet")
            print("Tryk 8 for at vise alle lånerne i systemet")

            choice = input("Vælg:")

            if choice == "1":
                print("Hvilken type bog vil du tilføje?")
                print("Tryk 1 for almindelig bog")
                print("Tryk 2 for e-bog")
                print("Tryk 3 for lydbog")
    
                book_type = input("Vælg:")
    
                title = input("Indtast bogens titel: ")
                author = input("Indtast bogens forfatter: ")
                isbn = input("Indtast bogens ISBN: ")
                copies = int(input("Indtast antal kopier: "))
    
                if book_type == "1":
                    new_book = Book(title, author, isbn, copies)
                elif book_type == "2":
                    file_format = input("Indtast filformat: ")
                    new_book = Ebook(title, author, isbn, copies, file_format)
                elif book_type == "3":
                    voice_actor = input("Indtast oplæserens navn: ")
                    file_format = input("Indtast filformat: ")
                    new_book = Audiobook(title, author, isbn, copies, voice_actor, file_format)
            
            library.add_book(new_book)
            print(f"{title} er tilføjet til systemet")

            if choice == "2":
                remove_requested_book = input("Indtast titel eller isbn på bogen der skal fjernes")
                

    
        
    else:
                print("Intet låner ID matcher det indtastede, prøv igen.")
