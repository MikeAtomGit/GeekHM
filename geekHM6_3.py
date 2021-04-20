class Worker():
    _income = {'wage': 0, 'bonus': 0}
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = int(input(f'Enter {self.name}`s wage: '))
        self._income['bonus'] = int(input(f'Enter {self.name}`s bonus: '))
class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} is on position {self. position}')
    def get_total_income(self):
        total_inc = self._income['wage'] + self._income['bonus']
        print(f'Total income is: {total_inc}')

worker_1 = Position('Vasiliy', 'Vasilev', 'Engineer')
worker_2 = Position('Leonid', 'Brezhnev', 'Dictator')
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()
#
