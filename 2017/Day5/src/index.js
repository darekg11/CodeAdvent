const lineReader = require("readline");
const fs = require("fs");
const offsetJumperAlgo = require("./offsetJumperAlgo");
const jumps = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", line => {
  jumps.push(Number(line));
});

lineReaderInterface.on("close", () => {
  console.log(offsetJumperAlgo.countRequiredJumpsToExitList(jumps));
  console.log(
    offsetJumperAlgo.countRequiredJumpsToExitListWithDecreasing(jumps)
  );
});
