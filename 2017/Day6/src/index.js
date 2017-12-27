const memoryAllocAlgo = require("./memoryAllocAlgo");

const requiredCycles = memoryAllocAlgo.countRequiredCyclesToFindDuplicatedSequence(
  [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
);

console.log(requiredCycles);

const requiredCyclesBetween = memoryAllocAlgo.countRequiredCyclesToFindDuplicatedSequenceIncludingAmmountOfCyclesBetweenUniqueAndDuplicate(
  [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
);

console.log(requiredCyclesBetween);
