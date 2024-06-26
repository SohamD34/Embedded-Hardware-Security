import numpy as np
import matplotlib.pyplot as plt
from circuits.peripherals import Peripheral, UART, GPIO
from circuits.cpu import CPU
from circuits.clock import rectangular_clock_pulse, triangular_clock_pulse, sawtooth_clock_pulse
from circuits.addons import SevenSegmentDisplay
from circuits.attack import buffer_overflow, pointer_subterfuge


''' CPU and Peripherals '''

cpu = CPU()

uart1 = UART("UART1")
uart2 = UART("UART2")
gpio1 = GPIO("GPIOA")

cpu.attach_peripheral(uart1)
cpu.attach_peripheral(uart2)
cpu.attach_peripheral(gpio1)


# ''' Simulation of instructions '''
# cpu.execute(['add 0x06 0x04 0x05', 'sub 0x07 0x06 0x05'])


# # UART Transmission 

print("\nUART Transmission")
transmitted_data = uart1.handle_interrupt(cpu, rectangular_clock_pulse(1, 0.5, 10000))
print("Transmitted data = ",cpu.data_memory[transmitted_data],"\n")

display = SevenSegmentDisplay()
display.program()
display.display(cpu.data_memory[transmitted_data])

# # UART Reception

print("\nUART Reception")
uart2.receiver(transmitted_data)
print("Recieved data = ",uart2.received_data,"\n")

display = SevenSegmentDisplay()
display.program()
display.display(cpu.data_memory[uart2.received_data])
