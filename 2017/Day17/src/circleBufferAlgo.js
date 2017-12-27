const _ = require("lodash");

const getIndexWrappingList = (destinationIndex, arrayLength) => {
  return destinationIndex >= arrayLength
    ? destinationIndex % arrayLength
    : destinationIndex;
};

const startBuffering = stepSize => {
  const buffer = [0];
  let currentPositionIndex = 0;

  for (let cnt = 1; cnt < 2018; cnt += 1) {
    const destinationIndex = getIndexWrappingList(
      currentPositionIndex + stepSize,
      buffer.length
    );
    buffer.splice(destinationIndex + 1, 0, cnt);
    currentPositionIndex = destinationIndex + 1;
  }
  return buffer[currentPositionIndex + 1];
};

const findValueAfterZero = stepSize => {
  let currentSize = 1;
  let currentPosition = 0;
  let valueAfterZero = 0;

  for (let cnt = 1; cnt <= 50000000; cnt += 1) {
    const destinationIndex = getIndexWrappingList(
      currentPosition + stepSize,
      currentSize
    );
    //it is enough to simulate inserting and checking if we step on index 1.
    //If yes then we need to update top most value after 0 which is always at index 0!
    if (destinationIndex + 1 === 1) {
      valueAfterZero = cnt;
    }
    currentPosition = destinationIndex + 1;
    currentSize += 1;
  }
  return valueAfterZero;
};

exports.startBuffering = startBuffering;
exports.findValueAfterZero = findValueAfterZero;
