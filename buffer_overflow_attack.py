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


# UART Transmission 

print("UART Transmission")
transmitted_data = uart1.handle_interrupt(cpu, rectangular_clock_pulse(1, 0.5, 10000))
print("Transmitted data = ", cpu.data_memory[transmitted_data],"\n")

display = SevenSegmentDisplay()
display.program()
display.display(cpu.data_memory[transmitted_data])


# Buffer Overflow Attack

print("\nTransmitted data address =", cpu.current_address)
buffer_overflow(cpu)
print("Recieved data address =", cpu.current_address)


# UART Reception

print("\nUART Reception")
uart2.receiver(cpu.data_memory[cpu.current_address])
print("Recieved data = ",uart2.received_data)