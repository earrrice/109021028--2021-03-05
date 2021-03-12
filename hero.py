class Hero:
    def __init__(self,nime,id,atk,matk,hp,mp,aspd,cspd):
        self.NAME=name
        self.ID=id
        self.ATK=atk
        self.MATK=matk
        self.HP=hp
        self.MP=mp
        self.ASPD=aspd
        self.CSPD=cspd
def showlnfo():
    print(Hero.__dict__)
    print(Hero.__doc__)
    print(Hero.__name__)
    print(Hero.__module__)
    print(Hero.__bases__)
x=Hero("A","1","2","3","4","5","6","7")
y=Hero("B","10","20","30","40","50","60","70")
z=Hero("C","100","200","300","400","500","600","700")

x.showlnfo