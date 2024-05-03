class Peripheral:
    def __init__(self, name):
        self.name = name

    def handle_interrupt(self):
        pass


class UART(Peripheral):
    def __init__(self, name):
        super().__init__(name)

    def handle_interrupt(self, clock_pulse):
        print(f"{self.name}: UART handling interrupt...")
        ##
        ## Code to handle interrupt
        ##
        print("Handling complete! Returning to main\n")


class SPI(Peripheral):
    def __init__(self, name):
        super().__init__(name)

    def handle_interrupt(self, clock_pulse):
        print(f"{self.name}: SPI handling interrupt...")
        ##
        ## Code to handle interrupt
        ##
        print("Handling complete! Returning to main\n")


class GPIO(Peripheral):
    def __init__(self, name):
        super().__init__(name)

    def handle_interrupt(self, clock_pulse):
        print(f"{self.name}: GPIO handling interrupt...")
        ##
        ## Code to handle interrupt
        ##
        print("Handling complete! Returning to main\n")


print("hELLO")