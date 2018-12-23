from collections import defaultdict, namedtuple
PLAYER_ID = 0
PLAYER_X = 1
PLAYER_Y = 2
PLAYER_HP = 3
PLAYER_ATTACK_RATE = 4
PLAYER_TYPE = 5
PLAYER_IS_ALIVE = 6

MAP_FREE_TILE = '.'

Point = namedtuple('Point', ['x', 'y'])

def read_map_from_file(filename):
    map_layout = []
    file = open(filename, 'r')
    lines = file.readlines()
    for single_line in lines:
        single_line_dropped_line_end = single_line.replace('\n', '')
        row = []
        for single_row in single_line_dropped_line_end:
            row.append(single_row)
        map_layout.append(row)
    return map_layout

def read_players_data_from_map(map):
    ELF_MAP_MARKER = 'E'
    GIBON_MAP_MARKER = 'G'
    HP_FOR_PLAYER = 200
    ATTACK_FOR_PLAYER = 3
    player_instances = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == ELF_MAP_MARKER or map[y][x] == GIBON_MAP_MARKER:
                # index 0 -> ID
                # index 1 -> x position
                # index 2 -> y position
                # index 3 -> HP of player
                # index 4 -> ATTACk Power og player
                # index 5 -> TYPE of player (Elf / Goblin)
                # index 6 -> Is player alive
                player_instance = [len(player_instances), x, y, HP_FOR_PLAYER, ATTACK_FOR_PLAYER, map[y][x], True]
                player_instances.append(player_instance)
    return player_instances

def sort_players(players):
    # By Y position first, then by X (aka reading order, top to bottom, left to right)
    return sorted(players, key = lambda k: [k[PLAYER_Y], k[PLAYER_X]])

def sort_paths(paths):
    return sorted(paths, key = lambda k: [k[-1].y, k[-1].x])

def try_to_find_enemy_to_attack(curent_player, all_other_players):
    current_player_type = curent_player[PLAYER_TYPE]
    current_player_x = curent_player[PLAYER_X]
    current_player_y = curent_player[PLAYER_Y]
    # get all all alive enemies
    all_alive_enemies = [single_player for single_player in all_other_players if single_player[PLAYER_TYPE] != current_player_type and single_player[PLAYER_IS_ALIVE] is True]
    # get only those enemies that are in range of attack aka:
    # if current_player and enemy has the same X then Math.abs(player.y - enemy.y) == 1
    # if current_player and enemy has the same Y then Math.abs(player.x - enemy.x) == 1
    all_alive_enemies_within_range = []
    for single_enemy in all_alive_enemies:
        if (single_enemy[PLAYER_X] == current_player_x and abs(single_enemy[PLAYER_Y] - current_player_y)) or (single_enemy[PLAYER_Y] == current_player_y and abs(single_enemy[PLAYER_X] - current_player_x)):
            all_alive_enemies_within_range.append(single_enemy)
    # Okay, so far seems so good
    # Now the last step, we need to find the weakest of those in range
    # In case of tie, we need to keep the order (top to bottom and left to right)
    if len(all_alive_enemies_within_range) == 0:
        return None
    if len(all_alive_enemies_within_range) == 1:
        return all_alive_enemies_within_range[0]
    if len(all_alive_enemies_within_range) > 1:
        # Find lowest HP of all enemies in range
        minimal_hp = min([single_alive_enemy_in_range[PLAYER_HP] for single_alive_enemy_in_range in all_alive_enemies_within_range])
        # Find all of such enemies
        enemies_with_lowest_hp = [single_low_hp_enemy for single_low_hp_enemy in all_alive_enemies_within_range if single_low_hp_enemy[PLAYER_HP] == minimal_hp]
        # If we have only one such enemy, return that one
        if len(enemies_with_lowest_hp) == 1:
            enemies_with_lowest_hp[0]
        # If we have mulitple, then sort them in reading order once more just to be sure and return the first one
        sorted_lowest_hp_enemies = sort_players(enemies_with_lowest_hp)
        return sorted_lowest_hp_enemies[0]
        
        
def generate_adjacent_movements_vectors(point):
    return [Point(point.x, point.y + 1), Point(point.x, point.y - 1), Point(point.x + 1, point.y), Point(point.x - 1, point.y)]

def try_to_find_next_movement(current_player, all_players, map_layout):
    current_player_type = current_player[PLAYER_TYPE]
    current_player_x = current_player[PLAYER_X]
    current_player_y = current_player[PLAYER_Y]

    #XY to X,Y position, this will be our targets to which we need to make pathfinding
    all_enemies_positions = defaultdict()
    # All coordsinates that have already been visited by the player so we won't loop
    coordinates_already_visited_by_current_players = defaultdict()
    all_alive_enemies = [single_player for single_player in all_players if single_player[PLAYER_TYPE] != current_player_type and single_player[PLAYER_IS_ALIVE] is True]
    # from all alive enemies we need to get only those that have a FREE MAP TILE IN ANY ADJACENT DIRECTION
    # because there is no sens in including enemies that are completely blocked for current_player
    # we includ every opening of enemy
    for single_alive_enemy in all_alive_enemies:
        enemy_alive_enemy_pos = Point(single_alive_enemy[PLAYER_X], single_alive_enemy[PLAYER_Y])
        adjacent_vectors_of_enemy = generate_adjacent_movements_vectors(enemy_alive_enemy_pos)
        for single_adjacent_vector in adjacent_vectors_of_enemy:
            vector_x = single_adjacent_vector.x
            vector_y = single_adjacent_vector.y
            # Okay, if enemy is accessible from that position, add it as possible attach vector
            if map_layout[vector_y][vector_x] == MAP_FREE_TILE:
                all_enemies_positions[single_adjacent_vector] = single_adjacent_vector
    # Mark current player position as already visited
    coordinates_already_visited_by_current_players[Point(current_player_x, current_player_y)] = True
    # This is the root of the path
    player_paths = []
    player_paths.append([Point(current_player_x, current_player_y)])
    while True:
        new_paths_to_take = []
        paths_to_enemies = []
        for current_path in player_paths:
            last_path = current_path[len(current_path) - 1]
            # from current player patg get all adjacent positions
            adjacent_vectors_of_player = generate_adjacent_movements_vectors(last_path)
            # go through every adjacent vectors
            for single_adjacent_vector_player in adjacent_vectors_of_player:
                enemy_pos = all_enemies_positions.get(single_adjacent_vector_player)
                # Check if we are at position that allows us to attack an enemy
                if enemy_pos is not None:
                    # update player path to enemies
                    new_array_to_append = []
                    for some_shit in current_path:
                        new_array_to_append.append(some_shit)
                    new_array_to_append.append(single_adjacent_vector_player)
                    new_array_to_append.append(enemy_pos)
                    paths_to_enemies.append(new_array_to_append)
                # if adjacent coords has not been yet viisted and adjacent cords is a FREE MAP TILE then add it to new paths to explore in coming iteration
                elif coordinates_already_visited_by_current_players.get(single_adjacent_vector_player) is None and map_layout[single_adjacent_vector_player.y][single_adjacent_vector_player.x] == MAP_FREE_TILE:
                    new_array_to_append = []
                    for some_shit in current_path:
                        new_array_to_append.append(some_shit)
                    new_array_to_append.append(single_adjacent_vector_player)
                    new_paths_to_take.append(new_array_to_append)
                # Whatever happen, mark that coordinate as visited
                coordinates_already_visited_by_current_players[single_adjacent_vector_player] = True
        
        # If we alrady found the path to enemy, then that is amazing and we can return it
        if len(paths_to_enemies) > 0:
            sorted_paths = sort_paths(paths_to_enemies)
            return sorted_paths[0][1]

        player_paths = new_paths_to_take
        # No more possibilities
        if len(player_paths) == 0:
            return None


def do_round_of_game(map_layout, players):
    for player_index in range(len(players)):
        current_player = players[player_index]
        is_player_alive = current_player[PLAYER_IS_ALIVE]
        player_type = current_player[PLAYER_TYPE]
        current_player_attack_rate = current_player[PLAYER_ATTACK_RATE]
        # If player is dead skip that player
        if is_player_alive is False:
            continue
        # Check if there are any players of opposite type left on the map
        # If not then we need to end game
        alive_enemies = [single_player for single_player in players if single_player[PLAYER_TYPE] != player_type and single_player[PLAYER_IS_ALIVE] is True]
        # If there are no alive enemies then end game and return current players
        if len(alive_enemies) == 0:
            return False, map_layout, players
        # check if given player can already attack an enemy
        enemy_to_attack = try_to_find_enemy_to_attack(current_player, alive_enemies)
        next_movement = try_to_find_next_movement(current_player, players, map_layout) if enemy_to_attack is None else None
        # if we don't have enemy to attack and we have possible move
        if enemy_to_attack is None and next_movement is not None:
            # Mark current tile as free
            map_layout[current_player[PLAYER_Y]][current_player[PLAYER_X]] = MAP_FREE_TILE
            # Move current player to new positions
            players[player_index][PLAYER_X] = next_movement.x
            players[player_index][PLAYER_Y] = next_movement.y
            current_player = players[player_index]
            # Mark new tile occupies by current player with type of that player
            map_layout[current_player[PLAYER_Y]][current_player[PLAYER_X]] = player_type
            # once moved, try to see if enemy is in the distance now
            enemy_to_attack = try_to_find_enemy_to_attack(current_player, alive_enemies)
        
        # see if we have enemy to attack
        # then attack
        if enemy_to_attack is not None:
            # find that enemy in players array by ID and get index of that player
            for enemy_index in range(len(players)):
                if players[enemy_index][PLAYER_ID] == enemy_to_attack[PLAYER_ID]:
                    #  Reduce enemy health
                    players[enemy_index][PLAYER_HP] -= current_player_attack_rate
                    # If enemy died
                    if players[enemy_index][PLAYER_HP] <= 0:
                        # No loner alive
                        players[enemy_index][PLAYER_IS_ALIVE] = False
                        # Clear enemy tile
                        enemy_y = players[enemy_index][PLAYER_Y]
                        enemy_x = players[enemy_index][PLAYER_X]
                        map_layout[enemy_y][enemy_x] = MAP_FREE_TILE
    
    # Round has ended
    return True, map_layout, players

def main():
    # Parse the input to get ma layout:
    map_layout = read_map_from_file('test-input.txt')

    # Get player instances from map layout:
    player_instances = read_players_data_from_map(map_layout)

    # should continue playing
    should_continue_game = True

    # game rounds
    rounds = 0

    while should_continue_game:
        # First sort the players:
        player_instances = sort_players(player_instances)
        should_continue_game, map_layout, player_instances = do_round_of_game(map_layout, player_instances)
        rounds += 1
    
    # Game has ended
    # Part 1 - calculate score
    sum_of_hp_of_remaining_players = 0
    for single_player in player_instances:
        if single_player[PLAYER_IS_ALIVE] is True:
            sum_of_hp_of_remaining_players += single_player[PLAYER_HP]
    total_score = rounds * sum_of_hp_of_remaining_players
    print(rounds)
    print(total_score)

main()