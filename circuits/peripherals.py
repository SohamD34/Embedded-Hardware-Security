class Peripheral:
    def __init__(self, name):
        self.name = name

    def handle_interrupt(self):
        pass


class UART(Peripheral):
    def __init__(self, name):
        super().__init__(name)
        self.transmitted_data = None
        self.received_data = None

    def transmitter(self, data):
        self.transmitted_data = data
        print(f"{self.name}: Transmitting data...")


    def receiver(self, data):
        self.received_data = data
        print(f"{self.name}: Receiving data...")


    def handle_interrupt(self, cpu, clock_pulse):

        print(f"{self.name}: UART handling interrupt...")
        address = input('Enter the address of data to be transmitted: ')
        
        data_for_transmission = cpu.data_memory[address]
        cpu.current_address = address

        for i in clock_pulse:
            if i==1:
                if(int(input("\nWaiting for transmission...")) != 1):
                    print("...")
                else:
                    self.transmitter(data_for_transmission)
                    print("Transmission complete!")
                    break
        return address


class GPIO(Peripheral):
    def __init__(self, name):
        super().__init__(name)

    def handle_interrupt(self, clock_pulse):
        print(f"{self.name}: GPIO handling interrupt...")
        ##
        ## Code to handle interrupt
        ##
        print("Handling complete! Returning to main\n")
