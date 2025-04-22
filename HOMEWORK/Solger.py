class Soldier:
    def __init__(self, name, rank, serial_number):
        self.name = name
        self._rank = rank
        self._serial_number = serial_number

    def get_rank(self):
        return self._rank

    def confirm_serial_number(self, serial_number):
        return self._serial_number == serial_number

    def promote(self, new_rank):
        self._rank = new_rank
        print(f"{self.name} е промотиран на {self._rank}.")

    def demote(self, new_rank):
        self._rank = new_rank
        print(f"{self.name} е понижен на {self._rank}.")

    @staticmethod
    def display_hero_info(soldier):
        print(f"Име: {soldier.name}")
        print(f"Военно звание: {soldier.get_rank()}")
        print(f"Сериен номер: {soldier._serial_number}")


soldier1 = Soldier("Иван Петров", "Сержант", "123456")


Soldier.display_hero_info(soldier1)

print(soldier1.confirm_serial_number("123456"))  # True
print(soldier1.confirm_serial_number("654321"))  # False

soldier1.promote("Лейтенант")

soldier1.demote("Редник")

Soldier.display_hero_info(soldier1)