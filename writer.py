class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.file = open(self.file_name, "r+")  
        except FileNotFoundError:  
            self.file = open(self.file_name, "w+")  

    def write(self, message: str):
        self.file.write(message)
        self.file.flush()  
    def read(self) -> str:
        self.file.seek(0)  
        return self.file.read()

    def readlines(self) -> list:
        self.file.seek(0)  
        return self.file.readlines()

    def close(self):
        self.file.close()


if __name__ == '__main__':
    def main():
        file_writer = FileWriter("fileWriter.txt")
        file_writer.write("cocacola\n")  
        
        file_writer.close()
        
        file_reader = FileWriter("fileWriter.txt")
        print(file_reader.read())  
        file_reader.close()

    main()
