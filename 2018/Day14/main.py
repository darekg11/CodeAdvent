def getNewRecipies(first_value, second_value):
    sum_of_recepies = first_value + second_value
    sum_as_string = str(sum_of_recepies)
    return int(sum_as_string[0]), int(sum_as_string[1])

def convertLastTenRecepiesToString(recepies):
    return ''.join(str(recepies[i]) for i in range(len(recepies) - 10, len(recepies)))

def move_index(current_index, recepies_length, offset):
    return (current_index + offset) % recepies_length

def generateRecepies(recepies_threshold):
    recepies = [3, 7]
    task_margin = 10
    first_elf_current_index = 0
    second_elf_current_index = 1
    while len(recepies) < recepies_threshold + task_margin:
        first_recepie = recepies[first_elf_current_index]
        second_recepie = recepies[second_elf_current_index]
        if first_recepie + second_recepie < 10:
            recepies.append(first_recepie + second_recepie)
        else:
            new_recepie_first, new_recepie_second = getNewRecipies(first_recepie, second_recepie)
            recepies.append(new_recepie_first)
            recepies.append(new_recepie_second)
        first_elf_current_index = move_index(first_elf_current_index, len(recepies), 1 + first_recepie)
        second_elf_current_index = move_index(second_elf_current_index, len(recepies), 1 + second_recepie)
    return recepies

def find_recepies(desired_sequence):
    # bytearray is fuck ton optimized for that
    recepies = bytearray([3, 7])
    first_elf_current_index = 0
    second_elf_current_index = 1
    loop_counter = 0
    loop_interval_check = 200_000
    while 1:
        if (loop_counter % loop_interval_check) == 0 and desired_sequence in recepies:
            break
        first_recepie = recepies[first_elf_current_index]
        second_recepie = recepies[second_elf_current_index]
        if first_recepie + second_recepie < 10:
            recepies.append(first_recepie + second_recepie)
        else:
            new_recepie_first, new_recepie_second = getNewRecipies(first_recepie, second_recepie)
            recepies.append(new_recepie_first)
            recepies.append(new_recepie_second)
        first_elf_current_index = move_index(first_elf_current_index, len(recepies), 1 + first_recepie)
        second_elf_current_index = move_index(second_elf_current_index, len(recepies), 1 + second_recepie)
        loop_counter+=1
    return recepies

def main():
    # Part - 1
    input_data = 540561
    recepies = generateRecepies(input_data)
    # Take last 10 items and show them as string
    last_ten = convertLastTenRecepiesToString(recepies)
    print(last_ten)

    # Part - 2
    tracking_sequence = bytearray([5, 4, 0, 5, 6, 1])
    recepies = find_recepies(tracking_sequence)
    length_of_recipies_prior_to_sequence = recepies.index(tracking_sequence)
    print(length_of_recipies_prior_to_sequence)

main()
