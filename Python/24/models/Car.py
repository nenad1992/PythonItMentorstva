class Car:
    def __init__(self):
        self.__brand = None
        self.__model = None

    # Getter
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        print("Pozvan je setter")
        self.__model = model

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand


audi = Car()
audi.brand = "Test"
print(audi.brand)