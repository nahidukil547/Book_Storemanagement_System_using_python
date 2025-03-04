class ReadBook:
    def read_store(self):
        with open ("Book_Store.txt","r") as f:
            read = f.read()
            if "Title" not in read:
                print("The Book Store is empty!!")
            else:
                print(read)


