class Road():
    _length = 0
    _width = 0
    def mass_calculation(self):
        mass_per_cm = 25
        cm = 7
        total_mass = self._length * self._width * mass_per_cm * cm
        print(f'Needed mass is {total_mass} kilos')
sector_1 = Road()
sector_1._length = int(input('Enter desired length: '))
sector_1._width = int(input('Enter desired width: '))
sector_1.mass_calculation()
#