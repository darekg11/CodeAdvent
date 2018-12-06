from collections import defaultdict

def readLinesFromFile(filename):
    points = []
    for line in open(filename, 'r'):
        strippedLine = line.strip()
        x, y = strippedLine.split(',')
        points.append((int(x), int(y)))
    return points

def distance(first_point_x, first_point_y, second_point_x, second_point_y):
    return abs(first_point_x - second_point_x) + abs(first_point_y - second_point_y)

# This will create a map where for each point we are going to assign the amount of place it is covering
def calculateAreas(min_x, min_y, max_x, max_y, margin, all_points):
    areas = defaultdict(int)
    for current_x in range(min_x - margin, max_x + margin):
        for current_y in range(min_y - margin, min_y + margin):
            # So now distances_of_given_coordinate_to_every_other_known is a map where key is a distance and value is a point to which the distanec was measured
            distances_of_given_coordinate_to_every_other_known = [(distance(current_x, current_y, p_x, p_y), (p_x, p_y)) for (p_x, p_y) in all_points]
            # So let's sort that so the first elements will have the shortest distances
            distances_of_given_coordinate_to_every_other_known.sort()
            # Because mulitple points might have the same distance we need to check
            first_element_distance = distances_of_given_coordinate_to_every_other_known[0][0]
            second_element_distance = distances_of_given_coordinate_to_every_other_known[1][0]
            if (first_element_distance < second_element_distance):
                closest_point = distances_of_given_coordinate_to_every_other_known[0][1]
                # Add +1 to a area marked by closest_point
                areas[closest_point] += 1
    return areas


def main():
    # Load the points
    points = readLinesFromFile('input.txt')
    SMALL_MARGIN = 200
    BIGGER_MARGIN = 300
    # Find min value of X to start iterating from that value MINUS some margin
    min_x = min((x for (x, y) in points))
    # Find max value of X to end iterating PLUS some margin
    max_x = max((x for (x, y) in points))
    # Find min value of Y to start iteratring from that value MINUS some margin
    min_y = min((y for (x, y ) in points))
    # Find max value of Y to end iterating PLUS some margin
    max_y = max((y for (x, y) in points))
    # what we are going to do is pretty stupid but should work :D
    # First we are going to caclculate the best surface on some small area
    # Then we are goign to calculate the same on bigger area
    # And we are going to drop every result that differs
    # So in the end we should in theory get those areas that did not stretch so in theory those should not be infinite
    small_area = calculateAreas(min_x, min_y, max_x, max_y, SMALL_MARGIN, points)
    bigger_area = calculateAreas(min_x, min_y, max_x, max_y, BIGGER_MARGIN, points)
    # Now drop every value that differs
    only_the_same_in_small_and_larger_area = []
    for (p_x, p_y), area in small_area.items():
        if (bigger_area[(p_x, p_y)] == area):
            only_the_same_in_small_and_larger_area.append(area)
    only_the_same_in_small_and_larger_area.sort(reverse = True)
    # part - 1
    print(only_the_same_in_small_and_larger_area[0])

    # part - 2
    # Much simpler
    # We just need to go throught every point in X,Y of grid and check if sum of distances to every defined POINT is below threshold
    DISTANCE_THRESHOLD = 10000
    area = 0
    for current_x in range(min_x - BIGGER_MARGIN, max_x + BIGGER_MARGIN):
        for current_y in range(min_y - BIGGER_MARGIN, min_y + BIGGER_MARGIN):
            distances_of_given_coordinate_to_every_other_known = [distance(current_x, current_y, p_x, p_y) for (p_x, p_y) in points]
            sum_of_distances = sum(distances_of_given_coordinate_to_every_other_known)
            if sum_of_distances < DISTANCE_THRESHOLD:
                area += 1
    print(area)

main()