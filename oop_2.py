class Exchange:
    def __init__(self, k=0):
        self.__k = k

    @property
    def kg(self):
        return self.__k

    @kg.setter
    def kg(self, k):
        if isinstance(k, (int, float)):
            self.__k = k
        else:
            print("Килограммы задаются только числами")


    def to_pounds(self):
        return self.__k * 2.205


ex = Exchange(12)
print(ex.kg, "кг => ", end="")
print(ex.to_pounds(), "фунтов")
































