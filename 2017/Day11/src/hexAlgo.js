const _ = require("lodash");

const calculateMinimumAmmountOfSteps = inputMovements => {
  const allPositions = [];

  let currentPosition = {
    x: 0,
    y: 0
  };

  inputMovements.forEach(singleMovement => {
    if (singleMovement === "n") {
      currentPosition.y -= 1;
    }
    if (singleMovement === "s") {
      currentPosition.y += 1;
    }
    if (singleMovement === "nw") {
      currentPosition.x -= 1;
    }
    if (singleMovement === "sw") {
      currentPosition.x -= 1;
      currentPosition.y += 1;
    }
    if (singleMovement === "se") {
      currentPosition.x += 1;
    }
    if (singleMovement === "ne") {
      currentPosition.x += 1;
      currentPosition.y -= 1;
    }
    allPositions.push({ ...currentPosition });
  });
  const finalPosition = allPositions[allPositions.length - 1];
  const minimumSteps =
    (Math.abs(currentPosition.x) +
      Math.abs(currentPosition.y) +
      Math.abs(currentPosition.x + currentPosition.y)) /
    2;
  const furthestPosition = _.max(
    allPositions.map(singlePosition => {
      return (
        (Math.abs(singlePosition.x) +
          Math.abs(singlePosition.y) +
          Math.abs(singlePosition.x + singlePosition.y)) /
        2
      );
    })
  );
  return {
    minimumSteps: minimumSteps,
    furthestPosition: furthestPosition
  };
};

exports.calculateMinimumAmmountOfSteps = calculateMinimumAmmountOfSteps;
