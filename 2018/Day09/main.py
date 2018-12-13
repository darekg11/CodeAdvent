from collections import deque, defaultdict

def findHighestRankedElve(max_players, last_marble):
    # Thanks to good people of Reddit, deque solution is the one to go.
    # deque - double linked list
    marbles = deque([0])
    # This will hold score of every player
    players = defaultdict(int)
    # Start with player 1
    current_player = 1
    for singleMarble in range(1, last_marble + 1):
        if singleMarble % 23 != 0:
            # Rotate twice to the right
            # Example: [0,1,2]
            # [2,0,1]
            # [1,2,0]
            marbles.rotate(2)
            # Append marble to the right
            # [1, 2, 0, 3]
            # BUT WAIT THIS IS NOT LIKE IN EXAMPLE, DUDE WTF?
            # Draw it like a circle and see that 3 is betwwen 0 and 1 just like in example
            #     1
            # 3        2
            #     0
            # Do it second time
            # [1, 2, 0, 3] => [3, 1, 2, 0] => [0, 3, 1, 2] => [0, 3, 1, 2, 4]
            #      0
            #        3
            #   4     1
            #      2
            # Shit is not perfect but 4 is betwwen 0 and 2 just like in example
            marbles.append(singleMarble)
        else:
            # Go counter clockwise 7 marbles
            marbles.rotate(-7)
            # Add current marble value to the player and pop current marble from dequeue
            players[current_player] += (singleMarble + marbles.pop())
        if current_player + 1 > max_players:
            current_player = 1
        else:
            current_player += 1

    elfe_highest_score = 0
    elfe_player_number = 1
    for player_number, score in players.items():
        if score > elfe_highest_score:
            elfe_highest_score = score
            elfe_player_number = player_number
    return elfe_player_number, elfe_highest_score

def main():
    # Part - 1
    player_number, score = findHighestRankedElve(416, 71617)
    print(score)

    # Part - 2 -> brutoforce this shit, fans 100% power, let's go
    player_number, score = findHighestRankedElve(416, 71617 * 100)
    print(score)

main()