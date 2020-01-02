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
SET_RELATIVE_BASE = 9

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

PART_1_INPUT_ID = 1
PART_2_INPUT_ID = 5

INSTRUCTION_LENGTH = 5

MEMORY_SIZE = 100000

BLACK_PAINT = '.'
WHITE_PAIN = '#'
GRID_SIZE = 4000
TURN_LEFT = 0
TURN_RIGHT = 1
DIRECTION_UP = '^'
DIRECTION_LEFT = '<'
DIRECTION_DOWN = 'v'
DIRECTION_RIGHT = '>'

ROTATION_TO_MOVE_VECTOR = {
    DIRECTION_UP: { 'x': 0, 'y': -1 },
    DIRECTION_LEFT: { 'x': -1, 'y': 0 },
    DIRECTION_DOWN: { 'x': 0, 'y': 1 },
    DIRECTION_RIGHT: { 'x': 1, 'y': 0 }
}

ROTATION_MATRIX = {
    TURN_LEFT: { DIRECTION_UP: DIRECTION_LEFT, DIRECTION_LEFT: DIRECTION_DOWN, DIRECTION_DOWN: DIRECTION_RIGHT, DIRECTION_RIGHT: DIRECTION_UP },
    TURN_RIGHT: { DIRECTION_UP: DIRECTION_RIGHT, DIRECTION_LEFT: DIRECTION_UP, DIRECTION_DOWN: DIRECTION_LEFT, DIRECTION_RIGHT: DIRECTION_DOWN }
}
class Computer:
    def __init__(self, program, inputs):
        self.program = program[:]
        self.program += [0] * MEMORY_SIZE
        self.inputs = inputs
        self.outputs = []
        self.grid = [[BLACK_PAINT for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
        self.current_robot_position = {'x': 0, 'y': 0} # robot position starting
        self.current_robot_rotation = DIRECTION_UP # robot rotation starting UP
        self.painted_blocks = set()
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
        self.program[store_position] = 0 if self.grid[self.current_robot_position['x']][self.current_robot_position['y']] == BLACK_PAINT else 1
        self.PC += 2

    def output_handler(self, op_code_decoded):
        value_index = self.get_index_of_value(op_code_decoded['FIRST_PARAM_MODE'], 1)
        value = self.program[value_index]
        self.outputs.append(value)
        if len(self.outputs) == 2:
            robot_paint = self.outputs.pop(0)
            robot_rotation = self.outputs.pop(0)
            robot_x_position = self.current_robot_position['x']
            robot_y_position = self.current_robot_position['y']
            # Paint
            self.grid[robot_x_position][robot_y_position] = robot_paint
            # Add panel to set of already painted
            self.painted_blocks.add((robot_x_position, robot_y_position))
            # Rotate robot
            self.current_robot_rotation = ROTATION_MATRIX[robot_rotation][self.current_robot_rotation]
            # Move robot
            vector = ROTATION_TO_MOVE_VECTOR[self.current_robot_rotation]
            new_robot_x = robot_x_position + vector['x']
            new_robot_y = robot_y_position + vector['y']
            self.current_robot_position = { 'x': new_robot_x, 'y': new_robot_y }
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
        print('Part 1:', len(self.painted_blocks))
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
    program = [ 3,8,1005,8,325,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,29,1006,0,41,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,54,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,76,1,9,11,10,2,5,2,10,2,1107,19,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,110,2,1007,10,10,2,1103,13,10,1006,0,34,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,142,1006,0,32,1,101,0,10,2,9,5,10,1006,0,50,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,179,1,1005,11,10,2,1108,11,10,1006,0,10,1,1004,3,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,216,1,1002,12,10,2,1102,3,10,1,1007,4,10,2,101,7,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,253,2,104,3,10,1006,0,70,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,282,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,305,101,1,9,9,1007,9,962,10,1005,10,15,99,109,647,104,0,104,1,21102,838211572492,1,1,21102,342,1,0,1105,1,446,21102,825326674840,1,1,21101,0,353,0,1106,0,446,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,29086686211,1,21102,1,400,0,1106,0,446,21102,209420786919,1,1,21101,0,411,0,1105,1,446,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838337298792,1,21101,434,0,0,1105,1,446,21101,988661154660,0,1,21102,1,445,0,1106,0,446,99,109,2,21201,-1,0,1,21101,40,0,2,21101,0,477,3,21101,0,467,0,1105,1,510,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,472,473,488,4,0,1001,472,1,472,108,4,472,10,1006,10,504,1101,0,0,472,109,-2,2106,0,0,0,109,4,1201,-1,0,509,1207,-3,0,10,1006,10,527,21102,0,1,-3,22102,1,-3,1,22102,1,-2,2,21101,0,1,3,21101,546,0,0,1105,1,551,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,574,2207,-4,-2,10,1006,10,574,21201,-4,0,-4,1105,1,642,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,593,0,1105,1,551,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,612,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,634,21202,-1,1,1,21102,1,634,0,105,1,509,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0 ]
    vm = Computer(program, [])
    vm.run_program([])

main()