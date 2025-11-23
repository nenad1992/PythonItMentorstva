class Car:
    VALID_CARS = {
        "Audi": [
            {"model": "A4", "production_year": 2004, "rented": True, "rented_until": None},
            {"model": "A5", "production_year": 2003, "rented": False, "rented_until": None},
            {"model": "A6", "production_year": 2002, "rented": False, "rented_until": None},
        ],
        "BMW": [
            {"model": "M5", "production_year": 2010, "rented": False, "rented_until": None},
            {"model": "M3", "production_year": 2008, "rented": False, "rented_until": None},
        ],
        "Mercedes": [
            {"model": "GLK", "production_year": 2015, "rented": False, "rented_until": None},
            {"model": "GLE", "production_year": 2017, "rented": False, "rented_until": None},
        ],
    }

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
