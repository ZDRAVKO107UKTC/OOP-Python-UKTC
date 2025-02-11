class Patient:
    def __init__(self, name, room_number):
        self._name = name
        self.room_number = room_number
        self.temperatures = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("Name must be a string of alphabetic characters.")
        self._name = value

    def add_temperature(self, temperature):
        if self.valid_temperature(temperature):
            self.temperatures.append(temperature)
        else:
            raise ValueError("Temperature must be between 35 and 40 degrees.")

    def mid_temperature(self):
        if len(self.temperatures) == 0:
            return None
        return sum(self.temperatures) / len(self.temperatures)

    @staticmethod
    def valid_temperature(temperature):
        return 35 <= temperature <= 40

    @classmethod
    def create_patient(cls):
        patient_input = input("Enter name and room number (e.g., 'Ivan Petrov 101'): ")
        name, room_number = patient_input.rsplit(' ', 1)
        return cls(name.strip(), int(room_number))


# Example usage
try:
    patient1 = Patient.create_patient()
    patient1.add_temperature(37.5)
    patient1.add_temperature(38.2)
    patient1.add_temperature(39.1)

    print(f"Patient's name: {patient1.name}")
    print(f"Room number: {patient1.room_number}")
    print(f"Mid temperature: {patient1.mid_temperature()}")

    for temperature in patient1.temperatures:
        if Patient.valid_temperature(temperature):
            print(f"Temperature: {temperature}")
        else:
            print(f"Invalid temperature: {temperature}")

    patient2 = Patient.create_patient()
    patient2.add_temperature(36.8)
    patient2.add_temperature(37.0)
    patient2.add_temperature(37.5)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")