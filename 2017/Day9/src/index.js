const lineReader = require("readline");
const fs = require("fs");
const streamAlgo = require("./streamAlgo");
let line = "";

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  line = singleLine;
});

lineReaderInterface.on("close", () => {
  const score = streamAlgo.countInputGroupScore(line);
  const garbageCount = streamAlgo.countGarbageCount(line);
  console.log(score);
  console.log(garbageCount);
});
