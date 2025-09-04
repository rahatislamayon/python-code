class student_marks:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
    


pass1=student_marks(90,80,70)
print(pass1.percentage)

pass1.phy=74
print(pass1.percentage)
