print("We have three types of operations!!")
print("1. Add a new Book info")
print("2. Read Book Store")
print("3. Search Book info")
print("4. Remove specific Book info")

while True:
    n= input("\nPlease enter the number of the operation you would like to run, or type 'Exit: ")
    if n.isnumeric() and int(n)==1 :
        from add_book import AddBookInfo
        book = AddBookInfo().add_book_info()

    elif n.isnumeric() and int(n)==2:
        from read_book_store import ReadBook
        read=ReadBook().read_store()

    elif n.isnumeric() and int(n)==3:
        from search import SearchingInfo
        view=SearchingInfo().search_book_info()

    elif n.isnumeric() and int(n)==4:
        from remove import RemoveBookInfo
        remove_book = RemoveBookInfo().remove_book_info()

    elif n.isnumeric() and int(n) not in (1,2,3,4) :
        print("Please enter a valid number for the operation (1, 2, 3, or 4)")

    elif n.isalpha and n.upper() != "EXIT":
        print("If you wish to exit, type 'Exit'. ):(")
        
    else: 
        print("Your operation has been exited. Thank You!!")
        break