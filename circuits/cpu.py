import sys
import os

class CPU:
    def __init__(self):
        self.peripherals = []

    def add(a, b):
        return a+b

    def sub(a, b):
        return a-b

    def mul(a, b):
        return a*b

    def div(a, b):
        return a/b

    def attach_peripheral(self, peripheral):
        print('Adding peripheral - ' + str(peripheral) + '...')
        self.peripherals.append(peripheral)
        print('Peripheral ' + str(peripheral) + ' added successfully!\n')


    def process(self, device, clock_pulse):
        print("CPU processing...")
        
        for i in clock_pulse:
            if i == 1:
                current_state = device.get_current_state()
                print("Current state: " + str(current_state))
                new_state = current_state + 1
                if(new_state <= 9):
                    device.display(new_state)
            print("\n")

        print("CPU processing completed!\n")
