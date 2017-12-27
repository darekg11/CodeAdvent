const lineReader = require("readline");
const fs = require("fs");
const programAlgo = require("./programAlgo");
let lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  lines.push(singleLine);
});

lineReaderInterface.on("close", () => {
  const dataObject = programAlgo.parseInput(lines);
  const programsThatCommunicateWithProgramZero = programAlgo.findNumberOfProgramsCommunicatingWithProgramZero(
    dataObject
  );
  console.log(programsThatCommunicateWithProgramZero);

  const allGroupsCount = programAlgo.countAllPossibleGroups(dataObject);
  console.log(allGroupsCount);
});
