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
  return registers[register] || 0;
};

const executeProgram = inputLines => {
  const instructions = parseInput(inputLines);
  let registers = {};
  let cpuInstructionsPosition = 0;
  let recoverExecuted = false;
  let lastFrequency = 0;
  while (
    !recoverExecuted &&
    cpuInstructionsPosition >= 0 &&
    cpuInstructionsPosition < instructions.length
  ) {
    const instruction = instructions[cpuInstructionsPosition];
    switch (instruction.instruction) {
      case "snd": {
        lastFrequency = getValueFromRegister(
          registers,
          instruction.firstOperand
        );
        cpuInstructionsPosition += 1;
        break;
      }
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
      case "add": {
        const valueToAdd = isOperandRegister(instruction.secondOperand)
          ? getValueFromRegister(registers, instruction.secondOperand)
          : instruction.secondOperand;
        const currentValueInRegister = getValueFromRegister(
          registers,
          instruction.firstOperand
        );
        const sum = currentValueInRegister + valueToAdd;
        registers = putValueToRegister(
          registers,
          instruction.firstOperand,
          sum
        );
        cpuInstructionsPosition += 1;
        break;
      }
      case "mul": {
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
      case "mod": {
        const valueToModuloBy = isOperandRegister(instruction.secondOperand)
          ? getValueFromRegister(registers, instruction.secondOperand)
          : instruction.secondOperand;
        const currentValueInRegister = getValueFromRegister(
          registers,
          instruction.firstOperand
        );
        const result = currentValueInRegister % valueToModuloBy;
        registers = putValueToRegister(
          registers,
          instruction.firstOperand,
          result
        );
        cpuInstructionsPosition += 1;
        break;
      }
      case "rcv": {
        const currentValueInRegister = getValueFromRegister(
          registers,
          instruction.firstOperand
        );
        if (currentValueInRegister !== 0) {
          recoverExecuted = true;
        }
        cpuInstructionsPosition += 1;
        break;
      }
      case "jgz": {
        const condition = isOperandRegister(instruction.firstOperand)
          ? getValueFromRegister(registers, instruction.firstOperand)
          : instruction.firstOperand;
        const jumpOffset = isOperandRegister(instruction.secondOperand)
          ? getValueFromRegister(registers, instruction.secondOperand)
          : instruction.secondOperand;
        if (condition > 0) {
          cpuInstructionsPosition += jumpOffset;
        } else {
          cpuInstructionsPosition += 1;
        }
        break;
      }
    }
  }
  return lastFrequency;
};

const executeOperation = (
  instructions,
  registers,
  cpuPositionIndex,
  firstProgramQueue,
  secondProgramQueue,
  program
) => {
  let registersCopy = _.cloneDeep(registers);
  let cpuPositionIndexCopy = cpuPositionIndex;
  let firstProgramQueueCopy = [...firstProgramQueue];
  let secondProgramQueueCopy = [...secondProgramQueue];
  let isWaiting = false;

  const instruction = instructions[cpuPositionIndexCopy];
  switch (instruction.instruction) {
    case "snd": {
      const valueToSend = getValueFromRegister(
        registersCopy,
        instruction.firstOperand
      );
      if (program === 0) {
        secondProgramQueueCopy.push(valueToSend);
      }
      if (program === 1) {
        firstProgramQueueCopy.push(valueToSend);
      }
      registersCopy.sendCount += 1;
      cpuPositionIndexCopy += 1;
      break;
    }
    case "set": {
      const value = isOperandRegister(instruction.secondOperand)
        ? getValueFromRegister(registersCopy, instruction.secondOperand)
        : instruction.secondOperand;
      registersCopy = putValueToRegister(
        registersCopy,
        instruction.firstOperand,
        value
      );
      cpuPositionIndexCopy += 1;
      break;
    }
    case "add": {
      const valueToAdd = isOperandRegister(instruction.secondOperand)
        ? getValueFromRegister(registersCopy, instruction.secondOperand)
        : instruction.secondOperand;
      const currentValueInRegister = getValueFromRegister(
        registersCopy,
        instruction.firstOperand
      );
      const sum = currentValueInRegister + valueToAdd;
      registersCopy = putValueToRegister(
        registersCopy,
        instruction.firstOperand,
        sum
      );
      cpuPositionIndexCopy += 1;
      break;
    }
    case "mul": {
      const valueToMultiplyBy = isOperandRegister(instruction.secondOperand)
        ? getValueFromRegister(registersCopy, instruction.secondOperand)
        : instruction.secondOperand;
      const currentValueInRegister = getValueFromRegister(
        registersCopy,
        instruction.firstOperand
      );
      const result = currentValueInRegister * valueToMultiplyBy;
      registersCopy = putValueToRegister(
        registersCopy,
        instruction.firstOperand,
        result
      );
      cpuPositionIndexCopy += 1;
      break;
    }
    case "mod": {
      const valueToModuloBy = isOperandRegister(instruction.secondOperand)
        ? getValueFromRegister(registersCopy, instruction.secondOperand)
        : instruction.secondOperand;
      const currentValueInRegister = getValueFromRegister(
        registersCopy,
        instruction.firstOperand
      );
      const result = currentValueInRegister % valueToModuloBy;
      registersCopy = putValueToRegister(
        registersCopy,
        instruction.firstOperand,
        result
      );
      cpuPositionIndexCopy += 1;
      break;
    }
    case "rcv": {
      if (program === 0) {
        if (firstProgramQueueCopy.length === 0) {
          isWaiting = true;
        } else {
          const valueToSave = firstProgramQueueCopy.shift();
          registersCopy = putValueToRegister(
            registersCopy,
            instruction.firstOperand,
            valueToSave
          );
          cpuPositionIndexCopy += 1;
        }
      }
      if (program === 1) {
        if (secondProgramQueueCopy.length === 0) {
          isWaiting = true;
        } else {
          const valueToSave = secondProgramQueueCopy.shift();
          registersCopy = putValueToRegister(
            registersCopy,
            instruction.firstOperand,
            valueToSave
          );
          cpuPositionIndexCopy += 1;
        }
      }
      break;
    }
    case "jgz": {
      const condition = isOperandRegister(instruction.firstOperand)
        ? getValueFromRegister(registersCopy, instruction.firstOperand)
        : instruction.firstOperand;
      const jumpOffset = isOperandRegister(instruction.secondOperand)
        ? getValueFromRegister(registersCopy, instruction.secondOperand)
        : instruction.secondOperand;
      if (condition > 0) {
        cpuPositionIndexCopy += jumpOffset;
      } else {
        cpuPositionIndexCopy += 1;
      }
      break;
    }
  }
  return {
    registers: registersCopy,
    cpuPosition: cpuPositionIndexCopy,
    firstProgramQueue: firstProgramQueueCopy,
    secondProgramQueue: secondProgramQueueCopy,
    isWaiting: isWaiting
  };
};

const executeProgramTwiceAtTheSameTime = inputLines => {
  const instructions = parseInput(inputLines);
  let firstProgramWaiting = false;
  let secondProgramWaiting = false;
  let firstProgramRegisters = {
    p: 0,
    sendCount: 0
  };
  let secondProgramRegisters = {
    p: 1,
    sendCount: 0
  };
  let firstProgramCpuInstructionsPosition = 0;
  let secondProgramCpuInstructionsPosition = 0;
  let firstProgramQueue = [];
  let secondProgramQueue = [];
  while (!(firstProgramWaiting && secondProgramWaiting)) {
    if (
      firstProgramCpuInstructionsPosition >= 0 &&
      firstProgramCpuInstructionsPosition < instructions.length
    ) {
      const firstProgramResult = executeOperation(
        instructions,
        firstProgramRegisters,
        firstProgramCpuInstructionsPosition,
        firstProgramQueue,
        secondProgramQueue,
        0
      );
      firstProgramWaiting = firstProgramResult.isWaiting;
      firstProgramRegisters = firstProgramResult.registers;
      firstProgramCpuInstructionsPosition = firstProgramResult.cpuPosition;
      firstProgramQueue = firstProgramResult.firstProgramQueue;
      secondProgramQueue = firstProgramResult.secondProgramQueue;
    }
    if (
      secondProgramCpuInstructionsPosition >= 0 &&
      secondProgramCpuInstructionsPosition < instructions.length
    ) {
      const secondProgramResult = executeOperation(
        instructions,
        secondProgramRegisters,
        secondProgramCpuInstructionsPosition,
        firstProgramQueue,
        secondProgramQueue,
        1
      );
      secondProgramWaiting = secondProgramResult.isWaiting;
      secondProgramRegisters = secondProgramResult.registers;
      secondProgramCpuInstructionsPosition = secondProgramResult.cpuPosition;
      firstProgramQueue = secondProgramResult.firstProgramQueue;
      secondProgramQueue = secondProgramResult.secondProgramQueue;
    }
    if (
      (firstProgramCpuInstructionsPosition < 0 ||
        firstProgramCpuInstructionsPosition >= instructions.length) &&
      (secondProgramCpuInstructionsPosition < 0 ||
        secondProgramCpuInstructionsPosition >= instructions.length)
    ) {
      break;
    }
  }
  return firstProgramRegisters.sendCount;
};

exports.executeProgram = executeProgram;
exports.executeProgramTwiceAtTheSameTime = executeProgramTwiceAtTheSameTime;
