const lineReader = require("readline");
const fs = require("fs");
const firewallAlgo = require("./firewallAlgo");
let lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  lines.push(singleLine);
});

lineReaderInterface.on("close", () => {
  const dataObject = firewallAlgo.parseInput(lines);
  const totalSeverity = firewallAlgo.runSimulation(dataObject);
  const delay = firewallAlgo.calculateDelayToRunWithoutDetection(dataObject);
  console.log(totalSeverity);
  console.log(delay);
});
