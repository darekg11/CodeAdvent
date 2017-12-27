const _ = require("lodash");

const parseInput = lines => {
  let finalObject = {};
  lines.forEach(singleLine => {
    const splitted = singleLine.split(":");
    const depth = Number(splitted[0]);
    const range = Number(splitted[1].substring(1));
    const newObject = {};
    newObject[depth] = range;
    finalObject = _.merge(finalObject, newObject);
  });
  return finalObject;
};

const runSimulation = dataObject => {
  let totalSeverity = 0;
  let currentStep = -1;
  let simulationStatus = {};
  _.forEach(dataObject, (value, key) => {
    let newObject = {};
    newObject[key] = {
      range: value,
      currentIndex: 0,
      direction: "UP"
    };
    simulationStatus = _.merge(simulationStatus, newObject);
  });

  let stepsCount = _.max(_.keys(dataObject).map(Number));

  for (let cnt = 0; cnt <= stepsCount; cnt += 1) {
    currentStep += 1;
    if (
      simulationStatus[currentStep] &&
      simulationStatus[currentStep].currentIndex === 0
    ) {
      totalSeverity += currentStep * simulationStatus[currentStep].range;
    }
    _.forEach(simulationStatus, (value, key) => {
      if (value.direction === "UP") {
        value.currentIndex += 1;
      }
      if (value.direction === "DOWN") {
        value.currentIndex -= 1;
      }
      if (value.currentIndex === value.range - 1) {
        value.direction = "DOWN";
      }
      if (value.currentIndex === 0) {
        value.direction = "UP";
      }
    });
  }
  return totalSeverity;
};

const calculateDelayToRunWithoutDetection = dataObject => {
  let delay = 0;
  let stepsCount = _.max(_.keys(dataObject).map(Number));
  let found = false;

  while (!found) {
    found = true;
    for (cnt = 0; cnt <= stepsCount; cnt += 1) {
      if (!dataObject[cnt]) {
        continue;
      }
      // formula for calculating if position of tracker is going to be at index 0 including delay and step is as follows:
      // (step + delay) % ( (range - 1) * 2)
      // if above is equal to 0 that means we are caught
      // brutefore was too slow : (
      const totalDelay = cnt + delay;
      const layerDividier = (dataObject[cnt] - 1) * 2;
      const isZeroIndex = totalDelay % layerDividier === 0;
      if (isZeroIndex) {
        delay++;
        found = false;
        break;
      }
    }
  }
  return delay;
};

exports.parseInput = parseInput;
exports.runSimulation = runSimulation;
exports.calculateDelayToRunWithoutDetection = calculateDelayToRunWithoutDetection;
