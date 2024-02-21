from book import Book
from customer import Customer
from transaction import Transaction
class BookInventory():
    def __init__(self) -> None:
        self.inventory_count = {}
        self.customer_list = []
        self.transaction_history = []
    def addBook(self, book):
        if not self.isBookPresent(book):
            self.inventory_count[book.title] = 1 
        else:
            self.inventory_count[book.title] += 1 

    def sellBook(self, book):
        if self.isBookPresent(book):
            self.inventory_count[book.title] -= 1
        else:
            return None

    def isBookPresent(self, book):
        if book.title in self.inventory_count.keys() and self.inventory_count[book.title] > 0:
            return True
        else:
            return False
    def addCustomer(self, customer):
        self.customer_list.append(customer)
    
    def isCustomerPresent(self, customer):
        if customer in self.customer_list:
            return True
        else:
            return False

    def ringCustomerUp(self, customer: Customer, books):
        for book in books:
            if customer.isBookInWishlist(book):
                customer.removeBookFromWishlist(book)
            if self.isBookPresent(book):
                self.sellBook(book)
            self.transaction_history.append(Transaction(customer, books))

