const generatorsAlgo = require("./generatorsAlgo");

const matched = generatorsAlgo.runGenerator(277, 349, 16807, 48271);

console.log(matched);

const matchedPicky = generatorsAlgo.runPickyGenerator(277, 349, 16807, 48271);

console.log(matchedPicky);
