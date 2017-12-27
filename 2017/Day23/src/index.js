const lineReader = require("readline");
const fs = require("fs");
const operationsAlgo = require("./operationsAlgo");

const lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  lines.push(singleLine);
});

lineReaderInterface.on("close", () => {
  operationsAlgo.executeProgram(lines);
  operationsAlgo.findPrimesCnt(106700, 123700);
});
