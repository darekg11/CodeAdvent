import re
from collections import defaultdict

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

    # Part - 2
    # Let's do it as follow:
    # Create dict from samples in following format:
    # OP_Number = ARRAY('SETI','SETR')
    # 0: [9, ['SETI', 'ADDR']]
    # Do a while loop until we have all operations as unique
    # In each iteration find, sample data that have only 1 OPCODE and map it, skip empty samples
    # At the same time remove that OPCODE from any other samples
    # At the end, print result in form:
    # OP_Number - Function Name
    
    #  This will be a dict of op_number to function_name
    unique_op_table = defaultdict()

    # Create OP_Codes sets from sample data:
    op_sample_table = defaultdict()

    for i in range(0, len(lines) - 2, 3):
        input_data = lines[i]
        instructions_data = lines[i + 1]
        output_data = lines[i + 2]
        op_number = instructions_data[0]
        current_items_under_op_code = op_sample_table.get(op_number)
        if current_items_under_op_code is None:
            current_items_under_op_code = []
            op_sample_table[op_number] = current_items_under_op_code
        available_instructions_for_sample = find_matching_opcodes(input_data, instructions_data, output_data)
        for single_instruction in available_instructions_for_sample:
            if single_instruction not in current_items_under_op_code:
                current_items_under_op_code.append(single_instruction)

    # Transfer dup
    # indicate found OPCode and it can be removed in in iteration so we don't keep on looping
    to_remove_in_iteration = []
    while len(unique_op_table) != len(INSTRUCTIONS):
        # if we have anything to remove, remove it
        for single_item_to_remove in to_remove_in_iteration:
            op_sample_table.pop(single_item_to_remove, None)
        # clear items to remove, jsut for safety
        to_remove_in_iteration = []
        # go through every item
        # so begin with for example 10: ['STRI', MULI'] 
        for op_code_number, possible_functions in op_sample_table.items():
            # Loop every possible function name in that number so it it will be [STRI, MULI]
            for single_possible_function in possible_functions:
                # Current presency is always included, otherwise for function names that appear only once it will be 0
                total_count_of = 1 # always include current op_code_number
                # Now go through every other op_code_number so EVERY one except 10
                for op_code_inner_loop, possible_functions_inner_loop in op_sample_table.items():
                    # So we don't check the same
                    if op_code_inner_loop != op_code_number:
                        if single_possible_function in possible_functions_inner_loop:
                            total_count_of += 1
                # If by the end of the loop, the number of STRI or MULI is still 1 that means it only is present in once op_number
                if total_count_of == 1:
                    unique_op_table[op_code_number] = single_possible_function
                    # mark op_number where it onlt exist as to remove so we don't try to loop it again
                    # so 10 will be removed from array
                    to_remove_in_iteration.append(op_code_number)
    # Yupii - OP Codes
    print(unique_op_table)

    # Okay, now load test program instructions
    program = getLinesFromFile('test-program.txt')
    # registers start as 0, 0, 0, 0
    registers = [0, 0, 0, 0]
    for single_instruction in program:
        function_to_execute = single_instruction[0]
        input_a = single_instruction[1]
        input_b = single_instruction[2]
        output = single_instruction[3]
        function_name = unique_op_table.get(function_to_execute)
        function_index = 0
        for i in range(len(INSTRUCTIONS)):
            if INSTRUCTIONS[i].__name__ == function_name:
                function_index = i
                break
        registers = INSTRUCTIONS[function_index](registers, input_a, input_b, output)

    # Part 2 - print registers 0 value
    print(registers[0])

main()