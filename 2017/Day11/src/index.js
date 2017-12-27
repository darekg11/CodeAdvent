const lineReader = require("readline");
const fs = require("fs");
const hexAlgo = require("./hexAlgo");
let line = "";

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  line = singleLine;
});

lineReaderInterface.on("close", () => {
  const mappedToSeparateString = line.split(",");
  const info = hexAlgo.calculateMinimumAmmountOfSteps(mappedToSeparateString);
  console.log(info.minimumSteps);
  console.log(info.furthestPosition);
});
