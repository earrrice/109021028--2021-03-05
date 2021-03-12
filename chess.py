class Class:
    def __init__(self,name,colour,front,about,back):
        self.Name=name
        self.Colour=colour
        self.Front=front
        self.About=about
        self.Back=back
    def showInfo(self):
        print(self.Name)
        print(self.Colour)
        print(self.Front)
        print(self.About)
        print(self.Back)
x=Class("將","black","可往前走","可左右走","可往後走")
y=Class("卒","black","可往前走","不可左右走","不可往後走")
z=Class("兵","red","可往前走","不可左右走","不可往後走")

x.showInfo()
y.showInfo()
z.showInfo()