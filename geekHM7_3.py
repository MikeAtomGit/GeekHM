class Cell():
    
    def __init__(self, nucleus_count):        
        self.nucleus_count = nucleus_count

    def __add__(self, other):
        return self.nucleus_count + other.nucleus_count
    
    def __sub__(self, other):
        if self.nucleus_count - other.nucleus_count <= 0:
            print('You can not do that! We do not study antimatter!')
        else:
            return self.nucleus_count - other.nucleus_count

    def __mul__(self, other):
        new_cell_mult = Cell(self.nucleus_count * other.nucleus_count)
        return new_cell_mult.nucleus_count 

    def __truediv__(self, other):
        new_cell_div = Cell(self.nucleus_count / other.nucleus_count)
        return round(new_cell_div.nucleus_count)

cell1 = Cell(30)
cell2 = Cell(50)
print(cell2 + cell1)
print(cell2 - cell1)
print(cell1 - cell2)
print(cell2 * cell1)
print(cell2 / cell1)