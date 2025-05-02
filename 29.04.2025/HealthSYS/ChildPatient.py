from Patient import Patient
from validator import validate_data

class ChildPatient(Patient):
    @validate_data
    def get_info(self):
        print(f"[CHILD] {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}")
