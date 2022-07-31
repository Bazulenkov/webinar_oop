class Transport:
    def __init__(self, fuel) -> None:
        self.fuel = fuel

    # def add_distance(self, dist):
    #     self.distance += dist

    @staticmethod
    def beep():
        print("fa-fa")

    @classmethod
    def class_method(cls, data):
        fuel = data["fuel"]
        result = cls(fuel)
        return result


class Car(Transport):
    pass


if __name__ == "__main__":
    t1 = Transport(50)
    t2 = Transport(100)
    data = {"param1": 2, "fuel": 3, "param3": 4}

    t3 = Transport.class_method(data)
    pass
