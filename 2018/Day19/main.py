from collections import defaultdict

def get_instruction_pointer_from_data(filename):
    file = open(filename, 'r')
    first_line = file.readline()
    file.close()
    splitted = first_line.split()
    return int(splitted[1])

def get_instructions_from_data(filename):
    file = open(filename, 'r')
    all_lines = file.readlines()
    file.close()
    all_instructions = []
    # Skip first line
    for cnt in range(1, len(all_lines)):
        splitted = all_lines[cnt].split()
        op_code = splitted[0]
        param_a = int(splitted[1])
        param_b = int(splitted[2])
        param_c = int(splitted[3])
        all_instructions.append((op_code, param_a, param_b, param_c))
    return all_instructions

def ADDR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] + copy_registers[input_b]
    return copy_registers

def ADDI(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] + input_b
    return copy_registers

def MULR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] * copy_registers[input_b]
    return copy_registers

def MULI(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] * input_b
    return copy_registers

def BANR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] & copy_registers[input_b]
    return copy_registers

def BANI(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] & input_b
    return copy_registers

def BORR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] | copy_registers[input_b]
    return copy_registers

def BORI(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a] | input_b
    return copy_registers

def SETR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = copy_registers[input_a]
    return copy_registers

def SETI(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = input_a
    return copy_registers

def GTIR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = 1 if input_a > copy_registers[input_b] else 0
    return copy_registers

def GTRI(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = 1 if copy_registers[input_a] > input_b else 0
    return copy_registers

def GTRR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = 1 if copy_registers[input_a] > copy_registers[input_b] else 0
    return copy_registers

def EQIR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = 1 if input_a == copy_registers[input_b] else 0
    return copy_registers

def EQRI(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = 1 if copy_registers[input_a] == input_b else 0
    return copy_registers

def EQRR(current_register_values, input_a, input_b, output):
    copy_registers = current_register_values[:]
    copy_registers[output] = 1 if copy_registers[input_a] == copy_registers[input_b] else 0
    return copy_registers

call_map = defaultdict()
call_map['addr'] = ADDR
call_map['addi'] = ADDI
call_map['mulr'] = MULR
call_map['muli'] = MULI
call_map['banr'] = BANR
call_map['bani'] = BANI
call_map['borr'] = BORR
call_map['bori'] = BORI
call_map['setr'] = SETR
call_map['seti'] = SETI
call_map['gtir'] = GTRI
call_map['gtri'] = GTRI
call_map['gtrr'] = GTRR
call_map['eqir'] = EQIR
call_map['eqri'] = EQRI
call_map['eqrr'] = EQRR

def main():
    # Get Instruction Pointer Reg Index
    instruction_pointer_register = get_instruction_pointer_from_data('test-program.txt')

    # Parse the data into format:
    #OP_CODE Param_A Param_B Param_C
    instructions = get_instructions_from_data('test-program.txt')

    # PC - program counter
    program_counter = 0

    # Registers
    registers = [0, 0, 0, 0, 0, 0]

    # Program loop
    while program_counter >= 0 and program_counter < len(instructions):
        # get instruction to execute
        instruction_to_execute = instructions[registers[instruction_pointer_register]]
        op_code = instruction_to_execute[0]
        param_a = instruction_to_execute[1]
        param_b = instruction_to_execute[2]
        output = instruction_to_execute[3]

        # Execute
        registers = call_map[op_code](registers, param_a, param_b, output)
        # update PC
        registers[instruction_pointer_register] += 1
        program_counter = registers[instruction_pointer_register]

    # Part 1 - print reg 0
    print(registers[0])

    # Part 2 - copy paste but start with value 1
    # This will go on for a really logn period of time so we need something better than bruteforcing
    program_counter = 0
    registers = [1, 0, 0, 0, 0, 0]
    looper = 0
    # Program loop
    # UNCOMMENT WHILE BLOCK TO UNDERSTAND WHAT IS GOING ON
    # while program_counter >= 0 and program_counter < len(instructions):
    #     # if registers[instruction_pointer_register] == 1:
    #     #     print (sum([x for x in range(1, registers[5]+1) if registers[5] % x == 0]))
    #     #     break
    #     # get instruction to execute
    #     instruction_to_execute = instructions[registers[instruction_pointer_register]]
    #     # Let's check what is in registers and instruction that is suppose to execute
    #     if looper % 400_000 == 0:
    #         # Stop it manually when you notice the pattern
    #         print(instruction_to_execute, registers)
    #     # there is a loop going on from instruction 3 - 11
    #     op_code = instruction_to_execute[0]
    #     param_a = instruction_to_execute[1]
    #     param_b = instruction_to_execute[2]
    #     output = instruction_to_execute[3]

    #     # Execute
    #     registers = call_map[op_code](registers, param_a, param_b, output)
    #     # update PC
    #     registers[instruction_pointer_register] += 1
    #     program_counter = registers[instruction_pointer_register]
    #     looper += 1

    # What Part 2 is actually doing:
    # instruction 3 - 11 is actually a loop
    # r[5] stores some really big number, for me it was 10551296
    # r[2] goes is outter loop like for i = 1; i <= r5 which is 10551296 for me
    # r[3] is an inner loop going for j = 1; j <= r5 which is 10551296 for me
    # inside the inner loop this is going on: if r[2] * r[3] == r[5] then r[0] += r[2]
    # so what it is really doing is trying to find sum of every number that divides r[5] with 0 leftover aka modulo aka r[5] % x == 0

    # Actual Part 2
    # for explanation, read above!
    my_input = 10551296
    sum_of_every_number = sum([i for i in range(1, my_input + 1) if my_input % i == 0])
    print(sum_of_every_number)
main()