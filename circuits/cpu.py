import sys
import os

class CPU:
    def __init__(self):
        self.peripherals = []

    def attach_peripheral(self, peripheral):

        print('Adding peripheral - ' + str(peripheral) + '...')
        self.peripherals.append(peripheral)
        print('Peripheral ' + str(peripheral) + ' added successfully!\n')

    def process(self):
        
        print("CPU processing...")
        
        
