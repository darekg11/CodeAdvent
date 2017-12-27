const lineReader = require("readline");
const fs = require("fs");
const fractalArtAlgo = require("./fractalArtAlgo");
const lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", singleLine => {
  lines.push(singleLine);
});

lineReaderInterface.on("close", () => {
  const patterns = fractalArtAlgo.parseInput(lines);
  const result = fractalArtAlgo.generateFractArt(patterns, 5);
  console.log(result);
});
