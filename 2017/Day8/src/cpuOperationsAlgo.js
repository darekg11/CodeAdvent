const _ = require("lodash");

const parseSingleLine = fileLine => {
  const parsedLines = fileLine.split(" ");
  return {
    destinationRegister: parsedLines[0],
    operation: parsedLines[1],
    value: Number(parsedLines[2]),
    leftOperandCondition: parsedLines[4],
    condition: parsedLines[5],
    rightOperandCondition: Number(parsedLines[6])
  };
};

const parseInput = fileLines => {
  const cpuInstructions = [];
  fileLines.forEach(singleLine => {
    cpuInstructions.push(parseSingleLine(singleLine));
  });
  return cpuInstructions;
};

const isConditionMet = (leftOperand, rightOperand, condition) => {
  switch (condition) {
    case ">":
      return leftOperand > rightOperand;
    case "<":
      return leftOperand < rightOperand;
    case ">=":
      return leftOperand >= rightOperand;
    case "<=":
      return leftOperand <= rightOperand;
    case "==":
      return leftOperand === rightOperand;
    case "!=":
      return leftOperand !== rightOperand;
  }
};

const isOperandRegister = operand => {
  return _.isString(operand);
};

const getValueFromRegister = (registers, register) => {
  return registers[register] || 0;
};

const putValueToRegister = (registers, destinationRegister, value) => {
  const registersCopy = _.cloneDeep(registers);
  registersCopy[destinationRegister] = value;
  return registersCopy;
};

const findRegisterWithMaximumValue = registers => {
  return _.chain(registers)
    .values()
    .max()
    .value();
};

const executeSingleOperation = (registers, singleOperation) => {
  let registersCopy = _.cloneDeep(registers);
  const leftOperandValue = isOperandRegister(
    singleOperation.leftOperandCondition
  )
    ? getValueFromRegister(registersCopy, singleOperation.leftOperandCondition)
    : singleOperation.leftOperandCondition;
  const rightOperandValue = isOperandRegister(
    singleOperation.rightOperandCondition
  )
    ? getValueFromRegister(singleOperation.rightOperandCondition)
    : singleOperation.rightOperandCondition;

  if (
    isConditionMet(
      leftOperandValue,
      rightOperandValue,
      singleOperation.condition
    )
  ) {
    const destinationRegisterCurrentValue = getValueFromRegister(
      registersCopy,
      singleOperation.destinationRegister
    );
    const operationValue = isOperandRegister(singleOperation.value)
      ? getValueFromRegister(singleOperation.value)
      : singleOperation.value;
    switch (singleOperation.operation) {
      case "inc": {
        newRegisterValue = destinationRegisterCurrentValue + operationValue;
        break;
      }
      case "dec": {
        newRegisterValue = destinationRegisterCurrentValue - operationValue;
        break;
      }
    }
    registersCopy = putValueToRegister(
      registersCopy,
      singleOperation.destinationRegister,
      newRegisterValue
    );
  }
  const highestValueInCycle = findRegisterWithMaximumValue(registersCopy);
  return {
    maximumValue: highestValueInCycle,
    registers: registersCopy
  };
};

const executeProgram = cpuInstructions => {
  let highestValueEver = 0;
  let registers = {};
  cpuInstructions.forEach(singleInstruction => {
    result = executeSingleOperation(registers, singleInstruction);
    registers = result.registers;
    if (result.maximumValue > highestValueEver) {
      highestValueEver = result.maximumValue;
    }
  });
  return { registers, highestValueEver };
};

exports.parseSingleLine = parseSingleLine;
exports.parseInput = parseInput;
exports.isConditionMet = isConditionMet;
exports.isOperandRegister = isOperandRegister;
exports.getValueFromRegister = getValueFromRegister;
exports.putValueToRegister = putValueToRegister;
exports.executeSingleOperation = executeSingleOperation;
exports.executeProgram = executeProgram;
exports.findRegisterWithMaximumValue = findRegisterWithMaximumValue;
