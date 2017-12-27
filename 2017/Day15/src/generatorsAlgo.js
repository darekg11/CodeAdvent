const _ = require("lodash");

const runGenerator = (startingValueA, startingValueB, factorA, factorB) => {
  let matchCount = 0;
  let firstGeneratorValue = startingValueA;
  let secondGeneratorValue = startingValueB;
  for (let cnt = 0; cnt < 40000000; cnt += 1) {
    firstGeneratorValue = (firstGeneratorValue * factorA) % 2147483647;
    secondGeneratorValue = (secondGeneratorValue * factorB) % 2147483647;
    firstGeneratorValueBinary = _.padStart(
      firstGeneratorValue.toString(2),
      32,
      "0"
    );
    secondGeneratorValueBinary = _.padStart(
      secondGeneratorValue.toString(2),
      32,
      "0"
    );
    firstGeneratorValueLowestBits = firstGeneratorValueBinary.substring(16);
    secondGeneratorValueLowestBits = secondGeneratorValueBinary.substring(16);
    if (firstGeneratorValueLowestBits === secondGeneratorValueLowestBits) {
      matchCount += 1;
    }
  }
  return matchCount;
};

const runPickyGenerator = (
  startingValueA,
  startingValueB,
  factorA,
  factorB
) => {
  let matchCount = 0;
  let firstGeneratorValue = startingValueA;
  let secondGeneratorValue = startingValueB;
  let pairsGeneratedCount = 0;
  let firstGeneratorBinaryValues = [];
  let secondGeneratorBinaryValues = [];
  while (firstGeneratorBinaryValues.length < 5000000) {
    firstGeneratorValue = (firstGeneratorValue * factorA) % 2147483647;
    if (firstGeneratorValue % 4 === 0) {
      const firstGeneratorValueBinary = _.padStart(
        firstGeneratorValue.toString(2),
        32,
        "0"
      );
      firstGeneratorBinaryValues.push(firstGeneratorValueBinary);
    }
  }

  while (secondGeneratorBinaryValues.length < 5000000) {
    secondGeneratorValue = (secondGeneratorValue * factorB) % 2147483647;
    if (secondGeneratorValue % 8 === 0) {
      const secondGeneratorValueBinary = _.padStart(
        secondGeneratorValue.toString(2),
        32,
        "0"
      );
      secondGeneratorBinaryValues.push(secondGeneratorValueBinary);
    }
  }

  for (let cnt = 0; cnt < 5000000; cnt += 1) {
    const firstGeneratorValueLowestBits = firstGeneratorBinaryValues[
      cnt
    ].substring(16);
    const secondGeneratorValueLowestBits = secondGeneratorBinaryValues[
      cnt
    ].substring(16);
    if (firstGeneratorValueLowestBits === secondGeneratorValueLowestBits) {
      matchCount += 1;
    }
  }

  return matchCount;
};

exports.runGenerator = runGenerator;
exports.runPickyGenerator = runPickyGenerator;
