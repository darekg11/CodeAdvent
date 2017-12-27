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
  const result = operationsAlgo.executeProgram(lines);
  const multiResult = operationsAlgo.executeProgramTwiceAtTheSameTime(lines);
  console.log(result);
  console.log(multiResult);
});
