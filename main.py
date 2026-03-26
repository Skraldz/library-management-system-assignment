from library import Library
from book import Book, Ebook, Audiobook
from member import Member

library = Library()
admin_password = "1234"

while True:
    print("Velkommen til Zealands bibliotekssystem")
    print("Tryk 1 for låner menu")
    print("Tryk 2 for administrator menu ")

    choice = input("Vælg:")

    if choice == "1":
        input_id = input("Indtast låner ID:")
        found_member = None
        for member in library.members:
            if member.member_id == int(input_id):
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
        else :
            print("ID ikke fundet, prøv igen.")
            continue
    
    if choice == "2":
        password = input("Indtast administrator password: ")
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

            if choice == "2":
                isbn = input("Indtast isbn på bogen der skal fjernes fra systemet: ")
                library.remove_book(isbn)
                
            if choice == "3":
                index_or_isbn = input("Vil du opdatere bogen via indeks-søgning(tast 1) eller isbn-nummer(tast 2)?: ")
                if index_or_isbn == "1":
                    library.display_books()
                    index = int(input("Indtast nummer på bogen der skal opdateres: ")) -1
                    book = library.books[index]
                    isbn = book.isbn
                else:
                    isbn = input("Indtast isbn på bogen der skal opdateres i systemet: ")
                title = input("Indtast opdateret titel: ")
                author = input("indtast opdateret forfatter: ")
                copies = int(input("Indtast opdateret antal kopier: "))

                print("Hvilken type bog er det?")
                print("Tryk 1 for fysisk bog")
                print("Tryk 2 for e-bog")
                print("Tryk 3 for lydbog")
                book_type = input("Vælg mellem 1-3: ")
                
                if book_type == "1":
                    file_format = "Fysisk"
                    voice_actor = None
                elif book_type == "2":
                    file_format = "E-bog"
                    voice_actor = None
                elif book_type == "3":
                    file_format = "Lydbog"
                    voice_actor = input("Indtast navn på oplæser:")
                else:
                    print("Forkert indtastning, prøv igen.")
                library.update_book(isbn, title, author, copies, file_format, voice_actor)

            if choice == "4":
                new_member_name = input("Indtast navnet på den nye låner: ")
                new_member = Member(new_member_name)
                library.add_member(new_member)
                print(f"Låner {new_member_name} er blevet tildelt ID {new_member.member_id}")

            if choice == "5":
                member_id = input("Indtast låner ID for at slette låneren fra databasen: ")
                library.remove_member(member_id)

            if choice == "6":
                index_or_id = input("Vil du opdatere via indeks-søgning(tast 1) eller låner ID(tast 2)?: ")
                if index_or_id == "1":
                    library.display_members()
                    index = int(input("Indtast indeksnummer på låneren der skal opdateres: ")) -1
                    member = library.members[index]
                    member_id = member.member_id
                else:
                    member_id = input("Indtast låner ID på låneren der skal opdateres: ")
                name = input("Indtast det opdaterede låner navn: ")
                library.update_member(member_id, name)
                print(f"Låneren er opdateret med navnet {name}.")


            if choice == "7":
                library.display_books()
        
            if choice == "8":
                library.display_members()

        else:
                print("Forkert password, prøv igen")
