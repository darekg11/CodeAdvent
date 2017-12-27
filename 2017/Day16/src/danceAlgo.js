const _ = require("lodash");

const spin = (danceState, danceMove) => {
  const copyDanceState = danceState.slice();
  const spinIndex = danceMove.firstArgument;
  const programsToMoveToFront = copyDanceState.substring(
    copyDanceState.length - spinIndex
  );
  const programsToLeaveAsItIs = copyDanceState.substring(
    0,
    copyDanceState.length - spinIndex
  );
  return programsToMoveToFront + programsToLeaveAsItIs;
};

const exchange = (danceState, exchangeOperation) => {
  const danceStateAsArray = [...danceState];
  const tempDanceCharacter = danceStateAsArray[exchangeOperation.firstArgument];
  danceStateAsArray[exchangeOperation.firstArgument] =
    danceStateAsArray[exchangeOperation.secondArgument];
  danceStateAsArray[exchangeOperation.secondArgument] = tempDanceCharacter;
  return danceStateAsArray.join("");
};

const partner = (danceState, partnerOperation) => {
  const danceStateAsArray = [...danceState];
  const indexOfFirstProgram = danceState.indexOf(
    partnerOperation.firstArgument
  );
  const indexOfSecondProgram = danceState.indexOf(
    partnerOperation.secondArgument
  );
  const firstProgram = danceState[indexOfFirstProgram];
  const secondProgram = danceState[indexOfSecondProgram];

  danceStateAsArray[indexOfFirstProgram] = secondProgram;
  danceStateAsArray[indexOfSecondProgram] = firstProgram;

  return danceStateAsArray.join("");
};

const executeDance = (danceState, danceMove) => {
  const danceStateCopy = danceState.slice();
  if (danceMove.operation === "SPIN") {
    return spin(danceStateCopy, danceMove);
  }

  if (danceMove.operation === "EXCHANGE") {
    return exchange(danceStateCopy, danceMove);
  }

  if (danceMove.operation === "PARTNER") {
    return partner(danceStateCopy, danceMove);
  }
};

const parseSingleLine = singleLine => {
  let operationObject = {};
  const operationMark = singleLine[0];
  if (operationMark === "s") {
    operationObject.operation = "SPIN";
    operationObject.firstArgument = Number(singleLine.substring(1));
  }

  if (operationMark === "x") {
    const separateObjectIndex = singleLine.indexOf("/");
    operationObject.operation = "EXCHANGE";
    operationObject.firstArgument = Number(
      singleLine.substring(1, separateObjectIndex)
    );
    operationObject.secondArgument = Number(
      singleLine.substring(separateObjectIndex + 1)
    );
  }

  if (operationMark === "p") {
    operationObject.operation = "PARTNER";
    operationObject.firstArgument = singleLine[1];
    operationObject.secondArgument = singleLine[3];
  }
  return operationObject;
};

const parseInput = string => {
  const operations = [];
  const strings = string.split(",");
  strings.forEach(singleString => {
    const operation = parseSingleLine(singleString);
    operations.push(operation);
  });
  return operations;
};

const dance = (stringInput, rounds) => {
  let danceState = "abcdefghijklmnop";
  let sequences = [];
  const operations = parseInput(stringInput);
  const operationsLength = operations.length;
  for (let cnt = 0; cnt < rounds; cnt += 1) {
    for (
      let operationCnt = 0;
      operationCnt < operationsLength;
      operationCnt += 1
    ) {
      danceState = executeDance(danceState, operations[operationCnt]);
    }
    //check for cyclic values to not calcualting 1000000000 values
    if (_.includes(sequences, danceState)) {
      return sequences[rounds % cnt - 1];
    }
    sequences.push(danceState);
  }
  return danceState;
};

const danceNumbers = (stringInput, rounds) => {
  let danceState = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
  const operations = parseInput(stringInput);
  const operationsLength = operations.length;
  for (let cnt = 0; cnt < rounds; cnt += 1) {
    for (
      let operationCnt = 0;
      operationCnt < operationsLength;
      operationCnt += 1
    ) {
      executeDanceNumber(danceState, operations[operationCnt]);
    }
  }
  return danceState;
};

const formatOutput = numbers => {
  const mapping = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p"
  };

  return numbers.map(singleNumber => mapping[singleNumber]).join("");
};

exports.parseInput = parseInput;
exports.spin = spin;
exports.exchange = exchange;
exports.partner = partner;
exports.dance = dance;
exports.danceNumbers = danceNumbers;
exports.formatOutput = formatOutput;
