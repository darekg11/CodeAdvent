const lineReader = require("readline");
const fs = require("fs");
const componentsAlgo = require("./componentsAlgo");

const lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  lines.push(singleLine);
});

lineReaderInterface.on("close", () => {
  const components = componentsAlgo.parseInput(lines);
  const bridgeInfo = componentsAlgo.bridgeInfo(components);
  console.log(bridgeInfo.strongest);
  console.log(bridgeInfo.strongestLongestBridge);
});
