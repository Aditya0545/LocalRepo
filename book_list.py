# python program to print the  details of the book with tittles, author and year
class books():
    def info(self):
        print(f"Tittle of the book : {self.tittle}\nAuthor : {self.author}\nYear of publition : {self.year}")

book1 = books()
book1.tittle = "To Kill a Mockingbird"
book1.author = "Harper Lee"
book1.year = 1960

book2 = books()
book2.tittle = "The Great Gatsby"
book2.author = "F. Scott Fitzgerald"
book2.year = 1925

book3 = books()
book3.tittle = "The Catcher in the Rye"
book3.author = "J.D. Salinger"
book3.year = 1951

book4 = books()
book4.tittle = "Harry Potter and the Sorcerer's Stone"
book4.author = "J.K. Rowling"
book4.year = 1997

book1.info()
print("\n")
book2.info()
print("\n")
book3.info()
print("\n")
book4.info()

    