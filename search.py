class Searching:
    def __init__(self,title):
        self.title =title
    
    def search_book(self):
        try:
            
            with open ("Book_Store.txt","r") as f:
                file= f.readlines()
                if self.title not in file:
                    print("\nInvalid book name. Kindly enter a valid book name. Thank you!!")
            new_file =[]
            i = 0
            while i < len(file) :
                if file[i].startswith("Title")  and self.title in file[i]:
                    for j in range(i,i+7):
                        if j <len(file):
                            new_file.append(file[j]) 
                i+=1
            final_view=''.join(new_file)
            print(final_view)
            print("\n<!-------- Here is Your info -------->")

        except FileNotFoundError:
            print("Invalid book!! kindly search for another book.")

class SearchingInfo:
    def search_book_info(self):
        title = input("Please enter the name of the book you want: ")
        view= Searching(title)
        view.search_book()

