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


# Before Attack
print("Before Attack...")
cpu.execute(['add 0x06 0x04 0x05'])


# Pointer Subterfuge Attack 

print("Before attack:", cpu.instruction_memory)
pointer_subterfuge(cpu)
print("After attack:", cpu.instruction_memory)


# Post attack

print("\nAfter attack")
cpu.execute(['add 0x06 0x04 0x05'])