class RemoveBook:
    def __init__(self,title,book_id):
        self.title = title
        self.book_id = book_id
    def remove_book(self):
        try:
            with open("Book_Store.txt",'r') as f:
                lines = f.readlines()
                new_lines =[]
                found=False
                i =0
                while i<len(lines):
                    if lines[i].startswith("Title") and self.title in lines[i]:
                        if i+2<len(lines) and lines[i+2].startswith("Book ID") and self.book_id in lines[i+2]:
                            found = True
                            i+=6
                            continue
                    new_lines.append(lines[i])
                    i+=1
                
                if found:
                    with open ("Book_Store.txt","w") as file:
                        file.writelines(new_lines)
                        print(f"Book '{self.title}' with ID {self.book_id} has been removed.")
                        print("\n<!-------- Removed -------->")

                else:
                    print(f"The information for '{self.title}' is not found.")
        except FileNotFoundError:
            print("Book storage file not found!")

class  RemoveBookInfo:
    def remove_book_info(self):
        title= input("Please enter the 'Book name' you wish to delete: ")
        book_id= input("Please enter the 'Book ID' you wish to delete: ")
        remove= RemoveBook(title, book_id)
        remove.remove_book()