import random

def buffer_overflow(cpu):
    last_address = [i for i in cpu.data_memory][-1]
    new_address = hex(int(last_address, 16) + 4)
    cpu.current_address = new_address


def pointer_subterfuge(cpu):
    
    all_instructions = cpu.instruction_memory
    all_addresses = [i for i in cpu.data_memory]

    function1_address, function2_address = random.randint(0, len(all_instructions) - 1), 0
    while(function1_address == function2_address):
        function2_address = random.randint(0, len(all_instructions) - 1)
    
    temp = all_instructions[function1_address]
    cpu.instruction_memory[function1_address], cpu.instruction_memory[function2_address] = cpu.instruction_memory[function2_address], temp

    func1 = all_instructions[function1_address]
    func2 = all_instructions[function2_address]
    
    print("Function 1: " + func1)
    print("Function 2: " + func2)

    temp = getattr(cpu, func1)
    setattr(cpu, func1, getattr(cpu, func2))
    setattr(cpu, func2, temp)

