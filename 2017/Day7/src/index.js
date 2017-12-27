const lineReader = require("readline");
const fs = require("fs");
const towerAlgo = require("./towerAlgo");
const lines = [];

const lineReaderInterface = lineReader.createInterface({
  input: fs.createReadStream("input.txt")
});

lineReaderInterface.on("line", line => {
  lines.push(line);
});

lineReaderInterface.on("close", () => {
  const towerData = towerAlgo.parseInput(lines);
  console.log(towerAlgo.findBottomTower(towerData.towerRelations));
  console.log(
    towerAlgo.findDifferenceToBalanceTower(
      towerData.towerWeights,
      towerData.towerRelations
    )
  );
});
