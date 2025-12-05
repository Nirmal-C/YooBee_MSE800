class FileOperations:
    # Open File for appending
    def open(self, file_name):
        return open(file_name, "a", encoding="utf-8")  
    
    # Write to the opened file
    def write(self, file_object):
        file_object.write("End of File\n")
        

data = FileOperations()

if __name__ == "__main__":
    file_name = input("File Name: ")
            
    file_object = data.open(file_name)  # opened in append mode

    data.write(file_object)  # writes to file

    file_object.close()
