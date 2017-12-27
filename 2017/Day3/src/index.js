const memoryAlgoSolver = require("./memoryAlgoSolver");

const puzzleResult = memoryAlgoSolver.getDistanceSpiralingOutwardUp(368078);

console.log(puzzleResult);

const puzzleResultAdjacent = memoryAlgoSolver.getFirstLargerOutputThanCombinedAdjacentValuesOfEachCell(
  368078
);

console.log(puzzleResultAdjacent);
