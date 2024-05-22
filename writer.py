class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, message: str):
        with open(self.file_name, "w") as file:  
            file.write(message)

    def read(self) -> str:
        with open(self.file_name, "r") as file: 
            return file.read()

if __name__ == '__main__':
    def main():
        file_writer = FileWriter("fileWriter.txt")
        file_writer.write("cocacola\n")  
        
        print(file_writer.read())  

    main()
