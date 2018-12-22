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
call_map['gtir'] = GTIR
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

    # Part 2 use set to contain mulitle values of reg[4] in my example
    unique_reg_values = set()
    
    # Part 2 - latest
    most_recent_value = 0

    # Program loop
    # note part 2 takes shit lot of time in Pyton3 runner ~ 20 minutes on my i7 two cores
    # running the same thing with pypy took only around 1 minute
    # PLEASE CONSIDER RUNNING THIS IN PYPY
    while program_counter >= 0 and program_counter < len(instructions):
        # get instruction to execute
        instruction_to_execute = instructions[registers[instruction_pointer_register]]
        op_code = instruction_to_execute[0]
        # Part - 1
        # In program input reg[0] is only used in my case at instruction:
        # eqrr 4 0 2
        # It checks if reg[4] == reg[0]
        # also eqrr OP_CODE is only happening once so just stop when OP_COde is 'eqrr'
        # print the register[4] and that is value that reg[0] should be set to stop at most few instructions
        if op_code == 'eqrr':
            if registers[4] not in unique_reg_values:
                if len(unique_reg_values) == 0:
                    # Part 1
                    print(registers[4])
                unique_reg_values.add(registers[4])
                most_recent_value = registers[4]
            else:
                # we have a duplication
                # Print most recent value used for comaprision
                # At that point there is a duplicate so the program had to start again so the last recent value is the lower integer after most of iterations
                print(most_recent_value)
                break
        param_a = instruction_to_execute[1]
        param_b = instruction_to_execute[2]
        output = instruction_to_execute[3]

        # Execute
        registers = call_map[op_code](registers, param_a, param_b, output)
        # update PC
        registers[instruction_pointer_register] += 1
        program_counter = registers[instruction_pointer_register]

main()