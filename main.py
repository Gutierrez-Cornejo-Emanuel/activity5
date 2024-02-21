from bookInventory import BookInventory
from customer import Customer
from book import Book
def main():

    print("Store owner adds 3 books to inventory:")
    Inventory = BookInventory()
    Book1 = Book("Sherlock Holmes")
    Book2 = Book("Harry Potter")
    Book3 = Book("Dune")
    Book4 = Book("Sherlock Holmes")
    Inventory.addBook(Book1)
    Inventory.addBook(Book2)
    Inventory.addBook(Book3)
    Inventory.addBook(Book4)
    print("Book Inventory: ")
    print(Inventory.inventory_count)

    print("3 customers walk in and the store owner adds them to the system")
    Customer1 = Customer("John")
    Customer2 = Customer("Mary")
    Customer3 = Customer("Bartholomew")
    Inventory.addCustomer(Customer1)
    Inventory.addCustomer(Customer2)
    Inventory.addCustomer(Customer3)
    print("Customers: ")
    print(Inventory.customer_list)

    print("Customer John adds Harry Potter to his wishlist")
    Customer1.addBookToWishlist(Book2)
    print("John's Wishlist:")
    print(Customer1.wishlist)

    print("Customer John buys Harry Potter Book")
    print("Now the book inventory is this: ")
    print(Inventory.inventory_count)
    print(Customer1.wishlist)
    #Inventory.sellBook(Book2)
    Inventory.ringCustomerUp(Customer1, [Book2])
    print(Inventory.inventory_count)
    print(Customer1.wishlist)



if __name__ == "__main__":
    main()