class Book:
    def __init__(self, title, author, isbn, copies, file_format="Fysisk"):
        self.title = title
        self.author = author
        self.copies = copies
        self.isbn = isbn
        self.file_format = file_format

    def display_info(self):
        print(f"isbn: {self.isbn}, Titel: {self.title}, Forfatter: {self.author}, Antal kopier: {self.copies}")

class Ebook(Book): # Book i parentes ved denne klassedefinition betyder at Book er forældreklassen (enheritance)
    def __init__(self, title, author, isbn, copies, file_format):
        super().__init__(title, author, isbn, copies, file_format) # Kører init fra Book klassen (enheritance) - Super() bruger forældreklassen (Book)
        
    def display_info(self):
        print(f"Titel: {self.title}, Forfatter: {self.author}, Format: {self.file_format}, antal kopier: {self.copies}")

class Audiobook(Book): # Book i parentes ved denne klassedefinition betyder at Book er forældreklassen (enheritance)
    def __init__(self, title, author, isbn, copies, voice_actor, file_format):
        super().__init__(title, author, isbn, copies, file_format) # Kører init fra Book klassen (enheritance) - Super() bruger forældreklassen (Book)
        self.voice_actor = voice_actor

    def display_info(self):
        print(f"isbn: {self.isbn} Titel: {self.title}, Forfatter: {self.author}, Format: {self.file_format}, Indtalt af: {self.voice_actor}, antal kopier: {self.copies}")