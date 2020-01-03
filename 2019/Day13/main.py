from os import system
from time import sleep
from collections import defaultdict
import operator

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

TILE_EMPTY = 0
TILE_WALL = 1
TILE_BLOCK = 2
TILE_HORIZONTAL_PADDLE = 3
TILE_BALL = 4

TILE_EMPTY_CHARACTER = ' '
TILE_WALL_CHARACTER = 'W'
TILE_BLOCK_CHARACTER = 'O'
TILE_HORIZONTAL_PADDLE_CHARACTER = '_'
TILE_BALL_CHARACTER = 'X'

TILE_TO_CHARACTER_MAP = {
    TILE_EMPTY: TILE_EMPTY_CHARACTER,
    TILE_WALL: TILE_WALL_CHARACTER,
    TILE_BLOCK: TILE_BLOCK_CHARACTER,
    TILE_HORIZONTAL_PADDLE: TILE_HORIZONTAL_PADDLE_CHARACTER,
    TILE_BALL: TILE_BALL_CHARACTER
}

RENDER_SPEED_SECONDS = 0.04 # Almost 40FPS

class Computer:
    def __init__(self, program, inputs):
        self.program = program[:]
        self.program += [0] * MEMORY_SIZE
        self.inputs = inputs
        self.outputs = []
        self.PC = 0
        self.game_userland = defaultdict(int)
        self.relative_base_offset = 0
        self.exited = False
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
        self.exited = True
        return

    def run_program(self, inputs):
        self.inputs = inputs
        while True:
            decoded_op_code = self.decode_opcode()
            current_opcode = decoded_op_code["OP_CODE"]
            handle_function_to_execute = self.OP_CODES[current_opcode]['handler']
            handle_function_to_execute(decoded_op_code)
            if current_opcode == OUTPUT_OP_CODE:
                return self.outputs.pop(0)
            if current_opcode == FINISH_OP_CODE:
                break
        return None

def main():
    program = [ 1,380,379,385,1008,2487,361412,381,1005,381,12,99,109,2488,1101,0,0,383,1102,0,1,382,20101,0,382,1,20101,0,383,2,21101,0,37,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,44,381,1005,381,22,1001,383,1,383,1007,383,21,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1105,1,161,107,1,392,381,1006,381,161,1102,-1,1,384,1105,1,119,1007,392,42,381,1006,381,161,1102,1,1,384,20101,0,392,1,21101,19,0,2,21102,0,1,3,21102,1,138,0,1106,0,549,1,392,384,392,21002,392,1,1,21102,19,1,2,21101,0,3,3,21101,161,0,0,1106,0,549,1101,0,0,384,20001,388,390,1,21001,389,0,2,21101,0,180,0,1106,0,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,21001,389,0,2,21101,0,205,0,1105,1,393,1002,390,-1,390,1101,1,0,384,21002,388,1,1,20001,389,391,2,21101,228,0,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,21001,388,0,1,20001,389,391,2,21102,253,1,0,1106,0,393,1002,391,-1,391,1101,1,0,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,279,0,0,1105,1,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21102,304,1,0,1105,1,393,1002,390,-1,390,1002,391,-1,391,1102,1,1,384,1005,384,161,20102,1,388,1,20102,1,389,2,21102,1,0,3,21102,1,338,0,1106,0,549,1,388,390,388,1,389,391,389,21002,388,1,1,21001,389,0,2,21102,4,1,3,21101,0,365,0,1105,1,549,1007,389,20,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,326,20,16,1,1,22,109,3,21201,-2,0,1,21201,-1,0,2,21101,0,0,3,21102,1,414,0,1105,1,549,21201,-2,0,1,22101,0,-1,2,21101,429,0,0,1105,1,601,1201,1,0,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2105,1,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,21202,-3,1,-7,109,-8,2106,0,0,109,4,1202,-2,44,566,201,-3,566,566,101,639,566,566,1202,-1,1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,44,594,201,-2,594,594,101,639,594,594,20101,0,0,-2,109,-3,2106,0,0,109,3,22102,21,-2,1,22201,1,-1,1,21101,0,467,2,21102,1,497,3,21101,0,924,4,21101,0,630,0,1106,0,456,21201,1,1563,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,0,2,2,0,0,2,2,0,0,2,2,2,0,2,0,0,2,0,0,1,1,0,2,2,0,0,2,0,0,2,2,0,0,2,2,2,2,0,0,0,0,0,0,0,2,0,2,2,2,2,0,2,0,2,2,2,0,2,0,0,0,0,0,1,1,0,2,0,0,2,0,2,0,0,2,0,2,0,0,0,0,2,2,2,2,2,2,0,2,2,2,0,0,2,0,2,2,0,2,0,0,2,2,2,0,0,0,1,1,0,2,2,2,0,2,2,2,2,2,0,2,2,2,2,0,2,2,0,0,2,0,2,0,0,2,2,2,2,2,2,0,2,2,0,0,0,2,2,2,0,0,1,1,0,0,0,2,2,2,2,2,2,0,0,0,2,2,0,0,2,2,2,0,2,0,0,2,0,0,2,2,2,2,0,2,2,0,2,0,0,2,2,0,2,0,1,1,0,2,2,0,2,2,0,2,2,2,0,2,2,2,2,2,2,2,2,2,0,2,2,0,0,2,2,2,0,0,2,0,2,0,0,2,2,2,2,2,2,0,1,1,0,0,2,2,2,0,2,0,2,2,2,0,0,2,0,0,2,2,0,0,2,2,0,2,2,0,0,0,0,0,2,0,0,2,2,2,2,0,0,0,2,0,1,1,0,2,2,0,2,2,2,2,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,0,0,2,2,2,0,2,2,0,0,2,2,2,0,2,0,2,0,1,1,0,2,0,2,2,2,0,2,2,0,0,2,2,2,2,0,0,2,2,2,2,0,2,0,2,0,0,2,2,2,0,0,2,2,2,0,0,2,2,0,2,0,1,1,0,2,0,0,2,2,2,0,0,0,2,0,0,2,2,0,2,2,2,2,0,2,2,2,2,0,0,2,2,0,0,2,2,2,0,2,2,0,2,2,2,0,1,1,0,2,2,2,0,2,2,2,0,2,2,0,2,2,2,2,0,0,2,0,2,0,0,2,2,2,2,2,2,2,2,0,2,0,2,2,0,2,2,0,0,0,1,1,0,0,2,2,2,2,2,2,2,2,0,2,0,0,2,2,2,2,0,0,2,0,0,0,2,0,2,2,2,2,0,2,0,2,2,0,2,2,2,0,2,0,1,1,0,2,2,2,2,2,2,2,2,0,0,2,2,0,2,2,2,2,2,2,2,0,0,0,0,2,2,2,2,2,2,2,0,0,2,2,2,0,0,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,76,15,12,20,17,35,34,85,94,21,61,77,95,65,26,54,97,28,64,78,13,60,7,20,13,39,26,86,92,16,31,89,45,57,59,94,4,79,83,27,94,86,44,96,79,56,56,68,94,84,79,17,16,43,86,35,76,47,16,20,71,88,82,7,12,17,8,63,61,88,40,93,14,85,9,34,70,27,27,58,71,69,88,14,72,51,33,43,15,44,84,29,35,18,82,14,45,98,10,35,62,74,16,44,7,51,38,50,31,82,72,21,94,21,53,73,40,24,93,96,6,64,19,57,51,56,53,57,58,68,78,9,79,87,52,62,36,17,80,30,42,65,96,3,55,56,95,89,42,33,23,30,90,47,18,68,94,51,26,52,23,32,13,3,93,91,44,1,30,86,93,8,69,72,2,53,33,23,58,48,69,74,24,6,33,85,96,38,83,51,61,96,79,25,14,78,83,41,85,32,94,95,67,87,53,47,81,14,56,88,37,95,54,83,84,41,35,75,33,77,24,32,62,10,5,91,82,63,21,81,71,5,89,4,64,87,32,59,22,3,98,79,70,79,5,52,26,70,19,95,23,45,77,79,60,89,89,88,45,5,50,31,47,14,76,22,9,48,71,4,15,38,82,61,62,59,68,50,81,71,57,47,41,9,63,77,49,91,25,2,14,88,60,43,44,7,14,51,93,44,45,75,19,49,34,41,19,48,25,34,32,88,29,51,88,71,79,76,7,81,73,90,42,78,43,50,40,18,8,56,51,86,58,74,47,27,5,80,83,96,36,23,93,56,94,40,67,49,83,10,62,45,82,94,8,51,16,43,7,16,37,92,12,9,77,51,75,95,46,95,91,46,35,49,97,85,28,17,39,78,42,37,17,20,9,22,3,41,43,78,34,70,60,28,92,60,8,81,70,86,6,61,57,37,85,23,55,69,89,25,5,20,49,31,98,11,27,56,9,74,9,66,5,44,60,97,13,37,74,54,27,38,4,19,72,90,89,23,8,35,54,35,79,82,72,43,14,67,64,89,12,4,52,30,6,7,11,7,72,81,73,49,76,23,44,8,17,35,21,26,88,4,46,71,96,89,34,71,79,59,24,49,87,24,57,89,32,97,71,95,41,29,27,70,70,33,94,62,84,21,26,23,82,5,35,58,48,71,60,97,89,84,69,82,85,90,54,30,81,87,51,59,76,20,95,8,11,46,18,59,36,76,69,71,42,29,69,69,24,54,84,96,88,79,40,38,73,10,89,66,32,25,96,16,41,78,53,76,28,37,92,33,33,77,22,51,50,7,47,50,4,59,70,14,42,20,97,95,54,10,47,94,89,68,69,10,85,9,57,7,32,44,3,75,54,52,89,39,38,88,10,23,95,5,66,68,72,42,94,94,51,73,3,5,35,8,28,4,20,74,32,40,20,51,17,3,62,28,59,43,10,7,52,70,82,8,52,70,50,45,79,98,65,78,20,73,64,64,87,2,11,69,28,70,37,73,3,29,57,32,15,87,42,66,1,57,26,31,23,56,51,45,50,31,10,8,74,29,73,70,72,18,74,97,88,80,46,10,20,8,97,80,54,47,64,12,48,87,14,94,49,52,30,20,21,9,98,30,51,11,30,32,78,21,72,55,38,79,74,35,93,31,40,66,86,27,12,34,80,45,44,23,4,35,35,58,6,17,47,57,30,82,65,16,82,76,63,75,76,85,86,69,29,92,79,9,14,46,76,37,66,61,15,97,7,4,23,91,8,81,81,15,59,3,29,47,24,81,85,63,10,87,9,10,87,15,25,25,62,17,30,21,87,38,92,65,88,13,23,21,75,44,89,9,86,58,81,25,75,93,46,52,44,13,70,32,71,82,7,11,54,71,11,69,3,31,7,26,23,65,10,15,10,82,33,28,67,33,65,7,70,23,92,83,53,6,35,44,65,95,23,53,13,25,90,69,7,89,34,26,91,81,84,45,61,78,87,51,98,38,5,59,29,12,5,53,78,88,4,93,56,97,65,37,22,3,52,80,1,18,43,93,20,97,65,81,84,35,6,58,16,31,86,72,47,18,27,22,97,85,52,43,95,16,12,10,44,49,24,86,28,55,19,22,361412 ]
    inputs = []
    vm = Computer(program, inputs)
    game_userland_tiles = defaultdict(int)
    while vm.exited is False:
        x_position = vm.run_program([])
        y_position = vm.run_program([])
        title_id = vm.run_program([])
        game_userland_tiles[(x_position, y_position)] = title_id
    print('Part 1:', len([block for block in game_userland_tiles.values() if block == TILE_BLOCK]))

    program[0] = 2
    # Flip it to see Game rendered every game loop tick - it's inside terminal so kinda shitty but it is still fun and helps with debugging
    draw_game_every_loop = True
    vm = Computer(program, inputs)
    current_score = 0
    ball_position_x = 0
    paddle_position_x = 0
    game_userland_tiles = defaultdict(int)
    while vm.exited is False:
        input_value = 0
        if ball_position_x < paddle_position_x:
            input_value = -1
        if ball_position_x > paddle_position_x:
            input_value = 1
        x_position = vm.run_program([input_value])
        y_position = vm.run_program([input_value])
        title_id = vm.run_program([input_value])
        paddle_position_x = x_position if title_id == TILE_HORIZONTAL_PADDLE else paddle_position_x
        ball_position_x = x_position if title_id == TILE_BALL else ball_position_x
        current_score = title_id if x_position == -1 and y_position == 0 else current_score
        if x_position != -1 and y_position != 0:
            game_userland_tiles[(x_position, y_position)] = title_id
        # Paddle is most probaly rendered at the end so render game screen once paddle is in blocks - not the best way but it works quite well
        if draw_game_every_loop and TILE_HORIZONTAL_PADDLE in game_userland_tiles.values():
            minx = min(game_userland_tiles, key=operator.itemgetter(0))[0]
            maxx = max(game_userland_tiles, key=operator.itemgetter(0))[0]
            miny = min(game_userland_tiles, key=operator.itemgetter(1))[1]
            maxy = max(game_userland_tiles, key=operator.itemgetter(1))[1]
            system('clear')
            print('Score:', current_score)
            for y in range(miny, maxy + 1):
                single_line = ""
                for x in range(minx, maxx + 1):
                    value = game_userland_tiles[(x, y)]
                    single_line += TILE_TO_CHARACTER_MAP[TILE_EMPTY] if value is None else TILE_TO_CHARACTER_MAP[value]
                print(single_line)
            sleep(RENDER_SPEED_SECONDS)
    print('Part 2:', current_score)
main()