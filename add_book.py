class AddBook:
    def __init__(self,title,author,book_id,genre,price,quantity_in_stock):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.genre = genre
        self.price = price
        self.quantity_in_stock = quantity_in_stock
    def add_book(self):
        try:
            if self.quantity_in_stock<=0:
                raise ValueError("Please check the stock quantity again!!")
                
            else:
                with open("Book_Store.txt","a") as f:
                    f.write(f"Title             : {self.title}\n")
                    f.write(f"Author            : {self.author}\n")
                    f.write(f"Book ID           : {self.book_id}\n")
                    f.write(f"Genre             : {self.genre}\n")
                    f.write(f"Price             : {self.price}\n")
                    f.write(f"Quantity in stock : {self.quantity_in_stock}\n\n") 
                    
                    print("\nBook information added successfully!!")
        except TypeError:
            print("\nCould you please check the book information? The stock quantity cannot be negative number or letters. Thank you!")




class AddBookInfo():
    def add_book_info(self):
        print("Please fill The Form with right information!!\n")
        title=input     ("The Book Title : ")
        author=input    ("Author Name    : ")
        book_id=input   ("Book ID        : ")
        genre=input     ("Genre          : ")
        price=input     ("price          : ")
        quantity_in_stock=input("In Stock       : ")
        book=AddBook(title, author, book_id, genre, price, quantity_in_stock)
        book.add_book()
        

    
# book = AddBookInfo()
# book.add_book_info()