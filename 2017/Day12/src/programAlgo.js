const _ = require("lodash");
const graphlib = require("graphlib");

const parseSingleInputLine = singleInputLine => {
  const inputCopy = singleInputLine.slice();
  const firstSpaceIndex = inputCopy.indexOf(" ");
  const keyNumber = inputCopy.substring(0, firstSpaceIndex);
  const endMiddleCharacter = ">";
  const endMiddleCharacterIndex = inputCopy.indexOf(endMiddleCharacter);
  const childNumbersSubstring = inputCopy.substring(
    endMiddleCharacterIndex + 2
  );
  const childrens = childNumbersSubstring
    .split(", ")
    .map(singleEntry => Number(singleEntry));
  const returnObject = {};
  returnObject[keyNumber] = childrens;
  return returnObject;
};

const parseInput = input => {
  let finalObject = {};
  input.forEach(singleLine => {
    finalObject = _.merge(finalObject, parseSingleInputLine(singleLine));
  });
  return finalObject;
};

const findNumberOfProgramsCommunicatingWithProgramZero = inputDataObject => {
  const graph = new graphlib.Graph();
  _.forEach(inputDataObject, (value, key) => {
    _.forEach(value, singleValue => {
      graph.setEdge(key, singleValue);
    });
  });
  return graphlib.alg.components(graph).find(comp => comp.includes("0")).length;
};

const countAllPossibleGroups = inputDataObject => {
  const graph = new graphlib.Graph();
  _.forEach(inputDataObject, (value, key) => {
    _.forEach(value, singleValue => {
      graph.setEdge(key, singleValue);
    });
  });
  return graphlib.alg.components(graph).length;
};

exports.parseSingleInputLine = parseSingleInputLine;
exports.parseInput = parseInput;
exports.findNumberOfProgramsCommunicatingWithProgramZero = findNumberOfProgramsCommunicatingWithProgramZero;
exports.countAllPossibleGroups = countAllPossibleGroups;
