const getIndexWrappingList = (destinationIndex, arrayLength) => {
  return destinationIndex >= arrayLength
    ? destinationIndex % arrayLength
    : destinationIndex;
};

const substringListWithWrapping = (list, startIndex, endIndex) => {
  let substringedArray = [];
  let currentIndex = getIndexWrappingList(startIndex, list.length);
  do {
    currentIndex = getIndexWrappingList(currentIndex, list.length);
    substringedArray.push(list[currentIndex]);
    currentIndex += 1;
  } while (currentIndex !== endIndex + 1);
  return substringedArray;
};

const insertSubListToList = (originalList, subList, startIndex, endIndex) => {
  let replacedList = [...originalList];
  let currentIndex = getIndexWrappingList(startIndex, originalList.length);
  for (let cnt = 0; cnt < subList.length; cnt += 1, currentIndex += 1) {
    currentIndex = getIndexWrappingList(currentIndex, originalList.length);
    replacedList[currentIndex] = subList[cnt];
  }
  return replacedList;
};

const hashInput = (hashingValues, inputArray, rounds) => {
  let hashingValuesCopy = [...hashingValues];
  let currentPosition = 0;
  let skipSize = 0;
  let roundNumber = 0;
  for (let roundCnt = 0; roundCnt < rounds; roundCnt += 1) {
    inputArray.forEach(element => {
      const reverseIndexStart = getIndexWrappingList(
        currentPosition,
        hashingValuesCopy.length
      );
      const reverseIndexEnd = getIndexWrappingList(
        element === 0 ? currentPosition : currentPosition + element - 1,
        hashingValuesCopy.length
      );
      const substringedArray = substringListWithWrapping(
        hashingValuesCopy,
        reverseIndexStart,
        reverseIndexEnd
      );
      const substringedReverse = substringedArray.reverse();
      hashingValuesCopy = insertSubListToList(
        hashingValuesCopy,
        substringedReverse,
        reverseIndexStart,
        reverseIndexEnd
      );
      currentPosition = getIndexWrappingList(
        currentPosition + element + skipSize,
        hashingValues.length
      );
      skipSize += 1;
    });
  }
  return hashingValuesCopy;
};

const calculateDenseHash = input => {
  let result = [];
  for (let cnt = 0; cnt < 16; cnt += 1) {
    const block = input.slice(cnt * 16, (cnt + 1) * 16);
    result.push(block.reduce((a, b) => a ^ b));
  }
  return result;
};
const getHexRepresentation = denseHash => {
  return denseHash
    .map(singleNumber => {
      const hexRepresntation = singleNumber.toString(16);
      if (hexRepresntation.length === 1) {
        return "0" + hexRepresntation;
      }
      return hexRepresntation;
    })
    .join("");
};

exports.getIndexWrappingList = getIndexWrappingList;
exports.substringListWithWrapping = substringListWithWrapping;
exports.insertSubListToList = insertSubListToList;
exports.hashInput = hashInput;
exports.calculateDenseHash = calculateDenseHash;
exports.getHexRepresentation = getHexRepresentation;
