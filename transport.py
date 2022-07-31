class Transport:
    fuel = 100

    def __init__(self, distance) -> None:
        self.distance = distance


class Car(Transport):
    pass


if __name__ == "__main__":
    t1 = Transport(50)
    t2 = Transport(100)
    pass
