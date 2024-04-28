class SevenSegmentDisplay:

    ''' Python implementation of a 7-segment display with 5x5 segments. 
        Each segment is a 5x5 matrix of booleans.    
        The display is a list of 10 segments, one for each digit 0-9.
    '''

    def __init__(self):
        print("Initiating 7-segment display...")
        self.segments = [[[False]*5]*5]*10

    def set_segment(self, segment, state):
        self.segments[segment] = state
        print('Added segment '+ str(segment)+ ' to state')

    def display(self, number):
        for r in range(5):
            row = self.segments[number][r]
            for c in range(5):
                if row[c]:
                    print("%", end="")
                else:
                    print("   ", end="")
            print()