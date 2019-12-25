# import only system from os 
from os import system 

FINISH_OP_CODE = 99
ADD_OP_CODE = 1
MULTIPLE_OP_CODE = 2
INPUT_STORE_OP_CODE = 3
OUTPUT_OP_CODE = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8

POSITION_MODE = 0
IMMEDIATE_MODE = 1

PART_1_INPUT_ID = 1
PART_2_INPUT_ID = 5

def add_handler(input_program, op_code_decoded, PC, input_value):
    processed_input = input_program
    first_value = processed_input[processed_input[PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 1]
    second_value = processed_input[processed_input[PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 2]
    store_position = processed_input[PC + 3]
    total = first_value + second_value
    processed_input[store_position] = total
    return { 'program': processed_input, 'PC': PC + 3 + 1 }

def multiply_handler(input_program, op_code_decoded, PC, input_value):
    processed_input = input_program
    first_value = processed_input[processed_input[PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 1]
    second_value = processed_input[processed_input[PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 2]
    store_position = processed_input[PC + 3]
    total = first_value * second_value
    processed_input[store_position] = total
    return { 'program': processed_input, 'PC': PC + 3 + 1}

def input_store_handler(input_program, op_code_decoded, PC, input_value):
    processed_input = input_program
    store_position = processed_input[PC + 1]
    processed_input[store_position] = input_value
    return { 'program': processed_input, 'PC': PC + 1 + 1}

def output_handler(input_program, op_code_decoded, PC, input_value):
    read_position = input_program[PC + 1]
    print(input_program[read_position])
    return { 'program': input_program, 'PC': PC + 1 + 1 }

def jump_if_true_handler(input_program, op_code_decoded, PC, input_value):
    processed_input = input_program
    first_value = processed_input[processed_input[PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 1]
    second_value = processed_input[processed_input[PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 2]
    pc_value = PC + 2 + 1
    if first_value != 0:
        pc_value = second_value
    return { 'program': processed_input, 'PC': pc_value }

def jump_if_false_handler(input_program, op_code_decoded, PC, input_value):
    processed_input = input_program
    first_value = processed_input[processed_input[PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 1]
    second_value = processed_input[processed_input[PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 2]
    pc_value = PC + 2 + 1
    if first_value == 0:
        pc_value = second_value
    return { 'program': processed_input, 'PC': pc_value }

def less_than_handler(input_program, op_code_decoded, PC, input_value):
    processed_input = input_program
    first_value = processed_input[processed_input[PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 1]
    second_value = processed_input[processed_input[PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 2]
    store_position = processed_input[PC + 3]
    processed_input[store_position] = 1 if first_value < second_value else 0
    return { 'program': processed_input, 'PC': PC + 3 + 1 }

def equals_handler(input_program, op_code_decoded, PC, input_value):
    processed_input = input_program
    first_value = processed_input[processed_input[PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 1]
    second_value = processed_input[processed_input[PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else processed_input[PC + 2]
    store_position = processed_input[PC + 3]
    processed_input[store_position] = 1 if first_value == second_value else 0
    return { 'program': processed_input, 'PC': PC + 3 + 1 }

def finish_handler(input_program, op_code_decoded, PC, input_value):
    print("Finished...")
    return { 'program': input_program, 'PC': PC }

OP_CODES = {
    ADD_OP_CODE: {
        'handler': add_handler
    },
    MULTIPLE_OP_CODE: {
        'handler': multiply_handler
    },
    INPUT_STORE_OP_CODE: {
        'handler': input_store_handler
    },
    OUTPUT_OP_CODE: {
        'handler': output_handler
    },
    JUMP_IF_TRUE: {
        'handler': jump_if_true_handler
    },
    JUMP_IF_FALSE: {
        'handler': jump_if_false_handler,
    },
    LESS_THAN: {
        'handler': less_than_handler
    },
    EQUALS: {
        'handler': equals_handler
    },
    FINISH_OP_CODE: {
        'handler': finish_handler,
    }
}

INSTRUCTION_LENGTH = 5

def map_opcode_from_instruction(instruction: str):
    # take last and next to last characters and convert it to integer
    opcode_parts = instruction[-2:]
    opcode_part_int = int(opcode_parts)
    return opcode_part_int

def map_parameter_mode(instruction: str, param_number: int):
    if len(instruction) <= 2:
        return POSITION_MODE
    instruction_padded = instruction.rjust(INSTRUCTION_LENGTH, '0')
    param_modes = instruction_padded[0:3]
    return int(param_modes[len(param_modes) - param_number])

def decode_opcode(input_program, PC):
    instruction = input_program[PC]
    op_code_as_string = str(instruction)
    op_code = map_opcode_from_instruction(op_code_as_string)
    mode_of_first_param = map_parameter_mode(op_code_as_string, 1)
    mode_of_second_param = map_parameter_mode(op_code_as_string, 2)
    mode_of_third_param = map_parameter_mode(op_code_as_string, 3)
    return {
        "OP_CODE": op_code,
        "FIRST_PARAM_MODE": mode_of_first_param,
        "SECOND_PARAM_MODE": mode_of_second_param,
        "THIRD_PARAM_MODE": mode_of_third_param
    }

def run_program(INPUT_VALUE):
    PC = 0
    input_program = [ 3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,34,224,101,-71,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1002,113,50,224,1001,224,-2550,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,13,50,225,102,7,187,224,1001,224,-224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,79,72,225,1101,42,42,225,1102,46,76,224,101,-3496,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,51,90,225,1101,11,91,225,1001,118,49,224,1001,224,-140,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,191,87,224,1001,224,-1218,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1,217,83,224,1001,224,-124,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,32,77,225,1101,29,80,225,101,93,58,224,1001,224,-143,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,45,69,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1108,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,509,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226 ]
    while True:
        decoded_op_code = decode_opcode(input_program, PC)
        current_opcode = decoded_op_code["OP_CODE"]
        handle_function_to_execute = OP_CODES[current_opcode]['handler']
        input_program_after_run = handle_function_to_execute(input_program, decoded_op_code, PC, INPUT_VALUE)
        instructions = input_program_after_run['program']
        PC = input_program_after_run['PC']
        input_program = instructions
        if current_opcode == FINISH_OP_CODE:
            break

def main():
    print('Part 1:')
    run_program(PART_1_INPUT_ID)
    print('End Part 1')
    print('Part 2:')
    run_program(PART_2_INPUT_ID)
    print('End Part 2')

main()