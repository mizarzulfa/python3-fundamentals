def tambah(n1,n2):
    a = n1 + n2
    print(a)


class data:
    def __init__(self) -> None:
        self.anj = tambah(1,1)
        self.unj = tambah(5,1)
    
    def pertambahan(self):
        tambah(12,12)
    
objek = data()

has = objek.pertambahan()

objek.anj
objek.unj