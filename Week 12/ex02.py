from abc import ABC, abstractmethod
import csv

class FileReader(ABC):
    @abstractmethod
    def read(self):
        pass

class TextFile(FileReader):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

class CSVFile(FileReader):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            return list(reader)

text_file = TextFile('example.txt')
print(text_file.read())

csv_file = CSVFile('example.csv')
print(csv_file.read())