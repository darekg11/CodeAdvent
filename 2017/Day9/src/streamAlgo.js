const countInputGroupScore = input => {
  let isGarbageStreamOpened = false;
  let sum = 0;
  let currentScore = 0;

  for (let cnt = 0; cnt < input.length; cnt += 1) {
    switch (input[cnt]) {
      case "{": {
        if (!isGarbageStreamOpened) {
          currentScore += 1;
        }
        break;
      }
      case "}": {
        if (!isGarbageStreamOpened) {
          sum += currentScore;
          currentScore -= 1;
        }
        break;
      }
      case "!": {
        cnt += 1;
        break;
      }
      case "<": {
        isGarbageStreamOpened = true;
        break;
      }
      case ">": {
        isGarbageStreamOpened = false;
        break;
      }
      default: {
        break;
      }
    }
  }
  return sum;
};

const countGarbageCount = input => {
  let isGarbageStreamOpened = false;
  let garbageCount = 0;

  for (let cnt = 0; cnt < input.length; cnt += 1) {
    switch (input[cnt]) {
      case "{": {
        if (isGarbageStreamOpened) {
          garbageCount += 1;
        }
        break;
      }
      case "}": {
        if (isGarbageStreamOpened) {
          garbageCount += 1;
        }
        break;
      }
      case "!": {
        cnt += 1;
        break;
      }
      case "<": {
        if (isGarbageStreamOpened) {
          garbageCount += 1;
        }
        isGarbageStreamOpened = true;
        break;
      }
      case ">": {
        isGarbageStreamOpened = false;
        break;
      }
      default: {
        if (isGarbageStreamOpened) {
          garbageCount += 1;
        }
        break;
      }
    }
  }
  return garbageCount;
};

exports.countInputGroupScore = countInputGroupScore;
exports.countGarbageCount = countGarbageCount;
