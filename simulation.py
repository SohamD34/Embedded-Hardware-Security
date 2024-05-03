import numpy as np
import matplotlib.pyplot as plt
from circuits.peripherals import Peripheral, UART, SPI, GPIO
from circuits.cpu import CPU
from circuits.clock import rectangular_clock_pulse, triangular_clock_pulse, sawtooth_clock_pulse
from circuits.addons import SevenSegmentDisplay
from circuits.attack import buffer_overflow, pointer_subterfuge


''' CPU and Peripherals '''

cpu = CPU()

uart1 = UART("UART1")
uart2 = UART("UART2")
spi1 = SPI("SPI1")
gpio1 = GPIO("GPIOA")

cpu.attach_peripheral(uart1)
cpu.attach_peripheral(uart2)
cpu.attach_peripheral(spi1)
cpu.attach_peripheral(gpio1)


# ''' 7-segment display '''
# display = SevenSegmentDisplay()
# display.reset()
# display.program()

# ''' Activating the clock '''
# clock_pulses = rectangular_clock_pulse(1, 0.5, 100)

# ''' Simulation '''
cpu.execute(['add 0x06 0x04 0x05', 'sub 0x07 0x06 0x05'])


# ''' Buffer Overflow Attack '''  
# buffer_overflow(cpu)
# print(cpu.current_address)
# print(cpu.data_memory[cpu.current_address])

''' Pointer Subterfuge Attack '''
print("Before attack:", cpu.instruction_memory)
pointer_subterfuge(cpu)
print("After attack:", cpu.instruction_memory)
print(cpu.add(1,1))