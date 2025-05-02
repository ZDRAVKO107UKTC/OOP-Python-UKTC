def adult_patients(patients):
    for patient in patients:
        if patient.age >= 18:
            yield patient
