class FileOperations:
    def open(self, file_name):
        return open(file_name, "r", encoding="utf-8")  

    def read(self, file_object):
        return file_object.read()

    def count_asteriks(self, content):
        count = 0
        for line in content.splitlines():
            count += line.count("*")
        return count
        

data = FileOperations()

if __name__ == "__main__":
    while True:
        try:
            file_name = input("File Name: ")
            
            file_object = data.open(file_name)  
            content = data.read(file_object)    

            total_asterisks = data.count_asteriks(content)
            print(f"Total asterisks (*): {total_asterisks}")

            break

        except FileNotFoundError:
            print("File not found.")
