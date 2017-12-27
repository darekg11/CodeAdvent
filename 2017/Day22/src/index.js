const lineReader = require("readline");
const fs = require("fs");
const infectionAlgo = require("./infectionAlgo");
const lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  lines.push(singleLine);
});

lineReaderInterface.on("close", () => {
  const initialMap = infectionAlgo.parseInput(lines);
  const resultPart1 = infectionAlgo.solveFirstPart(initialMap, 10000);
  const resultPart2 = infectionAlgo.solveSecondPart(initialMap, 10000000);
  console.log(resultPart1);
  console.log(resultPart2);
});
