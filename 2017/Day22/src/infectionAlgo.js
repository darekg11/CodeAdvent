const _ = require("lodash");

const UP = "UP";
const DOWN = "DOWN";
const LEFT = "LEFT";
const RIGHT = "RIGHT";

const CLEAN = 0;
const INFECTED = 1;
const WEAKENED = 2;
const FLAGGED = 3;

const parseSingleLine = singleLine => {
  return singleLine.split("").map(character => (character === "#" ? 1 : 0));
};

const parseInput = lines => {
  const rows = [];
  lines.forEach(singleLine => {
    rows.push(parseSingleLine(singleLine));
  });
  return rows;
};

const createInitialGridFromMap = initialMap => {
  let map = {};
  for (let rowCnt = 0; rowCnt < initialMap.length; rowCnt += 1) {
    for (let colCnt = 0; colCnt < initialMap[rowCnt].length; colCnt += 1) {
      map[
        colCnt -
          Math.floor(initialMap[rowCnt].length / 2) +
          "," +
          (rowCnt - Math.floor(initialMap.length / 2))
      ] =
        initialMap[rowCnt][colCnt];
    }
  }
  return map;
};

const turnLeft = currentDirection => {
  switch (currentDirection) {
    case UP: {
      return LEFT;
    }
    case LEFT: {
      return DOWN;
    }
    case DOWN: {
      return RIGHT;
    }
    case RIGHT: {
      return UP;
    }
  }
};

const turnRight = currentDirection => {
  switch (currentDirection) {
    case UP: {
      return RIGHT;
    }
    case LEFT: {
      return UP;
    }
    case DOWN: {
      return LEFT;
    }
    case RIGHT: {
      return DOWN;
    }
  }
};

const move = (direction, currentPosition) => {
  switch (direction) {
    case UP: {
      return {
        x: currentPosition.x,
        y: currentPosition.y - 1
      };
    }
    case DOWN: {
      return {
        x: currentPosition.x,
        y: currentPosition.y + 1
      };
    }
    case LEFT: {
      return {
        x: currentPosition.x - 1,
        y: currentPosition.y
      };
    }
    case RIGHT: {
      return {
        x: currentPosition.x + 1,
        y: currentPosition.y
      };
    }
  }
};

const solveFirstPart = (initialMap, bursts) => {
  let map = createInitialGridFromMap(initialMap);
  let x = 0;
  let y = 0;
  let infectedCellsCount = 0;
  let currentDirection = UP;
  for (let burstCnt = 0; burstCnt < bursts; burstCnt += 1) {
    const currentNode = map[x + "," + y];
    //infected
    if (currentNode === 1) {
      currentDirection = turnRight(currentDirection);
      map[x + "," + y] = 0;
    } else {
      currentDirection = turnLeft(currentDirection);
      map[x + "," + y] = 1;
      infectedCellsCount += 1;
    }
    const newPosition = move(currentDirection, { x: x, y: y });
    x = newPosition.x;
    y = newPosition.y;
  }
  return infectedCellsCount;
};

const solveSecondPart = (initialMap, bursts) => {
  let map = createInitialGridFromMap(initialMap);
  let x = 0;
  let y = 0;
  let infectedCellsCount = 0;
  let currentDirection = UP;
  for (let burstCnt = 0; burstCnt < bursts; burstCnt += 1) {
    const currentNode = map[x + "," + y];
    if (_.isUndefined(currentNode) || currentNode === CLEAN) {
      currentDirection = turnLeft(currentDirection);
      map[x + "," + y] = WEAKENED;
    } else if (currentNode === WEAKENED) {
      currentDirection = currentDirection;
      map[x + "," + y] = INFECTED;
      infectedCellsCount += 1;
    } else if (currentNode === INFECTED) {
      currentDirection = turnRight(currentDirection);
      map[x + "," + y] = FLAGGED;
    } else if (currentNode === FLAGGED) {
      currentDirection = turnLeft(currentDirection);
      currentDirection = turnLeft(currentDirection);
      map[x + "," + y] = CLEAN;
    }
    const newPosition = move(currentDirection, { x: x, y: y });
    x = newPosition.x;
    y = newPosition.y;
  }
  return infectedCellsCount;
};

exports.parseInput = parseInput;
exports.createInitialGridFromMap = createInitialGridFromMap;
exports.solveFirstPart = solveFirstPart;
exports.solveSecondPart = solveSecondPart;
