from collections import defaultdict
import math

IMMUNE_ARMY = 1
INFECTION_ARMY = 2

RADIATION = 1
COLD = 2
BLUDGEONING = 3
SLASHING = 4
FIRE = 5

WEAKNESSES = 1
IMMUNITIES = 2

POSSIBLE_EFFECTS_MAP = defaultdict()
POSSIBLE_EFFECTS_MAP['radiation'] = RADIATION
POSSIBLE_EFFECTS_MAP['cold'] = COLD
POSSIBLE_EFFECTS_MAP['bludgeoning'] = BLUDGEONING
POSSIBLE_EFFECTS_MAP['slashing'] = SLASHING
POSSIBLE_EFFECTS_MAP['fire'] = FIRE

class Group(object):
    def __init__(self, unit_id, count_of_units, hit_points, weaknesses, immunities, dmg_type, dmg, initiative, army):
        self.unit_id = unit_id # will be used to keep track which units are already choosen to fight
        self.count_of_units = count_of_units
        self.hit_points = hit_points
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.dmg_type = dmg_type
        self.dmg = dmg
        self.initiative = initiative
        self.army = army
        self.attacking_target = None
    def attack_power_of_group(self):
        return self.count_of_units * self.dmg
    def attack_power_multiplier_to_other_group(self, other_group):
        # the dmg type of attacking group is in immunities of defenders
        if self.dmg_type in other_group.immunities:
            return 0
        if self.dmg_type in other_group.weaknesses:
            return 2 * self.attack_power_of_group()
        return self.attack_power_of_group()
    def __repr__(self):
        return 'ID: {0} Army: {1} Count: {2} HP: {3} DMG: {4} DMG_TYPE: {5} Weaknesses: {6} Immunities: {7} Initiative: {8}'.format(self.unit_id, self.army, self.count_of_units, self.hit_points, self.dmg, self.dmg_type, self.weaknesses, self.immunities, self.initiative)

def parse_input_file_to_armies(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    groups = []
    current_army = IMMUNE_ARMY
    id_counter = 1
    for single_line in lines:
        if 'Immune' in single_line:
            current_army = IMMUNE_ARMY
        elif 'Infection' in single_line:
            current_army = INFECTION_ARMY
        else:
            single_line_strip_line_end = single_line.replace('\n', '')
            # Empty line between armies
            if len(single_line_strip_line_end) == 0:
                continue
            line_splitted = single_line_strip_line_end.split()
            # First word is alwys count of unit in group
            number_of_units = int(line_splitted[0])
            # Fifth word (index: 4) is always health point of unit
            hit_points = int(line_splitted[4])
            # Last word is always initiative
            initiative = int(line_splitted[-1])
            # Six word from the end is always the damage
            damage = int(line_splitted[-6])
            # Fifth word from the end is always the damage type
            damage_type = POSSIBLE_EFFECTS_MAP[line_splitted[-5]]
            weakness_set = set()
            immunities_set = set()
            # if we have immunities or weaknesses
            if  '(' in line_splitted[7]:
                # We will iterate starting from word with index 7
                start_index_of_parsing = 7
                # Find index of word that contains )
                end_index_of_parsing = [index for index, word in enumerate(line_splitted) if ')' in word][0]
                currently_adding_to = WEAKNESSES if 'weak' in line_splitted[start_index_of_parsing] else IMMUNITIES
                # Start iterating
                for immunities_weakness_sequence_index in range(start_index_of_parsing, end_index_of_parsing + 1):
                    next_word_token = line_splitted[immunities_weakness_sequence_index]
                    # remove last character from word - for effects, it is ',' or ')' or ';'
                    next_word_drop_last_character = next_word_token[:-1]
                    # try to match word with possible effects
                    found_effect = POSSIBLE_EFFECTS_MAP.get(next_word_drop_last_character)
                    # if successed add it to correct set
                    if found_effect is not None:
                        if currently_adding_to == WEAKNESSES:
                            weakness_set.add(found_effect)
                        else:
                            immunities_set.add(found_effect)
                    # if we have hit semicolon then switch sets to which we are adding
                    if ';' in next_word_token:
                        currently_adding_to = IMMUNITIES if currently_adding_to == WEAKNESSES else WEAKNESSES

            new_group = Group(id_counter, number_of_units, hit_points, weakness_set, immunities_set, damage_type, damage, initiative, current_army)
            groups.append(new_group)
            # Increase ID Counter only when processing actual group instead of headers like Infection or Immune System
            id_counter += 1

    return groups

def battle(groups, boost_value):
    fighting_units = []
    for single_group_units in groups:
        # Boost only the IMMUNE ARMY
        # For INFECTION leave it as it is
        damage_after_boots = single_group_units.dmg + boost_value if single_group_units.army == IMMUNE_ARMY else single_group_units.dmg
        fighting_units.append(Group(single_group_units.unit_id, single_group_units.count_of_units, single_group_units.hit_points, single_group_units.weaknesses, single_group_units.immunities, single_group_units.dmg_type, damage_after_boots, single_group_units.initiative, single_group_units.army))
    while True:
        # Sort by power and inititive in descending order
        fighting_units = sorted(fighting_units, key = lambda k: [k.attack_power_of_group(), k.initiative], reverse = True)
        # Set to keep IDs of choosen unit saved so that each unit can be targeted only once
        groups_already_targeted = set()
        # Now, we need to find a target for group
        for single_group in fighting_units:
            # Possible targets are only (according to puzzle desription):
            # You must target enemy (obvious)
            # Each enemy can be targeted only once so check in set
            # If it cannot deal any defending groups damage, it does not choose a target so only if unit damage output is greater than 0
            possible_targets = [single_enemy_group for single_enemy_group in fighting_units if single_group.army != single_enemy_group.army and single_enemy_group.unit_id not in groups_already_targeted and single_group.attack_power_multiplier_to_other_group(single_enemy_group) > 0]
            # Okay now we have possible target but according to puzzle it must be sorted in such order:
            # Most damage based on bonuses
            # Largest effective power
            # Inititative
            # If an attacking group is considering two defending groups to which it would deal equal damage, it chooses to target the defending group with the largest effective power;
            # if there is still a tie, it chooses the defending group with the highest initiative.
            # Descending order
            sorted_targets = sorted(possible_targets, key = lambda k: [single_group.attack_power_multiplier_to_other_group(k), k.attack_power_of_group(), k.initiative], reverse = True)
            # Set target for current group
            if sorted_targets:
                single_group.attacking_target = sorted_targets[0]
                # Add selected targets to set of already choosen targets so it won't be choosen again
                groups_already_targeted.add(sorted_targets[0].unit_id)
        
        # Targeting now seems to be done
        # Now for attacking phase
        # Sort by initiative
        fighting_units = sorted(fighting_units, key = lambda k: k.initiative, reverse = True)
        # There might be a situation where both sides figth forever
        anything_was_killed = False
        for single_group in fighting_units:
            # If group has attacking target
            if single_group.attacking_target:
                damage_output = single_group.attack_power_multiplier_to_other_group(single_group.attacking_target)
                units_killed =  math.floor(damage_output / single_group.attacking_target.hit_points)
                # if damage output is greater than total amount of units in enemy group
                if units_killed >= single_group.attacking_target.count_of_units:
                    units_killed = single_group.attacking_target.count_of_units
                if units_killed > 0:
                    anything_was_killed = True
                # finlly lower the enemy army
                single_group.attacking_target.count_of_units -= units_killed
        
        # Attack is finished
        # First remove units that died
        fighting_units = [single_unit for single_unit in fighting_units if single_unit.count_of_units > 0]
        # Reomve targets from remaining units
        for remaining_unit in fighting_units:
            remaining_unit.attacking_target = None

        # If nothing was killed, then assume that infection is winning
        if anything_was_killed is False:
            return INFECTION_ARMY, fighting_units

        alive_immune_units = sum([remaining_unit.count_of_units for remaining_unit in fighting_units if remaining_unit.army == IMMUNE_ARMY])
        alive_infection_units = sum([remaining_unit.count_of_units for remaining_unit in fighting_units if remaining_unit.army == INFECTION_ARMY])

        if alive_immune_units == 0 and alive_infection_units > 0:
            return INFECTION_ARMY, fighting_units
        
        if alive_infection_units == 0 and alive_immune_units > 0:
            return IMMUNE_ARMY, fighting_units


def main():
    # Parse input first to retrieve armies
    groups = parse_input_file_to_armies('input.txt')
    # Do the battle without boost at all
    winner, remaining_units = battle(groups, 0)
    # Part 1  - show winner and count reamining units
    print('Winner is: ', 'IMMUNE' if winner == IMMUNE_ARMY else 'INFECTION')
    sum_of_units = sum([single_remaining_unit.count_of_units for single_remaining_unit in remaining_units if single_remaining_unit.army == winner])
    print('Sum of winner: ', sum_of_units)

    # Part 2 - loop until winner is IMMUNE
    current_winner = INFECTION_ARMY
    boost = 0
    while current_winner == INFECTION_ARMY:
        current_winner, remaining_units = battle(groups, boost)
        boost += 1
    print('Used minimal boost: ', boost - 1)
    sum_of_units = sum([single_remaining_unit.count_of_units for single_remaining_unit in remaining_units if single_remaining_unit.army == IMMUNE_ARMY])
    print('Sum of immune system: ', sum_of_units)

main()