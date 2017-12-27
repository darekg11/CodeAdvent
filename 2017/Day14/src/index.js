const defragmenterAlgo = require("./defragmenterAlgo");

let usedSum = 0;
const binaryValues = [];

for (let cnt = 0; cnt < 128; cnt += 1) {
  const binary = defragmenterAlgo.getBinaryValue("stpzcrnm", cnt);
  binaryValues.push(binary);
  const result = defragmenterAlgo.getUsedAndEmptyGridCellsCount(binary);
  usedSum += result.used;
}

const groupCount = defragmenterAlgo.countGroups(binaryValues);
console.log(groupCount);
console.log(usedSum);
