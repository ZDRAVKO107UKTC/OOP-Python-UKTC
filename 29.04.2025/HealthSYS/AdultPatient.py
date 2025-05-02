from Patient import Patient
from validator import validate_data

class AdultPatient(Patient):
    @validate_data
    def get_info(self):
        print(f"[ADULT] {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}")
