# import only system from os 
from os import system 
from itertools import permutations 

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

INSTRUCTION_LENGTH = 5

class Computer:
    def __init__(self, program, inputs):
        self.program = program[:]
        self.inputs = inputs
        self.outputs = []
        self.PC = 0
        self.OP_CODES = {
            ADD_OP_CODE: {
                'handler': self.add_handler
            },
            MULTIPLE_OP_CODE: {
                'handler': self.multiply_handler
            },
            INPUT_STORE_OP_CODE: {
                'handler': self.input_store_handler
            },
            OUTPUT_OP_CODE: {
                'handler': self.output_handler
            },
            JUMP_IF_TRUE: {
                'handler': self.jump_if_true_handler
            },
            JUMP_IF_FALSE: {
                'handler': self.jump_if_false_handler,
            },
            LESS_THAN: {
                'handler': self.less_than_handler
            },
            EQUALS: {
                'handler': self.equals_handler
            },
            FINISH_OP_CODE: {
                'handler': self.finish_handler,
            }
        }

    def map_opcode_from_instruction(self, instruction: str):
        # take last and next to last characters and convert it to integer
        opcode_parts = instruction[-2:]
        opcode_part_int = int(opcode_parts)
        return opcode_part_int

    def map_parameter_mode(self, instruction: str, param_number: int):
        if len(instruction) <= 2:
            return POSITION_MODE
        instruction_padded = instruction.rjust(INSTRUCTION_LENGTH, '0')
        param_modes = instruction_padded[0:3]
        return int(param_modes[len(param_modes) - param_number])

    def decode_opcode(self):
        instruction = self.program[self.PC]
        op_code_as_string = str(instruction)
        op_code = self.map_opcode_from_instruction(op_code_as_string)
        mode_of_first_param = self.map_parameter_mode(op_code_as_string, 1)
        mode_of_second_param = self.map_parameter_mode(op_code_as_string, 2)
        mode_of_third_param = self.map_parameter_mode(op_code_as_string, 3)
        return {
            "OP_CODE": op_code,
            "FIRST_PARAM_MODE": mode_of_first_param,
            "SECOND_PARAM_MODE": mode_of_second_param,
            "THIRD_PARAM_MODE": mode_of_third_param
        }

    def add_handler(self, op_code_decoded):
        first_value = self.program[self.program[self.PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 1]
        second_value = self.program[self.program[self.PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 2]
        store_position = self.program[self.PC + 3]
        total = first_value + second_value
        self.program[store_position] = total
        self.PC += 4

    def multiply_handler(self, op_code_decoded):
        first_value = self.program[self.program[self.PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 1]
        second_value = self.program[self.program[self.PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 2]
        store_position = self.program[self.PC + 3]
        total = first_value * second_value
        self.program[store_position] = total
        self.PC += 4

    def input_store_handler(self, op_code_decoded):
        store_position = self.program[self.PC + 1]
        self.program[store_position] = self.inputs.pop(0)
        self.PC += 2

    def output_handler(self, op_code_decoded):
        read_position = self.program[self.PC + 1]
        self.outputs.append(self.program[read_position])
        self.PC += 2

    def jump_if_true_handler(self, op_code_decoded):
        first_value = self.program[self.program[self.PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 1]
        second_value = self.program[self.program[self.PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 2]
        self.PC = second_value if first_value != 0 else self.PC + 3

    def jump_if_false_handler(self, op_code_decoded):
        first_value = self.program[self.program[self.PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 1]
        second_value = self.program[self.program[self.PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 2]
        self.PC = second_value if first_value == 0 else self.PC + 3

    def less_than_handler(self, op_code_decoded):
        first_value = self.program[self.program[self.PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 1]
        second_value = self.program[self.program[self.PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 2]
        store_position = self.program[self.PC + 3]
        self.program[store_position] = 1 if first_value < second_value else 0
        self.PC += 4

    def equals_handler(self, op_code_decoded):
        first_value = self.program[self.program[self.PC + 1]] if op_code_decoded['FIRST_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 1]
        second_value = self.program[self.program[self.PC + 2]] if op_code_decoded['SECOND_PARAM_MODE'] == POSITION_MODE else self.program[self.PC + 2]
        store_position = self.program[self.PC + 3]
        self.program[store_position] = 1 if first_value == second_value else 0
        self.PC += 4

    def finish_handler(self, op_code_decoded):
        return

    def run_program(self, inputs):
        self.inputs += inputs
        while True:
            decoded_op_code = self.decode_opcode()
            current_opcode = decoded_op_code["OP_CODE"]
            handle_function_to_execute = self.OP_CODES[current_opcode]['handler']
            handle_function_to_execute(decoded_op_code)
            if current_opcode == OUTPUT_OP_CODE:
                return self.outputs.pop()
            if current_opcode == FINISH_OP_CODE:
                break
        return None

def run(program, feedback_loop_enabled):
    # Every output signal from AMP E
    output_signals = []
    # Choose based on whatever it's part 1 or part 2
    phase_settings_combinations = list(permutations(range(0, 5))) if feedback_loop_enabled is False else list(permutations(range(5, 10)))
    for single_combination in phase_settings_combinations:
        # Create 5 AMPs
        computers = [ Computer(program, [ single_phase ]) for single_phase in single_combination ]
        # First input is always 0 for AMP A
        output_signal = 0
        if feedback_loop_enabled is False:
            # Just run A->B->C->D->E and add to list
            for single_computer in computers:
                output_signal = single_computer.run_program([ output_signal ])
            output_signals.append(output_signal)
        else:
            # None is returned when AMP returned because of HALT so until every one halted continue to work
            # Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving and sending signals until it halts.
            # outpupt_signal is not going to be None when output OP Code is executed
            # We start with 0 so it is going to begin correctly
            while output_signal is not None:
                output_signals.append(output_signal)
                for single_computer in computers:
                    output_signal = single_computer.run_program([ output_signal ])

    # Always choose greatest signal
    return max(output_signals)

def main():
    program = [ 3,8,1001,8,10,8,105,1,0,0,21,42,67,84,109,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,4,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99 ]
    print('Part 1:', run(program, False))
    print('Part 2:', run(program, True))

main()