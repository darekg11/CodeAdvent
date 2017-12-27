const lineReader = require("readline");
const fs = require("fs");
const cpuOperationAlgo = require("./cpuOperationsAlgo");
const lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", line => {
  lines.push(line);
});

lineReaderInterface.on("close", () => {
  const cpuInstructions = cpuOperationAlgo.parseInput(lines);
  const result = cpuOperationAlgo.executeProgram(cpuInstructions);
  const maximumValueInRegisters = cpuOperationAlgo.findRegisterWithMaximumValue(
    result.registers
  );
  console.log(maximumValueInRegisters);
  console.log(result.highestValueEver);
});
