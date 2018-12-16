import re

def getLinesFromFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    data = [[int(singleValue) for singleValue in re.findall(r'-?\d+', singleLine)] for singleLine in lines if singleLine != '\n']
    return data

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

INSTRUCTIONS = [
    ADDR, ADDI,
    MULR, MULI,
    BANR, BANI,
    BORR, BORI,
    SETR, SETI,
    GTIR, GTRI, GTRR,
    EQIR, EQRI, EQRR
]

def find_matching_opcodes(input, instructions, output):
    # set so we can avoid having duplicates of the same instruction
    matching_instructions = set()
    for single_instruction in INSTRUCTIONS:
        # 0 is always OP Number which is not used in this case
        params_of_call = instructions[1:]
        returned_value = single_instruction(input, *params_of_call)
        if returned_value == output:
            matching_instructions.add(single_instruction.__name__)
    return matching_instructions

def main():
    # Parse the input, output are arrays - skipped the empty lines, each line is conveted to array
    lines = getLinesFromFile('sample-data.txt')
    # count of samples that cover 3 or more opcodes
    total_samples = 0
    # Part - 1
    for i in range(0, len(lines) - 2, 3):
        input_data = lines[i]
        instructions_data = lines[i + 1]
        output_data = lines[i + 2]
        if len(find_matching_opcodes(input_data, instructions_data, output_data)) >= 3:
            total_samples += 1
    print(total_samples)
main()