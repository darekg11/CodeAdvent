from collections import defaultdict

def readNumbersFromFile(filename):
    return [int(singleNumber) for singleNumber in open(filename, 'r').readline().split()]

# This will be a global variable
inputNumbers = readNumbersFromFile('input.txt')
# This will be a global variable so that we can keep on ierating further and further once we process the tree
currentNumberIndex = 0

def getNextNumberFromInput():
    # Modify global variables
    global currentNumberIndex
    global inputNumbers
    # Bump index
    currentNumberIndex += 1
    # Return previous item
    return inputNumbers[currentNumberIndex - 1]

def createTree():
    # Get amount of children
    children_count = getNextNumberFromInput()
    # Get amount of metadata entries
    metadata_entries_count = getNextNumberFromInput()
    # Children per node
    children = []
    # Metadatas per node
    metadata = []
    for single_child in range(children_count):
        # when we have children then recursively create subtree
        children.append(createTree())
    for single_metadata in range(metadata_entries_count):
        # when there are metadata entries, just keep on reading next and next number from inputs
        metadata.append(getNextNumberFromInput())
    return (children, metadata)

def sumTotalMetadata(tree):
    total = 0
    # children are always in 0 index while metadatas are in 1 index
    (children, metadatas) = tree
    # First, sum everything what is in metadata to total sum
    total += sum(metadatas)
    # Now go throught ever child and recursively calculate metadatas of that
    for singleChild in children:
        total += sumTotalMetadata(singleChild)
    return total

def valueOfTree(tree):
    (children, metadatas) = tree
    # If there are no children, just sum all of metadata
    if len(children) == 0:
        return sum(metadatas)
    else:
        totalSub = 0
        for singleMetadata in metadatas:
            # 0 metadata entries are not counted so metadata needs to be at least 1 or greater
            # and metadata must actually exists
            # so we need to check if given metadata is below the length
            if singleMetadata >= 1 and singleMetadata <= len(children):
                totalSub += valueOfTree(children[singleMetadata - 1])
        return totalSub
def main():
    # This will contain created tree
    tree = createTree()

    # Part 1
    print(sumTotalMetadata(tree))

    # Part 2
    print(valueOfTree(tree))

main()