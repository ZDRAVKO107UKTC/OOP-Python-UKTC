from AdultPatient import AdultPatient
from ChildPatient import ChildPatient
from iterator import PatientIterator
from generator import adult_patients

patients = [
    AdultPatient("Ivan Petrov", 35, "Diabetes"),
    ChildPatient("Maria Ivanova", 12, "Flu"),
    AdultPatient("Georgi Georgiev", 50, "Hypertension"),
    ChildPatient("Anna Dimitrova", 8, "Asthma")
]

print("=== All patients ===")
for p in PatientIterator(patients):
    p.get_info()

print("\n=== Adult patients only ===")
for p in adult_patients(patients):
    p.get_info()
