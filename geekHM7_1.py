class Matrix():
    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
    def __str__(self):
        return f"{' '.join(self.row1)}\n{' '.join(self.row2)}\n{' '.join(self.row3)}"
    def __add__(self, other):
        return f'{" ".join([str(int(el1) + int(el2)) for el1, el2 in zip(self.row1, other.row1)])}\n\
{" ".join([str(int(el1) + int(el2)) for el1, el2 in zip(self.row2, other.row2)])}\n\
{" ".join([str(int(el1) + int(el2)) for el1, el2 in zip(self.row3, other.row3)])}'
            
            

            
            
m1 = Matrix(input('Enter first row: ').split(),
    input('Enter second row: ').split(),
    input('Enter third row: ').split())
print(f'Matrix one: \n{m1}')
m2 = Matrix(input('Enter first row: ').split(),
    input('Enter second row: ').split(),
    input('Enter third row: ').split())
print(f'Matrix two: \n{m2}')
print(f'The sum of matrixes equals:\n{m1 + m2}')