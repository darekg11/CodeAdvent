const _ = require("lodash");
const hashAlgo = require("./hashAlgo");

const hexValueToBinary = hexValue => {
  const mapping = {
    0: "0000",
    1: "0001",
    2: "0010",
    3: "0011",
    4: "0100",
    5: "0101",
    6: "0110",
    7: "0111",
    8: "1000",
    9: "1001",
    a: "1010",
    b: "1011",
    c: "1100",
    d: "1101",
    e: "1110",
    f: "1111"
  };
  let binaryValues = "";
  for (let cnt = 0; cnt < hexValue.length; cnt += 1) {
    binaryValues += mapping[hexValue[cnt]];
  }
  return binaryValues;
};

const getBinaryValue = (hashKey, row) => {
  const actualHash = hashKey + "-" + row;
  const stringInputAsciiCodes = actualHash
    .split("")
    .map(singlElement => singlElement.charCodeAt())
    .concat([17, 31, 73, 47, 23]);

  const resultMuchRounds = hashAlgo.hashInput(
    [...Array(256).keys()],
    stringInputAsciiCodes,
    64
  );

  const denseHash = hashAlgo.calculateDenseHash(resultMuchRounds);
  const hexValue = hashAlgo.getHexRepresentation(denseHash);
  const binaryValue = hexValueToBinary(hexValue);
  return binaryValue;
};

const getUsedAndEmptyGridCellsCount = binaryValue => {
  const counted = _.countBy(binaryValue);
  return {
    used: counted["1"],
    free: counted["0"]
  };
};

const findGroup = (grid, labelingMarker, row, col) => {
  if (grid[row] && grid[row][col] && grid[row][col] === 1) {
    grid[row][col] = labelingMarker;
    //down
    findGroup(grid, labelingMarker, row + 1, col);
    //right
    findGroup(grid, labelingMarker, row, col + 1);
    //left
    findGroup(grid, labelingMarker, row, col - 1);
    //up
    findGroup(grid, labelingMarker, row - 1, col);
    return true;
  }
  return false;
};

const countGroups = grid => {
  const gridCopy = [...grid];
  for (let cnt = 0; cnt < 128; cnt += 1) {
    gridCopy.push(grid[cnt].split("").map(Number));
  }

  //needs to something else than 0 or 1
  let groupLabelingIndex = 2;
  let groupCount = 0;

  for (let row = 0; row < gridCopy.length; row += 1) {
    const singleRow = gridCopy[row];
    for (let col = 0; col < singleRow.length; col += 1) {
      if (findGroup(gridCopy, groupLabelingIndex, row, col)) {
        groupLabelingIndex += 1;
        groupCount += 1;
      }
    }
  }
  return groupCount;
};

exports.getBinaryValue = getBinaryValue;
exports.getUsedAndEmptyGridCellsCount = getUsedAndEmptyGridCellsCount;
exports.countGroups = countGroups;
