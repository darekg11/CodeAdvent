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
SET_RELATIVE_BASE = 9

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

PART_1_INPUT_ID = 1
PART_2_INPUT_ID = 5

INSTRUCTION_LENGTH = 5

MEMORY_SIZE = 100000

class Computer:
    def __init__(self, program, inputs):
        self.program = program[:]
        self.program += [0] * MEMORY_SIZE
        self.inputs = inputs
        self.outputs = []
        self.PC = 0
        self.relative_base_offset = 0
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
            SET_RELATIVE_BASE: {
                'handler': self.set_relative_base_handler
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

    def get_index_of_value(self, param_name, index_value):
        if param_name == POSITION_MODE:
            return self.program[self.PC + index_value]
        elif param_name == RELATIVE_MODE:
            return self.relative_base_offset + self.program[self.PC + index_value]
        else:
            return self.PC + index_value

    def add_handler(self, op_code_decoded):
        first_value = self.program[self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)]
        second_value = self.program[self.get_index_of_value(op_code_decoded['SECOND_PARAM_MODE'], 2)]
        store_position = self.get_index_of_value(op_code_decoded['THIRD_PARAM_MODE'], 3)
        total = first_value + second_value
        self.program[store_position] = total
        self.PC += 4

    def multiply_handler(self, op_code_decoded):
        first_value = self.program[self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)]
        second_value = self.program[self.get_index_of_value(op_code_decoded['SECOND_PARAM_MODE'], 2)]
        store_position = self.get_index_of_value(op_code_decoded['THIRD_PARAM_MODE'], 3)
        total = first_value * second_value
        self.program[store_position] = total
        self.PC += 4

    def input_store_handler(self, op_code_decoded):
        store_position = self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)
        self.program[store_position] = self.inputs.pop(0)
        self.PC += 2

    def output_handler(self, op_code_decoded):
        value_index = self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)
        value = self.program[value_index]
        print(value)
        self.outputs.append(value)
        self.PC += 2

    def jump_if_true_handler(self, op_code_decoded):
        first_value = self.program[self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)]
        second_value = self.program[self.get_index_of_value(op_code_decoded['SECOND_PARAM_MODE'], 2)]
        self.PC = second_value if first_value != 0 else self.PC + 3

    def jump_if_false_handler(self, op_code_decoded):
        first_value = self.program[self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)]
        second_value = self.program[self.get_index_of_value(op_code_decoded['SECOND_PARAM_MODE'], 2)]
        self.PC = second_value if first_value == 0 else self.PC + 3

    def less_than_handler(self, op_code_decoded):
        first_value = self.program[self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)]
        second_value = self.program[self.get_index_of_value(op_code_decoded['SECOND_PARAM_MODE'], 2)]
        store_position = self.get_index_of_value(op_code_decoded['THIRD_PARAM_MODE'], 3)
        self.program[store_position] = 1 if first_value < second_value else 0
        self.PC += 4

    def equals_handler(self, op_code_decoded):
        first_value = self.program[self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)]
        second_value = self.program[self.get_index_of_value(op_code_decoded['SECOND_PARAM_MODE'], 2)]
        store_position = self.get_index_of_value(op_code_decoded['THIRD_PARAM_MODE'], 3)
        self.program[store_position] = 1 if first_value == second_value else 0
        self.PC += 4

    def set_relative_base_handler(self, op_code_decoded):
        value_index = self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)
        value = self.program[value_index]
        self.relative_base_offset += value
        self.PC += 2

    def finish_handler(self, op_code_decoded):
        return

    def run_program(self, inputs):
        self.inputs += inputs
        while True:
            decoded_op_code = self.decode_opcode()
            current_opcode = decoded_op_code["OP_CODE"]
            handle_function_to_execute = self.OP_CODES[current_opcode]['handler']
            handle_function_to_execute(decoded_op_code)
            if current_opcode == FINISH_OP_CODE:
                break
        return None

def main():
    #program_test = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    program = [ 1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,0,1020,1101,0,23,1010,1102,1,31,1009,1101,34,0,1019,1102,38,1,1004,1101,29,0,1017,1102,1,25,1018,1102,20,1,1005,1102,1,24,1008,1101,897,0,1024,1101,0,28,1016,1101,1,0,1021,1101,0,879,1028,1102,1,35,1012,1101,0,36,1015,1101,311,0,1026,1102,1,37,1011,1101,26,0,1014,1101,21,0,1006,1102,1,32,1002,1102,1,33,1003,1102,27,1,1001,1102,1,667,1022,1101,0,892,1025,1101,664,0,1023,1101,30,0,1000,1101,304,0,1027,1101,22,0,1013,1102,1,874,1029,1102,1,39,1007,109,12,21108,40,41,1,1005,1013,201,1001,64,1,64,1106,0,203,4,187,1002,64,2,64,109,5,1205,4,221,4,209,1001,64,1,64,1106,0,221,1002,64,2,64,109,5,21108,41,41,-5,1005,1017,243,4,227,1001,64,1,64,1106,0,243,1002,64,2,64,109,-30,2101,0,8,63,1008,63,30,63,1005,63,269,4,249,1001,64,1,64,1105,1,269,1002,64,2,64,109,15,2101,0,-5,63,1008,63,35,63,1005,63,293,1001,64,1,64,1106,0,295,4,275,1002,64,2,64,109,28,2106,0,-8,1001,64,1,64,1105,1,313,4,301,1002,64,2,64,109,-22,1205,7,329,1001,64,1,64,1106,0,331,4,319,1002,64,2,64,109,-12,1208,6,37,63,1005,63,351,1001,64,1,64,1106,0,353,4,337,1002,64,2,64,109,-3,2108,21,8,63,1005,63,375,4,359,1001,64,1,64,1106,0,375,1002,64,2,64,109,14,1201,-5,0,63,1008,63,39,63,1005,63,401,4,381,1001,64,1,64,1105,1,401,1002,64,2,64,109,17,1206,-9,419,4,407,1001,64,1,64,1105,1,419,1002,64,2,64,109,-10,21101,42,0,-4,1008,1015,42,63,1005,63,445,4,425,1001,64,1,64,1105,1,445,1002,64,2,64,109,-5,1206,7,457,1105,1,463,4,451,1001,64,1,64,1002,64,2,64,109,-6,2107,34,-5,63,1005,63,479,1105,1,485,4,469,1001,64,1,64,1002,64,2,64,109,-8,2102,1,5,63,1008,63,23,63,1005,63,505,1106,0,511,4,491,1001,64,1,64,1002,64,2,64,109,5,2102,1,1,63,1008,63,21,63,1005,63,537,4,517,1001,64,1,64,1105,1,537,1002,64,2,64,109,15,21107,43,44,-6,1005,1014,555,4,543,1106,0,559,1001,64,1,64,1002,64,2,64,109,-6,1207,-7,38,63,1005,63,579,1001,64,1,64,1106,0,581,4,565,1002,64,2,64,109,-17,1201,4,0,63,1008,63,28,63,1005,63,601,1106,0,607,4,587,1001,64,1,64,1002,64,2,64,109,14,2107,31,-9,63,1005,63,625,4,613,1105,1,629,1001,64,1,64,1002,64,2,64,109,15,21102,44,1,-7,1008,1019,44,63,1005,63,651,4,635,1106,0,655,1001,64,1,64,1002,64,2,64,109,3,2105,1,-6,1106,0,673,4,661,1001,64,1,64,1002,64,2,64,109,-14,21101,45,0,2,1008,1017,42,63,1005,63,693,1105,1,699,4,679,1001,64,1,64,1002,64,2,64,109,5,21107,46,45,-8,1005,1012,719,1001,64,1,64,1105,1,721,4,705,1002,64,2,64,109,-19,2108,21,7,63,1005,63,737,1106,0,743,4,727,1001,64,1,64,1002,64,2,64,109,9,1207,-2,25,63,1005,63,761,4,749,1106,0,765,1001,64,1,64,1002,64,2,64,109,-10,1208,1,27,63,1005,63,783,4,771,1106,0,787,1001,64,1,64,1002,64,2,64,109,5,1202,4,1,63,1008,63,29,63,1005,63,807,1106,0,813,4,793,1001,64,1,64,1002,64,2,64,109,8,21102,47,1,0,1008,1013,50,63,1005,63,833,1106,0,839,4,819,1001,64,1,64,1002,64,2,64,109,-12,1202,8,1,63,1008,63,31,63,1005,63,865,4,845,1001,64,1,64,1105,1,865,1002,64,2,64,109,34,2106,0,-7,4,871,1105,1,883,1001,64,1,64,1002,64,2,64,109,-18,2105,1,7,4,889,1105,1,901,1001,64,1,64,4,64,99,21101,0,27,1,21101,915,0,0,1106,0,922,21201,1,13801,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,942,1,0,1106,0,922,21201,1,0,-1,21201,-2,-3,1,21102,957,1,0,1105,1,922,22201,1,-1,-2,1106,0,968,21202,-2,1,-2,109,-3,2106,0,0 ]
    inputs = [ 1 ]
    print('Part 1:')
    vm = Computer(program, inputs)
    vm.run_program([])
    print('Part 2:')
    inputs = [ 2 ]
    vm = Computer(program, inputs)
    vm.run_program([])


main()