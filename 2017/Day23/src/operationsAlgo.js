const _ = require("lodash");

const parseSingleLine = fileLine => {
  const parsedLines = fileLine.split(" ");
  const secondOperandExists = parsedLines.length === 3;
  let secondOperandValue = "";
  if (secondOperandExists) {
    if (!_.isNaN(Number(parsedLines[2]))) {
      secondOperandValue = Number(parsedLines[2]);
    } else {
      secondOperandValue = parsedLines[2];
    }
  }
  return {
    instruction: parsedLines[0],
    firstOperand: parsedLines[1],
    secondOperand: secondOperandValue
  };
};

const parseInput = fileLines => {
  const cpuInstructions = [];
  fileLines.forEach(singleLine => {
    cpuInstructions.push(parseSingleLine(singleLine));
  });
  return cpuInstructions;
};

const isOperandRegister = operand => {
  return _.isString(operand);
};

const putValueToRegister = (registers, destinationRegister, value) => {
  const registersCopy = _.cloneDeep(registers);
  registersCopy[destinationRegister] = value;
  return registersCopy;
};

const getValueFromRegister = (registers, register) => {
  return registers[register];
};

const executeProgram = inputLines => {
  const instructions = parseInput(inputLines);
  let registers = {
    a: 0,
    b: 0,
    c: 0,
    d: 0,
    e: 0,
    f: 0,
    g: 0,
    h: 0
  };
  let cpuInstructionsPosition = 0;
  let mulCounter = 0;
  while (cpuInstructionsPosition < instructions.length) {
    const instruction = instructions[cpuInstructionsPosition];
    switch (instruction.instruction) {
      case "set": {
        const value = isOperandRegister(instruction.secondOperand)
          ? getValueFromRegister(registers, instruction.secondOperand)
          : instruction.secondOperand;
        registers = putValueToRegister(
          registers,
          instruction.firstOperand,
          value
        );
        cpuInstructionsPosition += 1;
        break;
      }
      case "sub": {
        const valueToDecreaseBy = isOperandRegister(instruction.secondOperand)
          ? getValueFromRegister(registers, instruction.secondOperand)
          : instruction.secondOperand;
        const currentValueInRegister = getValueFromRegister(
          registers,
          instruction.firstOperand
        );
        const substraction = currentValueInRegister - valueToDecreaseBy;
        registers = putValueToRegister(
          registers,
          instruction.firstOperand,
          substraction
        );
        cpuInstructionsPosition += 1;
        break;
      }
      case "mul": {
        mulCounter += 1;
        const valueToMultiplyBy = isOperandRegister(instruction.secondOperand)
          ? getValueFromRegister(registers, instruction.secondOperand)
          : instruction.secondOperand;
        const currentValueInRegister = getValueFromRegister(
          registers,
          instruction.firstOperand
        );
        const result = currentValueInRegister * valueToMultiplyBy;
        registers = putValueToRegister(
          registers,
          instruction.firstOperand,
          result
        );
        cpuInstructionsPosition += 1;
        break;
      }
      case "jnz": {
        const condition = isOperandRegister(instruction.firstOperand)
          ? getValueFromRegister(registers, instruction.firstOperand)
          : instruction.firstOperand;
        const jumpOffset = isOperandRegister(instruction.secondOperand)
          ? getValueFromRegister(registers, instruction.secondOperand)
          : instruction.secondOperand;
        if (condition !== 0) {
          cpuInstructionsPosition += jumpOffset;
        } else {
          cpuInstructionsPosition += 1;
        }
        break;
      }
    }
  }
  console.log(`Mul counter: ${mulCounter}`);
};

const findPrimesCnt = (lowRange, highRange) => {
  let cntH = 0;
  for (let cnt = lowRange; cnt <= highRange; cnt += 17) {
    for (let innerCnt = 2; innerCnt < cnt; innerCnt += 1) {
      if (cnt % innerCnt === 0) {
        cntH += 1;
        break;
      }
    }
  }
  console.log(cntH);
};

exports.executeProgram = executeProgram;
exports.findPrimesCnt = findPrimesCnt;
