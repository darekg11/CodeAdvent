FINISH_OP_CODE = 99
ADD_OP_CODE = 1
MULTIPLE_OP_CODE = 2
DESIRED_VALUE = 19690720 # From Part 2

def run_program(noun, verb):
    PC = 0
    input_program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,9,19,23,1,13,23,27,1,5,27,31,2,31,6,35,1,35,5,39,1,9,39,43,1,43,5,47,1,47,5,51,2,10,51,55,1,5,55,59,1,59,5,63,2,63,9,67,1,67,5,71,2,9,71,75,1,75,5,79,1,10,79,83,1,83,10,87,1,10,87,91,1,6,91,95,2,95,6,99,2,99,9,103,1,103,6,107,1,13,107,111,1,13,111,115,2,115,9,119,1,119,6,123,2,9,123,127,1,127,5,131,1,131,5,135,1,135,5,139,2,10,139,143,2,143,10,147,1,147,5,151,1,151,2,155,1,155,13,0,99,2,14,0,0]
    input_program[1] = noun
    input_program[2] = verb
    while True:
        current_opcode = input_program[PC]
        if current_opcode == FINISH_OP_CODE:
            break
        input_program = process_opcode(input_program, current_opcode, PC)
        PC += 4
    return input_program[0]

def process_opcode(input_program, opcode, PC):
    processed_input = input_program
    first_position = processed_input[PC + 1]
    second_position = processed_input[PC + 2]
    first_value = processed_input[first_position]
    second_value = processed_input[second_position]
    store_position = processed_input[PC + 3]
    if (opcode == ADD_OP_CODE):
        total = first_value + second_value
        processed_input[store_position] = total
    if (opcode == MULTIPLE_OP_CODE):
        total = first_value * second_value
        processed_input[store_position] = total
    return processed_input


def main():
    noun = 0
    verb = 0
    output = 0
    while True:
        output = run_program(noun, verb)
        if (output == DESIRED_VALUE):
            break
        if noun < 100:
            noun += 1
        else:
            noun = 0
            verb += 1
    
    print('Part 2:', 100 * noun + verb)

main()