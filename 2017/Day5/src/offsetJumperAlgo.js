const countRequiredJumpsToExitList = listOfJumps => {
  const listOfJumpsCopy = [...listOfJumps];
  const jumpArrayLength = listOfJumpsCopy.length;
  let currentIndex = 0;
  let nextJumpIndex = 0;
  let requiredJumps = 0;

  while (nextJumpIndex >= 0 && nextJumpIndex <= jumpArrayLength) {
    nextJumpIndex = currentIndex + listOfJumpsCopy[currentIndex];
    listOfJumpsCopy[currentIndex] = listOfJumpsCopy[currentIndex] += 1;
    currentIndex = nextJumpIndex;
    requiredJumps += 1;
  }
  return requiredJumps - 1;
};

const countRequiredJumpsToExitListWithDecreasing = listOfJumps => {
  const listOfJumpsCopy = [...listOfJumps];
  const jumpArrayLength = listOfJumpsCopy.length;
  let currentIndex = 0;
  let nextJumpIndex = 0;
  let requiredJumps = 0;

  while (nextJumpIndex >= 0 && nextJumpIndex <= jumpArrayLength) {
    nextJumpIndex = currentIndex + listOfJumpsCopy[currentIndex];
    const increaseValue = listOfJumpsCopy[currentIndex] >= 3 ? -1 : 1;
    listOfJumpsCopy[currentIndex] = listOfJumpsCopy[
      currentIndex
    ] += increaseValue;
    currentIndex = nextJumpIndex;
    requiredJumps += 1;
  }
  return requiredJumps - 1;
};

exports.countRequiredJumpsToExitList = countRequiredJumpsToExitList;
exports.countRequiredJumpsToExitListWithDecreasing = countRequiredJumpsToExitListWithDecreasing;
