const areTwoMemorySequencesEqual = (
  firstMemorySequence,
  secondMemorySequence
) => {
  if (firstMemorySequence.length !== secondMemorySequence.length) {
    return false;
  }

  for (let cnt = 0; cnt < firstMemorySequence.length; cnt += 1) {
    if (firstMemorySequence[cnt] !== secondMemorySequence[cnt]) {
      return false;
    }
  }
  return true;
};

const isMemoryBlocksSequenceUnique = (
  memoryBlockToCheck,
  uniqueMemoryBlocks
) => {
  for (let cnt = 0; cnt < uniqueMemoryBlocks.length; cnt += 1) {
    const memoryBlockToCheckAgainst = uniqueMemoryBlocks[cnt];
    if (
      areTwoMemorySequencesEqual(memoryBlockToCheck, memoryBlockToCheckAgainst)
    ) {
      return false;
    }
  }
  return true;
};

const traverseArrayAndIncreaseEachNextValue = (
  memoryBlocks,
  startIndex,
  allocationValue
) => {
  const arrayCopy = [...memoryBlocks];
  let allocationValueCopy = allocationValue;
  let currentTraverseIndex = startIndex + 1;
  arrayCopy[startIndex] = 0;
  while (allocationValueCopy > 0) {
    if (currentTraverseIndex >= arrayCopy.length) {
      currentTraverseIndex = 0;
    }
    arrayCopy[currentTraverseIndex] += 1;
    allocationValueCopy -= 1;
    currentTraverseIndex += 1;
  }
  return arrayCopy;
};

const findLargestMemoryBlockInSequenceWithLowestIndex = memoryBlocks => {
  let memoryBlockIndexWithLargestValue = 0;
  let largestMemoryBlockAllocationValue = 0;

  for (let cnt = 0; cnt < memoryBlocks.length; cnt += 1) {
    if (memoryBlocks[cnt] > largestMemoryBlockAllocationValue) {
      memoryBlockIndexWithLargestValue = cnt;
      largestMemoryBlockAllocationValue = memoryBlocks[cnt];
    }
  }
  return memoryBlockIndexWithLargestValue;
};

const countRequiredCyclesToFindDuplicatedSequence = memoryBlocks => {
  let memoryBlocksCopy = [...memoryBlocks];
  const uniqueSequences = [];
  let requiredCycles = 0;
  let foundDuplicatedSequence = false;

  while (!foundDuplicatedSequence) {
    const largestMemoryBlockIndex = findLargestMemoryBlockInSequenceWithLowestIndex(
      memoryBlocksCopy
    );
    const memoryAllocations = memoryBlocksCopy[largestMemoryBlockIndex];
    memoryBlocksCopy = traverseArrayAndIncreaseEachNextValue(
      memoryBlocksCopy,
      largestMemoryBlockIndex,
      memoryAllocations
    );
    if (isMemoryBlocksSequenceUnique(memoryBlocksCopy, uniqueSequences)) {
      uniqueSequences.push(memoryBlocksCopy);
      requiredCycles += 1;
    } else {
      foundDuplicatedSequence = true;
    }
  }
  return requiredCycles + 1;
};

const countRequiredCyclesToFindDuplicatedSequenceIncludingAmmountOfCyclesBetweenUniqueAndDuplicate = memoryBlocks => {
  let memoryBlocksCopy = [...memoryBlocks];
  const uniqueSequences = [];
  let requiredCycles = 0;
  let difference = 0;
  let foundDuplicatedSequence = false;

  while (!foundDuplicatedSequence) {
    const largestMemoryBlockIndex = findLargestMemoryBlockInSequenceWithLowestIndex(
      memoryBlocksCopy
    );
    const memoryAllocations = memoryBlocksCopy[largestMemoryBlockIndex];
    memoryBlocksCopy = traverseArrayAndIncreaseEachNextValue(
      memoryBlocksCopy,
      largestMemoryBlockIndex,
      memoryAllocations
    );
    if (
      isMemoryBlocksSequenceUnique(
        memoryBlocksCopy,
        uniqueSequences.map(singleInfo => singleInfo.block)
      )
    ) {
      uniqueSequences.push({
        block: memoryBlocksCopy,
        cycle: requiredCycles
      });
      requiredCycles += 1;
    } else {
      const memoryBlockCycleFirstAppear = uniqueSequences.find(singleBlock => {
        return areTwoMemorySequencesEqual(singleBlock.block, memoryBlocksCopy);
      });
      difference = requiredCycles - memoryBlockCycleFirstAppear.cycle;
      foundDuplicatedSequence = true;
    }
  }
  return difference;
};

exports.countRequiredCyclesToFindDuplicatedSequence = countRequiredCyclesToFindDuplicatedSequence;
exports.countRequiredCyclesToFindDuplicatedSequenceIncludingAmmountOfCyclesBetweenUniqueAndDuplicate = countRequiredCyclesToFindDuplicatedSequenceIncludingAmmountOfCyclesBetweenUniqueAndDuplicate;
