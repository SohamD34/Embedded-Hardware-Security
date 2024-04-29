import time

class SevenSegmentDisplay:

    ''' Python implementation of a 7-segment display with 5x5 segments. 
        Each segment is a 5x5 matrix of booleans.    
        The display is a list of 10 segments, one for each digit 0-9.
    '''

    def __init__(self):
        print("Initiating 7-segment display...")
        self.segments = [[[False]*5]*5]*10
        self.current_state = 0

    def set_segment(self, segment, state):
        self.segments[segment] = state
        print('Added segment '+ str(segment)+ ' to state')

    def display(self, number):
        self.current_state = number
        for r in range(5):
            row = self.segments[number][r]
            for c in range(5):
                if row[c]:
                    print("%", end="")
                else:
                    print("   ", end="")
            print()

    def program(self):
        self.set_segment(0, [[True, True, True, True, True], [True, False, False, False, True], [True, False, False, False, True], [True, False, False, False, True], [True, True, True, True, True]])
        self.set_segment(1, [[False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True]])
        self.set_segment(2, [[True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True], [True, False, False, False, False], [True, True, True, True, True]])
        self.set_segment(3, [[True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True]])
        self.set_segment(4, [[True, False, False, False, True], [True, False, False, False, True], [True, True, True, True, True], [False, False, False, False, True], [False, False, False, False, True]])
        self.set_segment(5, [[True, True, True, True, True], [True, False, False, False, False], [True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True]])
        self.set_segment(6, [[True, True, True, True, True], [True, False, False, False, False], [True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True]])
        self.set_segment(7, [[True, True, True, True, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True], [False, False, False, False, True]])
        self.set_segment(8, [[True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True]])
        self.set_segment(9, [[True, True, True, True, True], [True, False, False, False, True], [True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True]])

    def reset(self):
        self.segments = [[[False]*5]*5]*10

    def get_current_state(self):
        return self.current_state


class UpCounter:
    
    ''' Python implementation of an up counter. 
        The counter is a list of 4 bits.
        The counter increments by 1 on each clock pulse.
    '''

    def __init__(self, clock_pulse, ARR):
        print("Initiating up counter...")
        self.arr = ARR
        self.clock_pulse = clock_pulse
        self.counter = 0

    def step(self):
        for i in self.clock_pulse:
            if i == 1:
                if self.counter == self.arr:    
                    self.counter = 0
                    return
                else:
                    self.counter += 1
            time.sleep(2e10)

    def reset(self):
        self.counter = 0


class DownCounter:
    
    ''' Python implementation of a down counter. 
        The counter is a list of 4 bits.
        The counter decrements by 1 on each clock pulse.
    '''

    def __init__(self, ARR, clock_pulse):
        print("Initiating down counter...")
        self.arr = ARR
        self.counter = ARR
        self.clock_pulse = clock_pulse

    def step(self):
        for i in self.clock_pulse:
            if i == 1:
                if self.counter == 0:    
                    self.counter = self.arr
                else:
                    self.counter -= 1
            time.sleep(2e10)

    def reset(self):
        self.counter = self.arr
