from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self):
        pass

class SBI(RBI):
    def show(self):
        print("This Is SBI")
    def roi(self):
        print("Rate Of Interest Given By SBI Is : ",6.5)

class ICICI(RBI):
    def show(self):
        print("This Is ICICI")
    def roi(self):
        print("Rate Of Interest Given By ICICI Is : ",7.0)

s1=SBI()
s1.show()
s1.roi()

i1=ICICI()
i1.show()
i1.roi()
