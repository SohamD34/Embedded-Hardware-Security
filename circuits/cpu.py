import sys
import os
os.chdir('E:\IIT Jodhpur\Embedded Systems\Course Project\Embedded-Hardware-Security\circuits')

class CPU:
    def __init__(self):
        self.peripherals = []
        self.instruction_memory = ['add', 'sub', 'mul', 'div']
        self.data_memory =  {   '0x00' : 0, '0x04' : 1, '0x05' : 2,
                                '0x06' : 3, '0x07' : 4, '0x08' : 5, 
                                '0x09' : 6, '0x0a' : 7, '0x0b' : 8,
                                '0x0c' : 9, '0x0d' : 10,
                                '0x0e' : 11, '0x0f' : 12,
                                '0x10' : 13, '0x11' : 14,
                                '0x12' : 15, '0x13' : 16,
                                '0x14' : 17, '0x15' : 18,
                                '0x16' : 19, '0x17' : 20,
                                '0x18' : 21, '0x19' : 22,
                                '0x1a' : 23, '0x1b' : 24 }
        self.current_address = '0x00'



    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
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
                new_state = current_state + 1
                if(new_state <= 9):
                    device.display(new_state)

        print("CPU processing completed!\n")




    def execute(self, instruction_list):
        data_memory = self.data_memory
        instruction_memory = self.instruction_memory

        print("\nExecuting instructions...")

        for instruction in instruction_list:

            instruction = instruction.split(' ')
            operation = instruction[0]
            destination = instruction[1]
            operand1 = data_memory[instruction[2]]
            operand2 = data_memory[instruction[3]]

            if operation == 'add':
                result = self.add(operand1, operand2)
                print("add operation completed.")

            elif operation == 'sub':
                result = self.sub(operand1, operand2)
                print("sub operation completed.")

            elif operation == 'mul':
                result = self.mul(operand1, operand2)
                print("mul operation completed.")

            elif operation == 'div':
                result = self.div(operand1, operand2)
                print("div operation completed.")

            data_memory[destination] = result
            print("Result: " + str(result) + " stored in " + destination + "\n")

        print("Execution completed!\n")


    def get_current_state(self):
        return self.current_address

        