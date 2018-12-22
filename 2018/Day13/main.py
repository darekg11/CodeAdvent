from collections import defaultdict
# Array defining what should happen on the intersection
# This will be looped with modulo based on cart intersection_counter
# ? means eiher up or down which direction the cart is doing currently
INTERSECTION_ACTIONS = ['<', '?', '>']

def read_input_return_carts_and_map(filename):
    # This will store the carts found on input
    # We need following props on them:
    # id -> to find if other crashed [x,y] coordinate is a diffrent cart
    # x position
    # y position
    # direction that cart is going
    # intersection_counter
    # did crash
    carts = []
    # tracks map [y][x]
    tracks_map = []
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    cart_start_direction_to_track_under_them_map = defaultdict()
    cart_start_direction_to_track_under_them_map['>'] = '-'
    cart_start_direction_to_track_under_them_map['<'] = '-'
    cart_start_direction_to_track_under_them_map['^'] = '|'
    cart_start_direction_to_track_under_them_map['v'] = '|'
    for single_line in lines:
        single_line_dropped_line_end = single_line.replace('\n', '')
        map_row = []
        for x in range(len(single_line_dropped_line_end)):
            # if this is not a cart, just add column to the map row
            cart_to_track = cart_start_direction_to_track_under_them_map.get(single_line[x])
            if cart_to_track is None:
                map_row.append(single_line[x])
            # if this is a card, we need to map it to correct track underneath when initial cart moves from it's position, we need to fill that
            else:
                map_row.append(cart_to_track)
                # we also need to add cart to our carts array
                # [id, x, y, direction, intersecton_counter]
                new_cart = [len(carts), x, len(tracks_map), single_line[x], 0, False]
                carts.append(new_cart)
        tracks_map.append(map_row)
    return carts, tracks_map

def sort_carts(carts):
    return sorted(carts, key = lambda k: [k[1], k[2]])

def main():
    # How position of cart should be updated based on current direction of cart
    # First index in value is X, second value is Y
    MOVEMENT_VECTORS = defaultdict()
    MOVEMENT_VECTORS['^'] = [0, -1]
    MOVEMENT_VECTORS['v'] = [0, 1]
    MOVEMENT_VECTORS['>'] = [1, 0]
    MOVEMENT_VECTORS['<'] = [-1, 0]

    CART_REDIRECTIONS = defaultdict()
    CART_REDIRECTIONS['^|'] = '^' # if dir is up and track is straight continue up
    CART_REDIRECTIONS['^>'] = '>' # if dir is up and you need to turn right, then just continue right
    CART_REDIRECTIONS['^<'] = '<' # if dir is up and you need to turn left, then just continue left
    CART_REDIRECTIONS['v|'] = 'v' # if dir is down and track is straight continue down
    CART_REDIRECTIONS['v<'] = '>' # if dir is down and you need to turn left, in reality the cart is turning right - imagine it top to bottom in 2d
    CART_REDIRECTIONS['v>'] = '<' # if dir is down and you need to turn right, in reality the cart is turning left -  imagine it top to bottom in 2d
    CART_REDIRECTIONS['>-'] = '>' # if dir is right and track is straight continue right
    CART_REDIRECTIONS['<-'] = '<' # if dir is left and track is straig continue left
    CART_REDIRECTIONS['><'] = '^' # if dir is right and you need to turn left, in reality the cart is turning up - imagine it top to bottom in 2d
    CART_REDIRECTIONS['<>'] = '^' # if dir is left and you need to turn right, in reality the cart is turning up - imagine it top to bottom in 2d
    CART_REDIRECTIONS['>>'] = 'v' # if dir is right and you need to turn right, in reality the cart is turning down - imagine it top to bottom in 2d
    CART_REDIRECTIONS['<<'] = 'v' # if dir is left and you need to turng left, in reality the cart is turning down - imagine it top to bottom in 2d
    CART_REDIRECTIONS['^?'] = '^' # if dir is up and we are at intersection marked by ? then just continue up
    CART_REDIRECTIONS['v?'] = 'v' # if dir is bottom and we are at intersection marked by ? then just down
    CART_REDIRECTIONS['>?'] = '>' # if dir is right and we are at intersection marked by ? then just continue right
    CART_REDIRECTIONS['<?'] = '<' # if dir is left and we are at intersection marked by ? then just continue left
    CART_REDIRECTIONS['>/'] = '^' # if dir is right and we hit curve we need to continue up
    CART_REDIRECTIONS['</'] = 'v' # if dir is left and we hit curve we need to go down
    CART_REDIRECTIONS['^/'] = '>' # if dir is up and we hit curve then go right
    CART_REDIRECTIONS['v/'] = '<' # if dir is down and we hit curve then go left 
    CART_REDIRECTIONS['>\\'] = 'v' # if dir is right and we hit curve then go down
    CART_REDIRECTIONS['<\\'] = '^' # if dir is left and we hit curve then go up
    CART_REDIRECTIONS['^\\'] = '<' # if dir is up and we hit curve then go left
    CART_REDIRECTIONS['v\\'] = '>' # if dir is down and we hit curve then go right

    # Parse the input
    not_crashed_carts, tracks_layout = read_input_return_carts_and_map('input.txt')

    # was there first crash:
    was_there_first_crash = False

    # Run carts until first crash
    while len(not_crashed_carts) > 1:
        # Crashed cars ids per tick
        crashed_cars_id = set()
        # First, we need to sort the carts by X coords and if there are any on the same track then we sort by Y too get them by top first
        not_crashed_carts = sort_carts(not_crashed_carts)
        for i in range(len(not_crashed_carts)):
            # If cart got crashed then skip it
            # It is required because crashed carts are removed after for loop
            # because removing them inside the loop won't update len(not_crashed_carts) that is calculated at the beggining
            if not_crashed_carts[i][5] == True:
                continue
            # Move the cart in cart current direction
            cart_movement_vector = MOVEMENT_VECTORS[not_crashed_carts[i][3]]
            not_crashed_carts[i][1] += cart_movement_vector[0]
            not_crashed_carts[i][2] += cart_movement_vector[1]
            # Get on what kind of track the cart is now
            new_cart_track = tracks_layout[not_crashed_carts[i][2]][not_crashed_carts[i][1]]
            # If we hit intersection
            if new_cart_track == '+':
                # get new direction based on counter
                # use modulo to wrap around array if index is greater than array length
                new_cart_track = INTERSECTION_ACTIONS[not_crashed_carts[i][4] % len(INTERSECTION_ACTIONS)]
                # Increase intersection_counter
                not_crashed_carts[i][4] += 1
            # Now we need to get new direction of cart somehow
            combine_current_dir_and_new_track = not_crashed_carts[i][3] + new_cart_track
            not_crashed_carts[i][3] = CART_REDIRECTIONS[combine_current_dir_and_new_track]
            
            for single_other_working_cart_index in range(len(not_crashed_carts)):
                other_cart_id = not_crashed_carts[single_other_working_cart_index][0]
                other_cart_x = not_crashed_carts[single_other_working_cart_index][1]
                other_cart_y = not_crashed_carts[single_other_working_cart_index][2]
                if other_cart_id != not_crashed_carts[i][0] and other_cart_x == not_crashed_carts[i][1] and other_cart_y == not_crashed_carts[i][2]:
                    crashed_cars_id.add(other_cart_id)
                    crashed_cars_id.add(not_crashed_carts[i][0])
                    # Mark current cart as crashed
                    not_crashed_carts[i][5] = True
                    # Mark other crashed cart as crashed
                    not_crashed_carts[single_other_working_cart_index][5] = True
                    if was_there_first_crash is False:
                        # Part 1
                        first_crash_x = not_crashed_carts[i][1]
                        first_crash_y = not_crashed_carts[i][2]
                        print(first_crash_x, first_crash_y)
                        was_there_first_crash = True
        # Remove crashed cars from array
        not_crashed_carts = [single_car for single_car in not_crashed_carts if single_car[0] not in crashed_cars_id]

    # Part - 2, X and Y of last cart
    print(not_crashed_carts[0][1], not_crashed_carts[0][2])

main()