from collections import defaultdict

def calculatePowerOfACall(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int((power_level/100)%10)
    if power_level < 1:
        power_level = 0
    power_level -= 5
    return power_level

def createAGridWithEveryCellCalculatedPower(serial_number):
    # Use 2d array of summed array table (https://en.wikipedia.org/wiki/Summed-area_table)
    # Clear grid to have 0s everywhere
    grid = [[0 for i in range(0, 301)] for j in range(0, 301)]
    for x in range(1, 301):
        for y in range(1, 301):
            grid[x][y] = calculatePowerOfACall(x, y, serial_number) +  grid[x - 1][y] + grid[x][y - 1] - grid[x - 1][y - 1]
    return grid

def findLargest3x3Square(grid):
    largest_x = 0
    largest_y = 0
    largest_power = None

    for x in range(1, len(grid) - 3):
        for y in range(1, len(grid) - 3):
            powerOfSquare = grid[x + 2][y + 2] - grid[x + 2][y - 1] - grid[x - 1][y + 2] + grid[x - 1][y - 1]
            if largest_power is None or powerOfSquare > largest_power:
                largest_power = powerOfSquare
                largest_x = x
                largest_y = y
    return largest_x, largest_y, largest_power

def main():
    # Input:
    serial_number = 5153

    # Create a grid:
    grid = createAGridWithEveryCellCalculatedPower(serial_number)

    # Part 1
    largest_x, largest_y, largest_power = findLargest3x3Square(grid)
    print(largest_x)
    print(largest_y)

main()