const DIRECTION_UP = "UP";
const DIRECTION_DOWN = "DOWN";
const DIRECTION_RIGHT = "RIGHT";
const DIRECTION_LEFT = "LEFT";

const move = (currentPositionVector, direction, counter) => {
  switch (direction) {
    case DIRECTION_UP:
      return {
        x: currentPositionVector.x,
        y: currentPositionVector.y + 1
      };
    case DIRECTION_DOWN:
      return {
        x: currentPositionVector.x,
        y: currentPositionVector.y - 1
      };
    case DIRECTION_RIGHT:
      return {
        x: currentPositionVector.x + 1,
        y: currentPositionVector.y
      };
    case DIRECTION_LEFT:
      return {
        x: currentPositionVector.x - 1,
        y: currentPositionVector.y
      };
  }
};

const moveInSingleDirection = (currentPositon, direction) => {
  const endPosition = move(currentPositon, direction);
  return endPosition;
};

const moveRepeatlyInSingleDirection = (
  cellsMap,
  repeats,
  currentPositon,
  direction,
  valueCallback
) => {
  let finalCellsMap = cellsMap;
  let finalPosition = currentPositon;
  for (let cnt = 0; cnt < repeats; cnt += 1) {
    const newCellPosition = moveInSingleDirection(finalPosition, direction);
    finalCellsMap.push({
      x: newCellPosition.x,
      y: newCellPosition.y,
      value: valueCallback(finalCellsMap, newCellPosition, cnt + 1)
    });
    finalPosition = newCellPosition;
  }
  return { cellsMap: finalCellsMap, position: finalPosition };
};

const calculateRequiredDistanceToStartPosition = from2DPosition => {
  return Math.abs(from2DPosition.x) + Math.abs(from2DPosition.y);
};

const getDistanceSpiralingOutwardUp = destinationMemoryCell => {
  let cellsMap = [
    {
      x: 0,
      y: 0,
      value: 1
    }
  ];
  let counter = 1;
  let currentPoint2DCoords = { x: 0, y: 0 };
  let repeatStepsCounter = 1;

  const valueCallback = (cellsMapData, position, loopCounter) => {
    return counter + loopCounter;
  };

  while (counter <= destinationMemoryCell) {
    let result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_RIGHT,
      valueCallback
    );
    cellsMap = result.cellsMap;
    currentPoint2DCoords = result.position;
    counter += repeatStepsCounter;

    result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_UP,
      valueCallback
    );
    cellsMap = result.cellsMap;
    currentPoint2DCoords = result.position;
    counter += repeatStepsCounter;

    repeatStepsCounter += 1;

    result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_LEFT,
      valueCallback
    );
    cellsMap = result.cellsMap;
    currentPoint2DCoords = result.position;
    counter += repeatStepsCounter;

    result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_DOWN,
      valueCallback
    );
    cellsMap = result.cellsMap;
    currentPoint2DCoords = result.position;
    counter += repeatStepsCounter;

    repeatStepsCounter += 1;
  }

  const desiredCellByValue = cellsMap.find(
    cell => cell.value === destinationMemoryCell
  );
  return calculateRequiredDistanceToStartPosition({
    x: desiredCellByValue.x,
    y: desiredCellByValue.y
  });
};

const calculateCellValue = (cellsMap, desiredCell2DCoords) => {
  const transformationMatrix = [
    { x: 1, y: 0 },
    { x: 1, y: 1 },
    { x: 0, y: 1 },
    { x: -1, y: 1 },
    { x: -1, y: 0 },
    { x: -1, y: -1 },
    { x: 0, y: -1 },
    { x: 1, y: -1 }
  ];
  let cellValue = 0;
  transformationMatrix.forEach(singleTransformation => {
    const neighborCell = cellsMap.find(singleCell => {
      return (
        singleCell.x === desiredCell2DCoords.x + singleTransformation.x &&
        singleCell.y === desiredCell2DCoords.y + singleTransformation.y
      );
    });
    if (neighborCell !== undefined) {
      cellValue += neighborCell.value;
    }
  });
  return cellValue;
};

const getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell = thresholdValue => {
  let largestValue = 1;
  let currentPoint2DCoords = { x: 0, y: 0 };
  let cellsMap = [
    {
      x: currentPoint2DCoords.x,
      y: currentPoint2DCoords.y,
      value: 1
    }
  ];
  let repeatStepsCounter = 1;

  const valueCallback = (cellMapsData, destinationCell2DCoords) => {
    return calculateCellValue(cellMapsData, destinationCell2DCoords);
  };

  while (largestValue <= thresholdValue) {
    let result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_RIGHT,
      valueCallback
    );
    currentPoint2DCoords = result.position;
    cellsMap = result.cellsMap;

    result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_UP,
      valueCallback
    );
    currentPoint2DCoords = result.position;
    cellsMap = result.cellsMap;

    repeatStepsCounter += 1;

    result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_LEFT,
      valueCallback
    );
    currentPoint2DCoords = result.position;
    cellsMap = result.cellsMap;

    result = moveRepeatlyInSingleDirection(
      cellsMap,
      repeatStepsCounter,
      currentPoint2DCoords,
      DIRECTION_DOWN,
      valueCallback
    );
    currentPoint2DCoords = result.position;
    cellsMap = result.cellsMap;
    largestValue = cellsMap[cellsMap.length - 1].value;

    repeatStepsCounter += 1;
  }

  let firstLargestAfterThreshold = largestValue;
  for (cnt = cellsMap.length - 1; cnt >= 0; cnt -= 1) {
    if (cellsMap[cnt].value - thresholdValue <= 0) {
      firstLargestAfterThreshold = cellsMap[cnt + 1].value;
      break;
    }
  }
  return firstLargestAfterThreshold;
};

exports.getDistanceSpiralingOutwardUp = getDistanceSpiralingOutwardUp;
exports.getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell = getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell;
