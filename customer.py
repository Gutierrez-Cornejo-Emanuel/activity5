from book import Book

class Customer():
    def __init__(self, name) -> None:
        self.wishlist = []
        self.name = name
    
    def addBookToWishlist(self, book):
        self.wishlist.append(book)
    
    def removeBookFromWishlist(self, book):
        self.wishlist.remove(book)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    def isBookInWishlist(self, book):
        if book in self.wishlist:
            return True
        else:
            return False