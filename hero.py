class Hero:
    def __init__(self,name,id,atk,hp,aspd):
        self.NAME=name
        self.ID=id
        self.ATK=atk
        self.HP=hp
        self.ASPD=aspd
    def showInfo(self):
        print(self.NAME)
        print(self.ID)
        print(self.ATK)
        print(self.HP)
        print(self.ASPD)
x=Hero("A","1",2,3,4)
y=Hero("B","10",20,30,40)
z=Hero("C","100",200,300,400)

x.showInfo()
y.showInfo()
z.showInfo()