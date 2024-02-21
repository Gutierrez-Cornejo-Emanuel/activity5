import unittest
from book import Book
from customer import Customer
from bookInventory import BookInventory


# class TestBooks(unittest.TestCase):
#     pass

class TestCustomers(unittest.TestCase):
    def testAddBookToWishlist(self):
       Book1 = Book("Sherlock Holmes")
       Book2 = Book("Harry Potter")
       Customer1 = Customer("James")
       Customer1.addBookToWishlist(Book1)
       Customer1.addBookToWishlist(Book2)
       self.assertTrue(Customer1.isBookInWishlist(Book1))
       self.assertTrue(Customer1.isBookInWishlist(Book2))

    def testRemoveBookFromWishlist(self):
       Book1 = Book("Sherlock Holmes")
       Book2 = Book("Harry Potter")
       Customer1 = Customer("James")
       Customer1.addBookToWishlist(Book1)
       Customer1.addBookToWishlist(Book2)
       Customer1.removeBookFromWishlist(Book1)
       Customer1.removeBookFromWishlist(Book2)
       self.assertFalse(Customer1.isBookInWishlist(Book1))
       self.assertFalse(Customer1.isBookInWishlist(Book2))
    def testCustomerPresent(self):
       Customer1 = Customer("James")
       Customer2 = Customer("John")
       inv = BookInventory()
       inv.addCustomer(Customer1)
       self.assertTrue(inv.isCustomerPresent(Customer1))
       self.assertFalse(inv.isCustomerPresent(Customer2))
      
       

class TestBookInventory(unittest.TestCase):
    def testAddBook(self):
      Book1 = Book("Sherlock Holmes")
      Inventory = BookInventory()
      Inventory.addBook(Book1)
      self.assertTrue(Inventory.isBookPresent(Book1))
    
    def testRemoveBook(self):
      Book1 = Book("Sherlock Holmes")
      Inventory = BookInventory()
      Inventory.addBook(Book1)
      Inventory.sellBook(Book1)
      self.assertFalse(Inventory.isBookPresent(Book1))

    def testAddCustomer(self):
      Customer1 = Customer("John")
      Inventory = BookInventory()
      Inventory.addCustomer(Customer1)
      self.assertTrue(Inventory.isCustomerPresent(Customer1))
    def testRingCustomerUp(self):
      customer1 = Customer("John")
      Inventory = BookInventory()
      book1 = Book("Harry Potter")
      customer1.addBookToWishlist(book1)
      Inventory.addBook(book1)
      Inventory.ringCustomerUp(customer1, [book1])
      self.assertFalse(customer1.isBookInWishlist(book1))
      self.assertFalse(Inventory.isBookPresent(book1))


def main():
  unittest.main()

if __name__ == "__main__":
  main()