class PatientIterator:
    def __init__(self, patients):
        self._patients = patients
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._patients):
            patient = self._patients[self._index]
            self._index += 1
            return patient
        else:
            raise StopIteration
