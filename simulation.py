import numpy as np
import matplotlib.pyplot as plt
from circuits.peripherals import Peripheral, UART, SPI, GPIO
from circuits.cpu import CPU
from circuits.clock import rectangular_clock_pulse, triangular_clock_pulse, sawtooth_clock_pulse
from circuits.addons import SevenSegmentDisplay


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


''' 7-segment display '''

display = SevenSegmentDisplay()
display.set_segment(0, [[True, True, True, True, True], [True, False, False, False, True], [True, False, False, False, True], [True, False, False, False, True], [True, True, True, True, True]])
display.set_segment(1, [[False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True]])
display.set_segment(2, [[True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True], [True, False, False, False, False], [True, True, True, True, True]])
display.set_segment(3, [[True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True]])
display.set_segment(4, [[True, False, False, False, True], [True, False, False, False, True], [True, True, True, True, True], [False, False, False, False, True], [False, False, False, False, True]])
display.set_segment(5, [[True, True, True, True, True], [True, False, False, False, False], [True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True]])
display.set_segment(6, [[True, True, True, True, True], [True, False, False, False, False], [True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True]])
display.set_segment(7, [[True, True, True, True, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True]])
display.set_segment(8, [[True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True]])
display.set_segment(9, [[True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True]])


''' Activating the clock '''

clock_pulses = rectangular_clock_pulse(1, 0.5, 100)

cpu.process()