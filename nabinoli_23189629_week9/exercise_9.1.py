class Vehicle:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__state = "stopped"

    def move(self):
        print("I am moving!")
        self.__state = "moving"

    def stop(self):
        print("I now stopped.")
        self.__state = "stopped"

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def __str__(self):
        return f"{self.get_make()} {self.get_model()} is {self.get_state()}."


class Bus(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.set_state("Not in use")
        self.__route = ["New Street", "Bullring", "Moor Street", "BCU"]
        self.__stop_index = 0

    def get_route(self):
        return " - ".join(self.__route)

    def move(self):
        previous_stop = self.__route[self.__stop_index]
        if self.__stop_index < len(self.__route) - 1:
            next_stop = self.__route[self.__stop_index + 1]
            print(f"The bus was at {previous_stop} and is moving to {next_stop}.")
            self.__stop_index += 1
            self.set_state(next_stop)
        else:
            print("I am finished for today!")

    def stop(self):
        print("I am a non-stop bus.")


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.__doors_no = doors

    def set_doors_no(self, number):
        self.__doors_no = number

    def get_doors_no(self):
        return self.__doors_no

    def __str__(self):
        return f"{self.get_make()} {self.get_model()} with {self.get_doors_no()} doors is {self.get_state()}."
