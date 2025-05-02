from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    @abstractmethod
    def get_info(self):
        pass
