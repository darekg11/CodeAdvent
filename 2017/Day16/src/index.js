const _ = require("lodash");
const lineReader = require("readline");
const fs = require("fs");
const performance = require("performance-now");
const danceAlgo = require("./danceAlgo");
let line = "";

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  line = singleLine;
});

lineReaderInterface.on("close", () => {
  const outputSequence = danceAlgo.dance(line, 1);
  console.log(outputSequence);

  const cyclicSequence = danceAlgo.dance(line, 1000000000);
  console.log(cyclicSequence);
});
