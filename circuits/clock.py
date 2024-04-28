import numpy as np
import matplotlib.pyplot as plt
import time

def rectangular_clock_pulse(frequency, duty_cycle, duration): 

    period = 1 / frequency
    time_values = np.linspace(-0.1, duration, num=200*duration)
    clock_pulse = np.where(np.mod(time_values, period) < period * duty_cycle, 1, 0)

    plt.figure(figsize=(2*duration, 4))
    plt.plot(time_values, clock_pulse)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Rectangular Clock Pulse')
    plt.xlim(-0.1, duration*period)
    plt.ylim(-0.1, 1.1)
    plt.show()

    return clock_pulse



def triangular_clock_pulse(frequency, duration): 

    period = 1 / frequency
    time_values = np.linspace(-0.1, duration, num=200*duration)
    clock_pulse = np.abs(np.mod(time_values, period) - period/2) / (period/2)

    plt.figure(figsize=(2*duration, 4))
    plt.plot(time_values, clock_pulse)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Triangular Clock Pulse')
    plt.xlim(-0.1, duration*period)
    plt.ylim(-0.1, 1.1)
    plt.show()

    return clock_pulse



def sawtooth_clock_pulse(frequency, duration): 

    period = 1 / frequency
    time_values = np.linspace(-0.1, duration, num=200*duration)
    clock_pulse = np.mod(time_values, period) / period

    plt.figure(figsize=(2*duration, 4))
    plt.plot(time_values, clock_pulse)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Sawtooth Clock Pulse')
    plt.xlim(-0.1, duration*period)
    plt.ylim(-0.1, 1.1)
    plt.show()

    return clock_pulse


def time_interval(frequency, duration): 
    time_values = np.linspace(-0.1, duration, num=200*duration)
    return time_values