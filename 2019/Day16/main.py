PATTERN = [ 0, 1, 0, -1 ]
MESSAGE_LENGTH = 8

def remap_string_to_int_array(string):
    return [ int(single_character) for single_character in string ]

def remap_int_array_to_string(array):
    return ''.join([str(single_number) for single_number in array])

def create_pattern_array(repetition_count, length):
    total_count_including_offset = length + 1
    pattern_array = []
    index_to_retrieve_pattern = 0
    while len(pattern_array) < total_count_including_offset:
        for __ in range(0, repetition_count):
            pattern_array.append(PATTERN[index_to_retrieve_pattern % len(PATTERN)])
        index_to_retrieve_pattern += 1
    # moved by 1 index from the left
    return pattern_array[1:]

def calculate_for_single_index(array, index):
    repetition_count = index + 1
    pattern_array = create_pattern_array(repetition_count, len(array))
    total_for_single_index = sum([value * pattern_array[index_inner] for index_inner, value in enumerate(array) ])
    total_as_string = str(total_for_single_index)
    return int(total_as_string[len(total_as_string) - 1])

def single_phase(array):
    after_phase = []
    for index, __ in enumerate(array):
        after_phase.append(calculate_for_single_index(array, index))
    return after_phase

def run_simulation(base_input, phases_count):
    array_inputs = remap_string_to_int_array(base_input)
    current_phase = 0
    while current_phase < phases_count:
        array_inputs = single_phase(array_inputs)
        current_phase += 1
    return remap_int_array_to_string(array_inputs)

def main():
    input_value = '59715091976660977847686180472178988274868874248912891927881770506416128667679122958792624406231072013221126623881489317912309763385182133601840446469164152094801911846572235367585363091944153574934709408511688568362508877043643569519630950836699246046286262479407806494008328068607275931633094949344281398150800187971317684501113191184838118850287189830872128812188237680673513745269645219228183633986701871488467284716433953663498444829748364402022393727938781357664034739772457855166471802886565257858813291667525635001823584650420815316132943869499800374997777130755842319153463895364409226260937941771665247483191282218355610246363741092810592458'
    value_after_phases = run_simulation(input_value, 100)
    first_8_characters = value_after_phases[0:8]
    print('Part 1:', first_8_characters)

    # Start part 2: this only works if your offset is in second half of your input
    # https://www.reddit.com/r/adventofcode/comments/ebai4g/2019_day_16_solutions/
    # https://www.youtube.com/watch?v=Xmcw8m0rukk
    # https://www.youtube.com/watch?v=mgwFfx-rOCs
    # So basically for part 2, the pattern is that each of digit going from the end is actually % 10 of sums on that index
    # So:
    # Last []: [7, 4, 6, 6, 4] -> previous combination (last - 1) is going to:
    # Last -1: [7, 0, 6, 0, 4] why? [4] -> because 4 from last % 10 is 4
    #                               [0, 4] -> because (4+6) from last % 10 = 0
    #                               [6, 0, 4] -> because (4+6+6) from last %10 = 0
    #                               etc
    # This is just a pattern that you needed to see in order to complete this
    # So we just need to go from end until our offset
    offset = int(input_value[0:7])
    input_value_huge = [int(single_character) for single_character in input_value] * 10000
    input_value_huge_len = len(input_value_huge)
    if offset > input_value_huge_len // 2:
        for __ in range(0, 100):
            pos = input_value_huge_len - 1
            total = 0
            while pos >= offset:
                total += input_value_huge[pos]
                total_as_string = str(total)
                input_value_huge[pos] = int(total_as_string[len(total_as_string) - 1])
                pos -= 1
        print('Part 2:', ''.join([ str(single_number) for single_number in input_value_huge[offset:offset + MESSAGE_LENGTH] ]))

main()